import mysql.connector

# Database connection parameters
db_config = {
    'user': 'root',
    'password': 'admin',
    'host': 'vamshisql',
    'database': 'vamshidb',  # Updated with the correct database name
}

try:
    # Establishing a connection to the MySQL server
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to MySQL database")

        # Creating a cursor object to interact with the database
        cursor = connection.cursor()

        # Fetching and displaying data from the STUDENTS table
        cursor.execute("SELECT * FROM STUDENTS")
        rows = cursor.fetchall()

        print("\nStudent Data:")
        for row in rows:
            print("Student ID:", row[0])
            print("Name:", row[1])
            print("Age:", row[2])
            print("Grade:", row[3])
            print("-------------")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Closing the database connection and cursor
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("\nConnection to MySQL database closed")
