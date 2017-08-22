from flask import Flask, render_template, request, url_for
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/login/', methods=['POST'])
def login():
	user = request.form['user']
	pwd = request.form['pass']
	return render_template('res.html', user = user, pwd = pwd)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

