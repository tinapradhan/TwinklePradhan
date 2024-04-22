#create databse mysql
import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="receipe"
)
mycursor= mydb.cursor()
'''mycursor.execute("create database receipe")
print("Database  created successfully.")'''

mycursor.execute("create table food  (id int(2) primary key Auto_Increment, Name varchar (467) , Ingredient varchar (155),  Process varchar(155), Quantity varchar(10), Serving varchar(120))")
print("Table created successfully.")
'''mycursor= mydb.cursor()
sql ="insert into food ( id, name, ingredient, process, quantity, serving) values(%s,%s,%s,%s,%s)"
val=[
    ('',"pudding","carrot","boil","8pcs","4"),
    ('',"Juice","mango","peel and grind","8pcs","4"),
    ('',"","carrot","boil","8pcs","4")]
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")'''


