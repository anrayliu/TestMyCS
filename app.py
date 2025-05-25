from flask import Flask, render_template, redirect, request
from database import Database
import random
import json


app = Flask(__name__)

db = Database()


@app.route("/")
def root():
    count = db.query("SELECT COUNT(*) FROM questions;")[0]
    qid = random.randint(1, count)
    return redirect(f"/questions?id={qid}")

@app.route("/questions", methods=["GET", "POST"])
def question():
    qid = request.args.get("id")
    question, answer = db.query(f"SELECT question, answer FROM questions WHERE qid={qid}")

    if request.method == "POST":
        return render_template("question.html", qid=qid, question=question, answer=answer, next=True, choice=request.form.get("choice"))
    else:
        return render_template("question.html", qid=qid, question=question, answer=answer, next=False)

@app.route("/api/v1")
def api_endpoint():
    qid = request.args.get("id")
    try:
        question, answer = db.query(f"SELECT question, answer FROM questions WHERE qid={qid}")
    except TypeError:
        return "Bad qid", 400

    return json.dumps({
        "question": question,
        "answer": answer
    })


if __name__ == "__main__":
    app.run(port=5001, debug=True)
    db.close()
