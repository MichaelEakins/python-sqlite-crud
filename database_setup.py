import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Create a table with 10 fields of varying types
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT,
            salary REAL,
            active INTEGER,
            created_at TEXT,
            updated_at TEXT,
            phone_number TEXT,
            notes BLOB
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
