from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql

# Create your views here.

def connect_database():
	con = sql.connect(host="localhost",user="root",password="",database = 'pythontest')

def home(request):

	return HttpResponse("I am a tester")

def insertdata():

	qry = 'INSERT INTO testtable (name,ph) VALUES (%s, %s)'
	return qry

def myform(request):
	d = {'title':'Studet Information',
	      'si' : 'Student Form',
	    }

	x = request.GET.get('username')
	y = request.GET.get('ph')
	print(x,y)
	d['na'] = x
	d['ph'] = y
    
	
	if x == None and y ==None:
		pass

	else:
    
		con = sql.connect(host="database-1.czcw8cekq1vt.eu-north-1.rds.amazonaws.com",user='admin',password="Amazon123",database = 'pythontest')

		db = con.cursor()

		insert = insertdata()
		data = (x,y)

		db.execute(insert,data)
		con.commit()
	
	return render(request,'index.html',d)
