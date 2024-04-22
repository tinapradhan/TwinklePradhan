#create databse mysql
import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory"
)
mycursor= mydb.cursor()
mycursor.execute("create database inventory")
print("Database  created successfully.")

mycursor.execute("create table invention (id int(2) primary key Auto_Increment, Name varchar (155), Model no varchar(155), Inventor varchar(10), Date of Issuevarchar(120))")
print("Table created successfully.")
mycursor= mydb.cursor()
sql ="insert into invention ( id, Name, Model no, Inventor, Date of Issue) values(%s,%s,%s,%s,%s)"
val=[
    ('',"car","o4","sufus","5/6/2003"),
    ('',"bike","hh9","jdf","7/6/2000"),
    ('',"scooty","ik67","kfhh","8/7/2008")
]
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")
