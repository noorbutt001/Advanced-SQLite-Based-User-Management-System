import sqlite3
from sqlite3 import Error

DB_NAME = "users.db"

def create_connection():
    """Create and return a database connection."""
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Error as e:
        print(f"❌ Database connection error: {e}")
        return None


def create_tables():
    """Create the Users table if it doesn't exist."""
    conn = create_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                phone TEXT,
                role TEXT DEFAULT 'User',
                failed_attempts INTEGER DEFAULT 0,
                is_locked INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        print("✅ Database initialized successfully.")
    except Error as e:
        print(f"❌ Error creating tables: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    create_tables()