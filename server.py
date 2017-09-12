import random
import hashlib
import sqlite3 as sl3
f = open("password")
passwords = f.read().splitlines()
conn = sl3.connect("user.db")


conn.execute('''CREATE TABLE IF NOT EXISTS USER
     (USERNAME INT PRIMARY KEY NOT NULL,
      PASSWORD TEXT NOT NULL);''')

ch = int(input("1.Sign Up 2.Login: "))

if ch == 1:

	username = input("Username: ")
	password = input("Enter password: ")
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
	print(len(stringified))

	conn.execute('INSERT INTO USER (USERNAME, PASSWORD) VALUES (?,?)',(username, stringified))
	conn.commit()

else:

	username = input("Username: ")
	password = input("Password: ")
	hashname = hashlib.md5(username.encode('utf-8')).hexdigest()
	index = index_calc(hashname)
	hashword = hashlib.md5(password.encode('utf-8')).hexdigest()

	curr = conn.cursor()
	curr.execute('SELECT PASSWORD FROM USER WHERE USERNAME=?',(username,))
	
	rows = curr.fetchall()
	lst = eval(''.join(rows[0]))
	i = lst.index(hashword) if hashword in lst else -1
	if i == index:
		print('Success')
	elif i == -1:
		print('Fail')
	else:
		print('Honeyword')

		
