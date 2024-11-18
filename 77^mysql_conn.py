import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="1234", 
    database="cse2A"
)

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS student2 (name VARCHAR(20), age INT)")

cursor.execute("INSERT INTO student2 (name, age) VALUES ('aditya', 24)")

db.commit()

cursor.execute("SELECT * FROM student2")

result = cursor.fetchall()

print(result)

cursor.close()
db.close()

# Expected Output:
# [('aditya', 24)]
