import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
