import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")

cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS userdata(
     id INTERGER PRIMARY KEY ,
     username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
    )
    
""")
username1, password1 = "kevin123", hashlib.sha256("kevinpassword".encode()).hexdigest()
username2, password2 = "kevin1", hashlib.sha256("spurs567".encode()).hexdigest()
username3, password3 = "k123", hashlib.sha256("gateru76".encode()).hexdigest()
username4, password4 = "kevoh5", hashlib.sha256("banter345".encode()).hexdigest()


cur.execute("INSERT INTO userdata(username, password)VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata(username, password)VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata(username, password)VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata(username, password)VALUES (?, ?)", (username4, password4))

conn.commit()