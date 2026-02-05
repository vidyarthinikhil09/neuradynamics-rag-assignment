import pandas as pd
from rag_agent import answer_question

# 1. Define the Test Dataset
# We include specific categories as requested in the assignment:
# - Answerable (Ground Truth exists)
# - Edge Case (Ambiguous or partially mentioned)
# - Unanswerable (Hallucination trap)
test_questions = [
    {
        "category": "Answerable",
        "question": "What is the policy on web scraping?",
        "expected_key_concept": "Prohibited / Not allowed"
    },
    {
        "category": "Answerable",
        "question": "How long is support chat data retained?",
        "expected_key_concept": "90 days"
    },
    {
        "category": "Edge Case",
        "question": "Can I use the AI to generate political content?",
        "expected_key_concept": "Harmful/Unethical content is prohibited"
    },
    {
        "category": "Unanswerable",
        "question": "What is the phone number for the HR department?",
        "expected_key_concept": "I cannot answer / Not in document"
    },
    {
        "category": "Unanswerable",
        "question": "Does the company offer a refund for the annual plan?",
        "expected_key_concept": "I cannot answer (Refunds not explicitly detailed for annual vs monthly)"
    }
]

# 2. Run Evaluation
results = []

print("--- Starting Automated Evaluation ---")

for i, item in enumerate(test_questions):
    print(f"Testing Q{i+1}: {item['question']}...")
    
    # Get actual response from our Agent
    response_text, sources = answer_question(item['question'])
    
    # Check if the retrieved context was actually used (Simple heuristic)
    retrieved_source_names = [doc.metadata.get('source', 'policy.txt') for doc, _ in sources]
    
    results.append({
        "Category": item["category"],
        "Question": item["question"],
        "Expected": item["expected_key_concept"],
        "Actual_Answer": response_text,
        "Source_Used": list(set(retrieved_source_names))
    })

# 3. Save Results
df = pd.DataFrame(results)

# Save to Markdown (Great for your GitHub README)
markdown_report = df.to_markdown(index=False)
with open("evaluation_report.md", "w", encoding="utf-8") as f:
    f.write("# RAG System Evaluation Report\n\n")
    f.write(markdown_report)

# Save to CSV (for analysis)
df.to_csv("evaluation_results.csv", index=False)

print("\nEvaluation Complete! Results saved to 'evaluation_report.md'")
print("-" * 30)
print(markdown_report)