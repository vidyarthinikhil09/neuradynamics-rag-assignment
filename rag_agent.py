import os
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings # CHANGED
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

# 1. Setup - Load DB and Model
# Must match the embedding model used in ingest.py
embedding_function = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embedding_function)

# Using Gemini 1.5 Flash for speed and efficiency
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite", 
    temperature=0
    )

# 2. Retrieval Function
def retrieve_docs(question, k=3):
    results = vector_store.similarity_search_with_score(question, k=k)
    return results

# 3. Generation Function
def answer_question(question):
    results = retrieve_docs(question)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    template = """
    You are an intelligent assistant for "Pragya" (Neuradynamics). 
    Answer strictly based on the provided context.

    RULES:
    1. Use ONLY the provided context.
    2. If the answer is not in the context, say: "I cannot answer this based on the provided policy documents."
    3. Format with bullet points where appropriate.
    
    CONTEXT:
    {context}
    
    USER QUESTION:
    {question}
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm
    
    response = chain.invoke({"context": context_text, "question": question})
    return response.content, results

# 4. Loop
if __name__ == "__main__":
    print("--- Pragya Policy Agent ---")
    while True:
        query = input("\nUser: ")
        if query.lower() in ["exit", "quit"]:
            break
        
        answer, sources = answer_question(query)
        print(f"\nAgent:\n{answer}")