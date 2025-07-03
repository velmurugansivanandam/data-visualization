import pandas as pd
import mysql.connector

# Load CSV
df = pd.read_csv(r"C:\Users\HP\Documents\student_exam_data.csv")


# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="sys"
)
cursor = conn.cursor()

# Optional: Truncate table to avoid duplicates
cursor.execute("TRUNCATE TABLE student_exam_data")

# Insert each row into the MySQL table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO student_exam_data 
        (student_id, name, email, course_id, course_name, grade, attendance)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()

# Query and print the data
cursor.execute("SELECT * FROM student_exam_data")
results = cursor.fetchall()

print("📋 Student Exam Data:")
for record in results:
    print(record)

# Close connection
cursor.close()
conn.close()
