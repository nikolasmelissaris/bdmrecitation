#!/usr/local/bin/python3
print("Content-Type: text/html")
print()

import pymysql
import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
weapon = form.getvalue('fname')
print("Heroes that use:", weapon)


# Open connection to the database
db = pymysql.connect("localhost","root","mypassword","fellowship_of_the_ring" )

# Start a cursor object using cursor() method
cursor = db.cursor()
sql = f"""SELECT * FROM heroes WHERE weapon={weapon};"""
# Execute a SQL query using execute() method. This should return all the columns of heroes that use swords.
cursor.execute(sql)

# Fetch all the rows using fetchall() method.
data = cursor.fetchall()
print (data)

# disconnect from server
db.close()
