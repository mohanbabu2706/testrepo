import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "myusername",
    password = "mypassword",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers(name,address)VALUES(%s,%s)"

val = ("Michael","Blue Village")
mycursor.execute(sql,val)

mydb.commit()

print("1 record inserted ,ID:",mycursor.lastrowid)
