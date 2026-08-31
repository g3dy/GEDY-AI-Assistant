import sqlite3

# Creating the database to store the application paths
connectDB = sqlite3.connect("Gedy.db")
# Adding a Cursor
cursor = connectDB.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR)"
# cursor.execute(query)

# # Now adding data to the database by inserting values
# query = "INSERT INTO sys_command VALUES (null, 'Google Chrome', 'C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe')"
# cursor.execute(query)
# connectDB.commit()
# connectDB.close()

# CREATING DATABASE FOR WEB THIRDPARTY APPLICATIONS
query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), path VARCHAR)"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null, 'My Site', 'https://www.g3dy.github.io/Cine-Vault/')"
cursor.execute(query)
connectDB.commit()
connectDB.close()