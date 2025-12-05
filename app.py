from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer
import numpy as np
load_dotenv()
api_key = os.getenv("API_KEY")
client=OpenAI(api_key=api_key)
def load_knowledge_base(folder="knowledge_base"):
    kb = {}
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                kb[filename] = f.read()
    return kb
knowledge_base = load_knowledge_base()
model = SentenceTransformer("all-MiniLM-L6-v2")
documents = list(knowledge_base.values())
doc_names = list(knowledge_base.keys())
doc_embeddings = model.encode(documents, convert_to_numpy=True)
def find_best_document(question, model, doc_embeddings, documents, doc_names):
    q_vec = model.encode([question], convert_to_numpy=True)
    similarities = np.dot(doc_embeddings, q_vec.T).squeeze()
    best_idx = similarities.argmax()
    best_doc_name = doc_names[best_idx]
    best_doc_text = documents[best_idx]
    return best_doc_name, best_doc_text
def answer_question(question):
    best_name, best_text = find_best_document(question, model, doc_embeddings, documents, doc_names)
    prompt = f"""
You are a helpful assistant for Metropolia students. Answer the student's question using the information below. 
If the information does not explicitly mention the answer, do your best to provide a helpful and reasonable response based on the context. 
Avoid making up information that is not supported by the text.
Source file: {best_name}
Information: {best_text}
Question: {question} """
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )
    return response.output_text
app = Flask(__name__) 
@app.route('/', methods=["GET","POST"])     
 
def index():
    answer = None
    if request.method == "POST":
        question = request.form.get("question")
        answer = answer_question(question)
    return render_template("index.html", answer=answer)    
    
if __name__ == "__main__":
    app.run(debug=True)