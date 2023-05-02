import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

cursorobject = dataBase.cursor()
cursorobject.execute('CREATE DATABASE elderco')
print('ALL DONE')