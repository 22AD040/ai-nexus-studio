import sqlite3
import bcrypt

DB_PATH = "database/users.db"


def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def register_user(fullname, email, password):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        cursor.execute(
            "INSERT INTO users (fullname,email,password) VALUES (?,?,?)",
            (fullname, email, hashed)
        )

        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()


def login_user(email, password):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE email=?",
        (email,)
    )

    data = cursor.fetchone()
    conn.close()

    if data:
        if bcrypt.checkpw(password.encode(), data[0]):
            return True

    return False