import sqlite3
connection = sqlite3.connect('data.db')

cursor =connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# if we want auto increment user id then we use ID as INTEGER PRIMARY KEY... thet next one will be 
# automatically incremented.
#create_table = "CREATE TABLE IF NOT EXISTS users (if int, username text, password text)"

cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

### below to lines used until leture 90
#insert_query= "INSERT INTO items VALUES (?,?)"
#cursor.execute(insert_query,('table',20.99,))

connection.commit()
connection.close()