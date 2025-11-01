from datetime import date
from todo import db

class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    details = db.Column(db.String(length=150), nullable=False)
    # due = db.Column(db.Date(), default=date.today)
    priority = db.Column(db.Integer(), default=0 )
    is_complete = db.Column(db.Boolean(), default=False)