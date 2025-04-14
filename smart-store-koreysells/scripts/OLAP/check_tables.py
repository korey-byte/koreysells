import sqlite3

# Connect to the database
conn = sqlite3.connect('data/dw/smart_sales.db')

# Look at the "sales" table fully
query = "SELECT * FROM sales LIMIT 1;"

cursor = conn.cursor()
cursor.execute(query)

row = cursor.fetchone()
columns = [description[0] for description in cursor.description]

print("Columns inside SALES table:")
print(columns)

conn.close()