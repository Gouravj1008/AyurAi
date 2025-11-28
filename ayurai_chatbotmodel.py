# ayurai_chatbot_model.py
# Uses trained Ayurveda Q&A model

import joblib
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load trained artifacts
vectorizer = joblib.load("vectorizer.joblib")
question_vectors = joblib.load("question_vectors.joblib")
questions = joblib.load("questions_list.joblib")
answers = joblib.load("answers_list.joblib")

def get_best_answer(user_question: str) -> str:
    # Convert user question to vector
    user_vec = vectorizer.transform([user_question])

    # Compute similarity with all training questions
    sims = cosine_similarity(user_vec, question_vectors)[0]

    # Get index of most similar question
    best_idx = sims.argmax()
    best_score = sims[best_idx]

    # Optional: if similarity is very low, say "I don't know"
    if best_score < 0.1:
        return "I am not sure about this. Please rephrase or ask something else in Ayurveda."

    return answers[best_idx]

if __name__ == "__main__":
    print("AyurAI (Model-based) – type 'exit' to quit.")
    while True:
        q = input("\nYou: ")
        if q.lower() in ["exit", "quit"]:
            break
        print("AyurAI:", get_best_answer(q))
