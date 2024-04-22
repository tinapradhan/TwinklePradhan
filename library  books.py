#create databse mysql#
import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="library"
)
mycursor= mydb.cursor()
mycursor.execute("create database library")
print("Database  created successfully.")
mycursor.execute("create table books (id int(2) primary key Auto_Increment, Name varchar (155), Author varchar(155), Edition varchar(10), language varchar(120))")
print("Table created successfully.")
mycursor= mydb.cursor()
sql ="insert into books ( id, name, author, edition, language) values(%s,%s,%s,%s,%s)"
val=[
    ('',"Java","Balaguruswamy","4th ","English"),
    ('',"Pyhton","Dan Barder","5th","English"),
    ('',"Data Structure","Anuradha","3th","English")
    ]
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")
