from flask import Flask, render_template, request, url_for, flash
from datetime import datetime
from db_models import User, Index, db
import hashlib, random, os, boto3

kms = boto3.client('kms', region_name='eu-central-1')
key_id = 'alias/honeywords'

f = open("password")
passwords = f.read().splitlines()

def kms_encrypt_index(index):
	enc = kms.encrypt(KeyId=key_id, Plaintext=str(index))
	return enc['CiphertextBlob']

def kms_decrypt_index(ctb):
	dec = kms.decrypt(CiphertextBlob=ctb)
	return int(dec['Plaintext'])

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/anuraag/Projects/honeywords/user.db'
app.config['SQLALCHEMY_BINDS'] = { 'index': 'sqlite:////home/anuraag/Projects/honeywords/index.db'}
@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/login/', methods=['POST'])
def login():
	username = request.form['user']
	password = request.form['pass']
	
	enc_i = Index.query.filter_by(username=username).first().index
	index = kms_decrypt_index(enc_i)
	
	hashword = hashlib.md5(password.encode('utf-8')).hexdigest()

	user = User.query.filter_by(username=username).first()

	lst = eval(''.join(user.password))
	i = lst.index(hashword) if hashword in lst else -1
	if i == index:
		return 'OK'
	elif i == -1:
		return 'WRONG'
	else:
		return('Honeyword')
	

@app.route('/signup/', methods=['POST'])
def signup():
	username = request.form['user']
	password = request.form['pass']
	
	hashname = hashlib.md5(username.encode('utf-8')).hexdigest()

	honeywords = []

	index = (int.from_bytes(os.urandom(1), byteorder='little')%10)

	print(index)

	for i in range(10):
		if i == index:
			honeywords.append(password)
		else:
			pwd = passwords[random.randint(1, 999999)]
			print(pwd)
			honeywords.append(pwd)
	
		honeywords[i] = hashlib.md5(honeywords[i].encode('utf-8')).hexdigest()

	stringified = repr(honeywords)

	encrypted_index = kms_encrypt_index(index)

	user = User(username, stringified)
	db.session.add(user)
	db.session.commit()
	
	index = Index(username, encrypted_index)
	db.session.add(index)
	db.session.commit()

	return 'OK'

if __name__ == '__main__':
	db.init_app(app)
	db.create_all()
	app.secret_key = 'secret'
	app.run(debug=True, use_reloader=True)

