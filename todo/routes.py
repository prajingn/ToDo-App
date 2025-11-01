from todo import app, curr_date
from flask import render_template

@app.route("/")
@app.route("/home")
def pending():
    return render_template("pending.html", curr_date=curr_date)

@app.route("/complete")
def complete():
    return render_template("complete.html", curr_date=curr_date)