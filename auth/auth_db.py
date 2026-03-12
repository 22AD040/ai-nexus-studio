import sqlite3
import hashlib


def create_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()



def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



def register_user(fullname, email, password):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    hashed_password = hash_password(password)

    try:
        c.execute(
            "INSERT INTO users(fullname,email,password) VALUES(?,?,?)",
            (fullname, email, hashed_password)
        )
        conn.commit()
        conn.close()
        return True

    except sqlite3.IntegrityError:
        conn.close()
        return False



def login_user(email, password):

    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    hashed_password = hash_password(password)

    c.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, hashed_password)
    )

    data = c.fetchone()

    conn.close()

    if data:
        return True
    else:
        return False