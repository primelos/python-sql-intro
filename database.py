import mysql.connector

config = {
  'user': 'root',
  'password': 'checkpass',
  'host': 'localhost',
  'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()