from todo import app, curr_date, date, db, datetime, Task
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/pending")
def pending():
    return render_template("pending.html", curr_date=curr_date, date=date, tasks=Task.query.filter(Task.is_complete == False).all())
        
@app.route("/complete")
def complete():
    return render_template("complete.html", curr_date=curr_date, tasks=Task.query.filter(Task.is_complete == True).all())

@app.route("/add_task", methods=["POST"])
def add_task():
    t1 = Task(name=request.form["name"],
            details=request.form["details"],
            priority=request.form["priority"],
            due = datetime.strptime(request.form["due"], "%Y-%m-%d").date(),
            is_complete = False)
    db.session.add(t1)
    db.session.commit()
    return redirect(url_for("pending"))

@app.route("/clear_all", methods=["POST"])
def clear_all():
    page = request.form["page"].strip()
    if page == "pending":
        tasks=Task.query.filter(Task.is_complete == False).all()
    elif page == "complete":
        tasks=Task.query.filter(Task.is_complete == True).all()
    for t in tasks:
        db.session.delete(t)
    db.session.commit()
    return redirect(url_for(page))

@app.route("/task_options", methods=["GET", "POST"])
def task_options():
    task_id = int(request.form["id"])
    t = Task.query.get(task_id)

    if request.form["btn"] == "complete":
        t.is_complete = True
        db.session.commit()

    elif request.form["btn"] == "edit":
        print("hello")
        return render_template("edit_task.html", curr_date=curr_date, date=date, task_id=task_id, name=t.name, details=t.details)

    elif request.form["btn"] == "delete":
        db.session.delete(t)
        db.session.commit()

    return redirect(url_for("pending"))

@app.route("/edit_task/<int:id>", methods=["POST"])
def edit_task(id):
    t = Task.query.get(id)
    t.name=request.form["name"]
    t.details=request.form["details"]
    t.priority=request.form["priority"]
    t.due = datetime.strptime(request.form["due"], "%Y-%m-%d").date()

    db.session.commit()
    return redirect(url_for("pending"))