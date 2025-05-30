from flask import Flask, render_template, redirect, request, abort, session
from database import Database
import random
import os
import json
import datetime


app = Flask(__name__)
app.secret_key = os.environ["APP_SESSION_KEY"]
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)

db = Database()


@app.before_request
def make_session_permanent():
    session.permanent = True

@app.errorhandler(400)
@app.errorhandler(404)
def handle_bad_request(e):
    return render_template("error.html", error_code=e.code), e.code

@app.route("/")
def index():
    if not session.get("answered"):
        session["answered"] = []

    count = db.query("SELECT COUNT(*) FROM questions;")[0]

    if len(session["answered"]) == count:
        session["answered"] = []

    qid = random.choice(list(set(range(1, count + 1)).difference(set(session["answered"]))))

    return redirect(f"/questions?qid={qid}")

@app.route("/questions", methods=["GET", "POST"])
def question():
    count = db.query("SELECT COUNT(*) FROM questions;")[0]

    qid = request.args.get("qid")
    if qid is None or not qid.isnumeric():
        abort(400)
    
    try:
        question, answer = db.query(f"SELECT question, answer FROM questions WHERE qid={qid};")
    except TypeError:
        abort(400)

    if request.method == "POST":
        if not session.get("answered"):
            session["answered"] = []
        
        if request.form.get("reset") == "true":
            session["answered"] = []
        else:
            if not qid in session["answered"]:
                session["answered"] = session["answered"] + [qid]

            choice = request.form.get("choice")
            msg = None 

            if choice != str(answer).lower():
                msg = db.query(f"SELECT explanation FROM explanations WHERE qid={qid};")
                if msg is not None:
                    msg = msg[0]

            return render_template("question.html", qid=qid, question=question, answer=answer, next=True, choice=choice, msg=msg, completed=len(session["answered"]), total=count)

    return render_template("question.html", qid=qid, question=question, answer=answer, next=False, choice=None, msg=None, completed=len(session["answered"]), total=count)

@app.route("/api/v1")
def api_endpoint():
    qid = request.args.get("qid")
    if qid is None or qid == "":
        return json.dumps(
            {
                "status": 400,
                "message": "Missing qid."
            }, indent=4)

    if not qid.isnumeric():
        return json.dumps(
            {
                "status": 400,
                "message": "Qid must be an integer."
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
