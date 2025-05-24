from flask import Flask, render_template, redirect, request
from database import Database
import random 


app = Flask(__name__)

db = Database()


@app.route("/")
def index():
    count = db.query("SELECT COUNT(*) FROM questions;")[0]
    qid = random.randint(1, count)
    return redirect(f"/{qid}")

@app.route("/<int:qid>", methods=["GET", "POST"])
def question(qid):
    question, answer = db.query(f"SELECT question, answer FROM questions WHERE qid={qid}")

    if request.method == "POST":
        print(request.form.get("choice"))
        print(answer)
        return render_template("question.html", qid=qid, question=question, answer=answer, next=True, choice=request.form.get("choice"))
    else:
        return render_template("question.html", qid=qid, question=question, answer=answer, next=False)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
    db.close()
