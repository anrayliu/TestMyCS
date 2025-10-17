from flask import Flask, render_template, redirect, request, abort, session, jsonify
from dotenv import load_dotenv
from database import Database
import random
import os


load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ["APP_SESSION_KEY"]

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

    # get questions that have not been answered yet
    qid = random.choice(list(set(map(str, range(1, count + 1))).difference(set(session["answered"]))))

    return redirect(f"/questions?qid={qid}")


@app.route("/questions", methods=["GET", "POST"])
def question():
    if not session.get("answered"):
        session["answered"] = []

    count = db.query("SELECT COUNT(*) FROM questions;")[0]

    qid = request.args.get("qid")
    if qid is None or not qid.isnumeric():
        abort(400)
    
    try:
        q, answer = db.query("SELECT question, answer FROM questions WHERE qid=%s;", args=(qid,))
    except TypeError:
        abort(400)

    if request.method == "POST":
        if request.form.get("reset") == "true":
            session["answered"] = []
        else:
            if not qid in session["answered"]:
                session["answered"] = session["answered"] + [qid]

            choice = request.form.get("choice")
            msg = None 

            if choice != str(answer).lower():
                msg = db.query("SELECT explanation FROM explanations WHERE qid=%s;", args=(qid,))
                if msg is not None:
                    msg = msg[0]

            return render_template("question.html", qid=qid, question=q, answer=answer, next=True, choice=choice, msg=msg, completed=len(session["answered"]), total=count)

    return render_template("question.html", qid=qid, question=q, answer=answer, next=False, choice=None, msg=None, completed=len(session["answered"]), total=count)


if __name__ == "__main__":
    app.run(port=int(os.environ["APP_PORT"]), debug=True)
