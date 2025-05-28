from flask import Flask, render_template, redirect, request
from database import Database
import random
import os
import json


app = Flask(__name__)

db = Database()


@app.route("/")
def index():
    count = db.query("SELECT COUNT(*) FROM questions;")[0]
    qid = random.randint(1, count)
    return redirect(f"/questions?qid={qid}")

@app.route("/questions", methods=["GET", "POST"])
def question():
    qid = request.args.get("qid")
    question, answer = db.query(f"SELECT question, answer FROM questions WHERE qid={qid};")

    if request.method == "POST":
        choice = request.form.get("choice")
        msg = None 

        if choice != str(answer).lower():
            msg = db.query(f"SELECT explanation FROM explanations WHERE qid={qid};")
            if msg is not None:
                msg = msg[0]

        return render_template("question.html", qid=qid, question=question, answer=answer, next=True, choice=choice, msg=msg)
    else:
        return render_template("question.html", qid=qid, question=question, answer=answer, next=False, choice=None, msg=None)
    
@app.route("/report")
def report():
    return render_template("report.html")

@app.route("/api/v1")
def api_endpoint():
    qid = request.args.get("qid")
    if qid is None:
        return json.dumps(
            {
                "status": 400,
                "message": "Missing qid."
            }, indent=4)

    try:
        question, answer = db.query(f"SELECT question, answer FROM questions WHERE qid={qid}")
    except TypeError:
        return json.dumps(
        {
            "status": 400,
            "message": "Qid does not exist."
        }, indent=4)
    
    return json.dumps(
    {
        "status": 200,
        "message": "Content retrieved successfully.",
        "question": question,
        "answer": answer
    }, indent=4)


if __name__ == "__main__":
    app.run(port=os.environ["APP_PORT"], debug=True)
    db.close()
