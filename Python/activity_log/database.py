import sqlite3

CREATE_ENTRY_TABLE = ("""
                      CREATE TABLE IF NOT EXISTS log
                      (
                      id  PRIMARY KEY,
                      entry_date DATE,
                      upload_date DATE,
                      owner TEXT,
                      sub_county TEXT,
                      description TEXT,
                      floors INTEGER,
                      issues TEXT,
                      assigned TEXT,
                      date_moved DATE,
                      days_left INTEGER,
                      last_follow_up DATE,
                      status TEXT,
                      remarks TEXT);
                      """)

conn = sqlite3.connect('activity_log.db')
cursor = conn.cursor()

def create_entry_table(connection):
    with connection:
        return connection.execute(CREATE_ENTRY_TABLE)
    

# create_entry_table(conn)