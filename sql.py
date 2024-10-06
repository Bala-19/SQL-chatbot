import sqlite3

connection=sqlite3.connect('student.db')

cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)


cursor.execute('''Insert into STUDENT values('Bala','Data Science','A',95)''')
cursor.execute('''Insert into STUDENT values('Levi','Data Science','A',66)''')
cursor.execute('''Insert into STUDENT values('Mikasa','Data Science','B',70)''')
cursor.execute('''Insert into STUDENT values('Isagi','Devops','A',90)''')
cursor.execute('''Insert into STUDENT values('Noelle','Devops','B',86)''')


print('The inserted records are:')


data=cursor.execute('''Select * from STUDENT''')

for r in data:
    print(r)

connection.commit()
connection.close()
