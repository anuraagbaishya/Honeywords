from flask import Flask, render_template, request, url_for
from datetime import datetime
from db_models import User, db
import hashlib, random

f = open("password")
passwords = f.read().splitlines()

def index_calc(string):

	index = 0
	for s in string:
		index += ord(s)

	return index%10

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/login/', methods=['POST'])
def login():
	username = request.form['user']
	password = request.form['pass']

	hashname = hashlib.md5(username.encode('utf-8')).hexdigest()
	index = index_calc(hashname)
	hashword = hashlib.md5(password.encode('utf-8')).hexdigest()

	user = User.query.filter_by(username=username).first()

	lst = eval(''.join(user.password))
	i = lst.index(hashword) if hashword in lst else -1
	if i == index:
		flash('Success')
	elif i == -1:
		flash('Fail')
	else:
		flash('Honeyword')

@app.route('/signup/', methods=['POST'])
def signup():
	username = request.form['user']
	password = request.form['pass']
	
	hashname = hashlib.md5(username.encode('utf-8')).hexdigest()

	honeywords = []

	index = index_calc(hashname)

	for i in range(10):
		if i == index:
			honeywords.append(password)
		else:
			pwd = passwords[random.randint(1, 999999)]
			print(pwd)
			honeywords.append(pwd)
	
		honeywords[i] = hashlib.md5(honeywords[i].encode('utf-8')).hexdigest()

	stringified = repr(honeywords)
	
	user = User(username, stringified)
	db.session.add(user)
	db.session.commit()
	flash('Successfully Added')

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

