import sqlite3

connection = sqlite3.connect("aircraft.db")

print("Database created successfully!")

connection.close()