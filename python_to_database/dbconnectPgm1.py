# step1 import msql.connector
import mysql.connector

# step2: establish mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password'
)

# step3: create a cursor object(it is used to export and inmport data from python to sql and vice versa)

cursor=db.cursor()
sql='select version()'
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()