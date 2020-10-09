import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "myusername",
    password = "mypassword",
    database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "INSER INTO customers (name, address) VALUES (%s,%s)"

val = ("Jhon","highway 21")


mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount,"record inserted.")
