import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "myusername",
    password = "mypassword",
    databasse = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
