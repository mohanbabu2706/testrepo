import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "myusername",
    password = "mypassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASE")

for x in mycursor:
    print(x)
