from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAQ data
questions = []
answers = []

with open("faqs.txt", "r") as file:
    for line in file:
        q, a = line.strip().split("|")
        questions.append(q)
        answers.append(a)

# Convert questions into embeddings
question_embeddings = model.encode(questions)

# User query
query = input("Ask your question: ")

# Convert query to embedding
query_embedding = model.encode([query])

# Similarity search
scores = cosine_similarity(query_embedding, question_embeddings)

# Get best match
best_index = scores.argmax()

print("\nBest Answer:")
print(answers[best_index])