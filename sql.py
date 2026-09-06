import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password= 'luqman2499',
    database = 'students'
    )

mycursor = mydb.cursor()

