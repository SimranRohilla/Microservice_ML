import sqlite3

def init_db():
    # Connect to the SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect('metrics.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        accuracy REAL,
        f1_score REAL,
        created_ts DATETIME DEFAULT CURRENT_TIMESTAMP,
        modified_ts DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully!")



