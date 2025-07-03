import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='employees',
        user='root',
        password='123456789'
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    cursor = connection.cursor()

    table_name = input("Enter the table name: ")
    columns = input("Enter the column names separated by comma (e.g., student_id, student_name): ")

    query = f"SELECT {columns} FROM {table_name}"
    print("Query:", query)

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
