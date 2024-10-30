
import sys
import mysql.connector
from mysql.connector import Error

# Function to create a MySQL connection
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    
    return connection

# Function to execute a single query (CREATE, UPDATE, DELETE)
def execute_query(connection, query, data=None):
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Function to execute a read query (SELECT)
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# Establishing connection
connection = create_connection("localhost", "root", "", "CRUD")

# Step 1: Create Table
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(10),
    nationality VARCHAR(50)
);
"""
execute_query(connection, create_users_table)

# Step 2: Create (Insert Data)
insert_user_query = """
INSERT INTO users (name, age, gender, nationality) VALUES (%s, %s, %s, %s)
"""
user_data = ("Alice", 30, "Female", "USA")
execute_query(connection, insert_user_query, user_data)

# Step 3: Read (Select Data)
select_users_query = "SELECT * FROM users"
users = execute_read_query(connection, select_users_query)
print("Users in the database:")
for user in users:
    print(user)

# Step 4: Update (Modify Data)
update_user_query = """
UPDATE users 
SET age = %s 
WHERE name = %s
"""
updated_data = (35, "Alice")
execute_query(connection, update_user_query, updated_data)

# Step 5: Read again to confirm update
users = execute_read_query(connection, select_users_query)
print("Users after update:")
for user in users:
    print(user)

# Step 6: Delete (Remove Data)
delete_user_query = "DELETE FROM users WHERE name = %s"
delete_user_data = ("Alice",)
execute_query(connection, delete_user_query, delete_user_data)

# Step 7: Read again to confirm deletion
users = execute_read_query(connection, select_users_query)
print("Users after deletion:")
for user in users:
    print(user)
