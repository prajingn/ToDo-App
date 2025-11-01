from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
db = SQLAlchemy(app)
curr_date = date.today().strftime("%b %d %Y")

from todo import routes