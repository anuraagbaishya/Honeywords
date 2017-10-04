from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/anuraag/Projects/honeywords/user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_BINDS'] = { 'index': 'sqlite:////home/anuraag/Projects/honeywords/index.db'}
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(80), unique=True, primary_key=True)
    password = db.Column(db.String(360))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

class Index(db.Model):
	__bind_key__ = 'index'	

	username = db.Column(db.String(80), unique=True, primary_key=True)
	index = db.Column(db.String(160))

	def __init__(self, username, index):
		self.username = username
		self.index = index

	def __repr__(self):
		return '<User %r>' % self.username