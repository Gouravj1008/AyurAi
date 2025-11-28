# train_model.py
# Train a simple Ayurveda Q&A retrieval model

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# 1. Load your Q&A data
data = pd.read_csv("ayurveda_qa.csv")   # file from step 2

questions = data["question"].astype(str).tolist()
answers = data["answer"].astype(str).tolist()

# 2. Convert questions to numeric vectors using TF-IDF
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

# 3. Save the vectorizer and data for later use
joblib.dump(vectorizer, "vectorizer.joblib")
joblib.dump(question_vectors, "question_vectors.joblib")
joblib.dump(questions, "questions_list.joblib")
joblib.dump(answers, "answers_list.joblib")

print("Model trained and saved successfully!")
