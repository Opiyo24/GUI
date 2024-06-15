import sqlite3

def create_table():
    conn = sqlite3.connect('Messages.db')
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS messages (
                   message_id INTEGER PRIMARY KEY, message_content TEXT )''')
    
    conn.commit()
    conn.close()


def insert_message(message):
    conn = sqlite3.connect('Messages.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO messages (message_content) VALUES (?)', (message,))
    conn.commit()
    conn.close()


create_table()