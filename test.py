import pymysql
conn= pymysql.connect()

cursor = conn.cursor(
    host='sql6.freesqldatabase.com',
    database='	sql6431985',
    user='sql6431985',
    password='hk9MLEKDi6',
    cursorclass=pymysql.cursors.DictCursor

)
cursor.conn.cursor()
sql_query=""" CREATE TABLE book (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
    )"""

cursor.execute(sql_query)
conn.close()