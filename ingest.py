import os
import shutil
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

# 0. Cleanup old DB 
if os.path.exists("./chroma_db"):
    shutil.rmtree("./chroma_db")

# 1. Load the data
loader = TextLoader("./data/policy.txt", encoding="utf-8")
documents = loader.load()

# 2. Split the text 
# WHY THIS CHUNK SIZE?
# We use a chunk size of 1000 characters with a 200 character overlap.
# - Size (1000): Large enough to capture a full policy(context), but small enough
#   to fit multiple retrieved chunks into the LLM's context window.
# - Overlap (200): Prevents cutting a sentence in half at the boundary, ensuring 
#   critical meaning isn't lost between chunks.
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""] # Try to split by paragraphs first
)
chunks = text_splitter.split_documents(documents)

print(f"Split {len(documents)} document(s) into {len(chunks)} chunks.")

# 3. Create Vector Store (ChromaDB)
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001"),
    persist_directory="./chroma_db"
)

print("Ingestion complete! Data saved to ./chroma_db")
