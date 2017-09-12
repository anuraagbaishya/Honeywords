from flask import Flask
from flask_sqlalchemy import SQLAlchemy as alchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = alchemy(app)

class User(db.Model):
	username = db.Column(db.String(20), primary_key=True)
	password = db.Column(db.String(360))

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return '{} {}'.format(username, password)

if __name__ == '__main__':
	db.create_all()
