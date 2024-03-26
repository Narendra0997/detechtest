pip install pyodbc

import pyodbc

# Establish a connection to the SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=NP;DATABASE=GroupM;;Trusted_Connection=yes;')

cursor = conn.cursor()

# SQL command to create a table for posts
create_table_posts = '''
CREATE TABLE dbo.Posts (
    userId INT PRIMARY KEY,
    id INT,
    title NVARCHAR(1000),
    body NVARCHAR(MAX),
    status NVARCHAR(50),
    loaddate DATETIME
)
'''


# SQL command to create a table for users
create_table_users = '''
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    Username NVARCHAR(50),
    Email NVARCHAR(255),
    CreatedDate DATETIME
)
'''

cursor.execute(create_table_posts)
cursor.execute(create_table_users)
