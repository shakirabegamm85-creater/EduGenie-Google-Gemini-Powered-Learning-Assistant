import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"answer": "Please enter a question."}), 400
    if not api_key:
        return jsonify({"answer": "Add GEMINI_API_KEY to your .env file."}), 500
    try:
        model = genai.GenerativeModel("gemini-3.8-flash")
        prompt = f"""You are EduGenie, a friendly educational assistant.
Explain this topic clearly for a college student using simple language and examples:

{question}"""
        response = model.generate_content(prompt)
        return jsonify({"answer": response.text})
    except Exception as exc:
        return jsonify({"answer": f"Error: {exc}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
