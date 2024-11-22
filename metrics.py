import sqlite3

# Function to establish connection to the sqlite3 Database
def save_metrics(accuracy, f1_score):
    conn = sqlite3.connect('metrics.db')
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO metrics (accuracy, f1_score) 
                      VALUES (?, ?)''', (accuracy, f1_score))
    
    conn.commit()
    conn.close()

# Function to retrieve all metrics from the database
def get_metrics():
    conn = sqlite3.connect('metrics.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM metrics ORDER BY created_ts DESC')
    rows = cursor.fetchall()
    
    conn.close()
    
    return rows

