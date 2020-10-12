import mysql.connector

mydb = mysql.connecotr.connect(
    host = "localhost",
    user = "myusername",
    password = "mypassword",
    database = "mydatabase"
)

mycursor  = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
