from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SECRET KEY']='f4a8dd522d3e19909f78b669'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

from src import routes
