import mysql.connector


dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Archit@26",
)

#cursorObject

cursorObject=dataBase.cursor()

#create db

cursorObject.execute('CREATE DATABASE Blog_Post')
print('All done!')