#!/usr/bin/env python3
"""
created: 2022-08-29 15:14:31
@author: seraph★776
contact: seraph776@gmail.com
project: SQL Injection Attack - Hacker Challenge
license: MIT
"""


import sqlite3
import requests

# SQL statements:
CREATE_USERS_TABLE = "CREATE TABLE IF NOT EXISTS usernames (id INTEGER PRIMARY KEY, username TEXT, password TEXT);"
INSERT_USER_DATA = "INSERT INTO usernames (username, password) VALUES (?, ?)"


def get_userdata() -> list:
    """Returns username, and password in tuple from online username.dat file."""
    # url to username and password file
    URL = "https://pastebin.com/raw/ih7szSSv"
    raw = [i.strip() for i in requests.get(URL).text.split('\n')]
    output = []
    for i in raw:
        users = i.split(', ')[0].split(',')[0]
        passwords = i.split(', ')[0].split(',')[1]
        output.append((users, passwords))
    return output


# Create database in memory
conn = sqlite3.connect(":memory:")
# Get usernames and passwords
user_data = get_userdata()

# Create table
conn.execute(CREATE_USERS_TABLE)
# Insert username, passwords into database
conn.executemany(INSERT_USER_DATA, user_data)


while True:
    INJECTION = input("Enter your SQL Injection:\n>  ")
    sql = f"SELECT * FROM usernames WHERE id = 776 {INJECTION}"
    try:
        results = conn.execute(sql).fetchall()
        if results:
            print(f"\n\033[92m" + "Good job, you did it!" + "\033[0m")
            with conn:
                for row in results:
                    print(row)
            conn.close()
    except sqlite3.OperationalError as e:
        print("\n\033[91m" + "Nope, try again!" + "\033[0m")
        pass
