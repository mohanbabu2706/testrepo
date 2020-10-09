import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "myusername",
    password = "mypassword",
    database = "mydatabase"
)

mycursor = mudb.cursor()

sql = "INSERT INTO customers(name,address) VALUES (%s,%s)"
val = [
    ('peter','Lowstreet 4'),
    ('Amy','Apple st 652'),
    ('Hanna','Mountain 21'),
    ('Michael','Valley 345'),
    ('Sandy','Ocean blvd 2'),
    ('Betty','Green Grass 1'),
    ('Richard','Sky st 331'),
    ('Susan','One way 98'),
    ('Vicky','Yellow Garden 2'),
    ('Ben','Park Lane 38'),
    ('William','Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sidway 1633')
]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount,"record was inserted.")
