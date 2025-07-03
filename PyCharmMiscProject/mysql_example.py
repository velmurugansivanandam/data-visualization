import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database='Customers',
        user='root',
        password='123456789'
    )

    if connection.is_connected():
        print("Conneted to MySQL datbases")
        cursor = connection.cursor()
        query="SELECT * FROM s"
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except Error as e:
    print("Error while connectnig to MySQL",e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")