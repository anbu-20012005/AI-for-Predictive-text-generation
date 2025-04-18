import sqlite3

def init_db():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_text TEXT,
            prediction TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_prediction(input_text, prediction):
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('INSERT INTO predictions (input_text, prediction) VALUES (?, ?)', (input_text, prediction))
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('SELECT input_text, prediction, timestamp FROM predictions ORDER BY timestamp DESC')
    history = [{'input': row[0], 'prediction': row[1], 'timestamp': row[2]} for row in c.fetchall()]
    conn.close()
    return history