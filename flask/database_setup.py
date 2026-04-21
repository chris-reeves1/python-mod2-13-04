import sqlite3

def setup():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY,  
        password TEXT,
        rating TEXT
        )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup()