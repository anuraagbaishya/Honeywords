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

	index = 0
	for pwd in password:
		index += ord(pwd)

	index = index%10
	print(index)
	honeywords = []

	for i in range(10):
		if i == index:
			honeywords.append(password)
		else:
			pwd = passwords[random.randint(1, 999999)]
			honeywords.append(pwd)
	
		honeywords[i] = hashlib.md5(honeywords[i].encode('utf-8')).hexdigest()

	stringified = repr(honeywords)
	print(stringified)

	conn.execute('INSERT INTO USER (USERNAME, PASSWORD) VALUES (?,?)',(username, stringified))
	conn.commit()

else:

	username = input("Username: ")
	curr = conn.cursor()
	curr.execute('SELECT PASSWORD FROM USER WHERE USERNAME=?',(username,))
	
	rows = curr.fetchall()
	lst = eval(''.join(rows[0]))
	for l in lst:
		print(l)
