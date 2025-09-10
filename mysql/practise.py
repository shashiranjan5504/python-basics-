import mysql.connector


conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",#write the password and execute 
        database="family",
        
    )
mycursor=conn.cursor()
mycursor.execute ("select * from members")
result=mycursor.fetchone()
for i in result:
    print(i)

    