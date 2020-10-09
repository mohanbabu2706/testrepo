import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "myusername",
    password = "mypassword"
)

mycusor = mydb.cursor()

mycusor.execute("CREATE DATABASE mydatabase")
