import sqlite3

connection=sqlite3.connect("student.db")

##create a cursor object to insert record, create table, retrive
cursor=connection.cursor()

##create a table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

##insert some more records

cursor.execute('''INSERT INTO STUDENT VALUES('Sai','Data Science','A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Giri','Data Science','B',100);''')
cursor.execute('''INSERT INTO STUDENT VALUES('Thechina','Data Science','A',86);''')
cursor.execute('''INSERT INTO STUDENT VALUES('Vikram','DEVOPS','A',50);''')
cursor.execute('''INSERT INTO STUDENT VALUES('Mugilan','DEVOPS','A',35);''')

## display all the records
print("The inserted records are")

data=cursor.execute('''SELECT * FROM STUDENT''')

for row in data:
    print(row)
    
##close the connection

connection.commit()
connection.close()