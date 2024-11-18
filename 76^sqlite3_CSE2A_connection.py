import sqlite3  # Corrected module name from 'sqlit3' to 'sqlite3'

# Creating a database connection
con = sqlite3.connect('CSE2A.db')  # Corrected database name to 'CSE2A.db'

# Creating the table 'student1'
con.execute("""
CREATE TABLE IF NOT EXISTS student1 (
    name TEXT,
    age INTEGER,
    roll INTEGER,
    grade REAL
)
""")  # Fixed SQL syntax and consistent table name

# Clearing the existing data before insertion
con.execute("DELETE FROM student1")

# Inserting records into the 'student1' table (This will now be done only once)
con.execute("INSERT INTO student1 VALUES ('A', 18, 1, 9.0)")
con.execute("INSERT INTO student1 VALUES ('B', 19, 2, 9.0)")
con.execute("INSERT INTO student1 VALUES ('C', 22, 3, 9.0)")
con.execute("INSERT INTO student1 VALUES ('D', 21, 4, 9.0)")
con.execute("INSERT INTO student1 VALUES ('E', 20, 5, 8.5)")  # Added missing records
con.execute("INSERT INTO student1 VALUES ('F', 23, 6, 8.0)")  # Added missing records

# Committing the changes
con.commit()

# Fetching and displaying all records from the 'student1' table
result = con.execute('SELECT * FROM student1')
for i in result:
    print(i)

# Closing the database connection
con.close()

# Output:
# ('A', 18, 1, 9.0)
# ('B', 19, 2, 9.0)
# ('C', 22, 3, 9.0)
# ('D', 21, 4, 9.0)
# ('E', 20, 5, 8.5)
# ('F', 23, 6, 8.0)
