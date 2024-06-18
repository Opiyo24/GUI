import sqlite3

CREATE_USERS_TABLE = ("""
CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY,
                      username TEXT NOT NULL,
                      password TEXT NOT NULL);
""")

QUERRY_USER = ("""
SELECT * FROM users WHERE username = ?;
""")

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

ENTRIES = ("""
    SELECT * FROM log;
""")

CREATE_DEV_TYPE_TABLE = ("""
CREATE TABLE IF NOT EXISTS others_dev_type (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
);
""")

CREATE_STATUS_TABLE = ("""
CREATE TABLE IF NOT EXISTS others_status (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
);
""")

CREATE_MEMBERS_TABLE = ("""
CREATE TABLE IF NOT EXISTS others_members (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
);
""")

CREATE_SUB_COUNTY_TABLE = ("""
CREATE TABLE IF NOT EXISTS others_sub_county (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
);
""")

CREATE_DEV_TABLE = ("""
CREATE TABLE IF NOT EXISTS others_dev (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
);
""")

conn = sqlite3.connect('activity_log.db')
cursor = conn.cursor()

def create_entry_table(connection):
    with connection:
        return connection.execute(CREATE_ENTRY_TABLE)
    
def make_entry(data):

    try:
        conn = sqlite3.connect('activity_log.db')
        cursor = conn.cursor()

        sql = '''INSERT INTO log (id,entry_date,upload_date,owner,sub_county,description,floors,issues,assigned,date_moved,days_left,last_follow_up,status,remarks) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        with conn:
            cursor.execute(sql, data)
            conn.commit()
        
        conn.close()
        print('Entry made successfully')
        return True
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
    
def pull_user(connection, username):
    try:
        with connection:
            user =  connection.execute(QUERRY_USER, (username,)).fetchone()
            if user:
                return user
            else:
                return None
    except:
        return f'User {username} not found'
    
def create_dev_type_table(connection):
    with connection:
        return connection.execute(CREATE_DEV_TYPE_TABLE)
    
def create_status_table(connection):
    with connection:
        return connection.execute(CREATE_STATUS_TABLE)
    
def create_members_table(connection):
    with connection:
        return connection.execute(CREATE_MEMBERS_TABLE)
    
def create_sub_county_table(connection):
    with connection:
        return connection.execute(CREATE_SUB_COUNTY_TABLE)
    
def create_dev_table(connection):
    with connection:
        return connection.execute(CREATE_DEV_TABLE)
    
def create_users_table(connection):
    with connection:
        return connection.execute(CREATE_USERS_TABLE)


    

# create_entry_table(conn)
# create_entry_table(conn)
# create_dev_type_table(conn)
# create_status_table(conn)
# create_members_table(conn)
# create_sub_county_table(conn)
# create_dev_table(conn)
# create_users_table(conn)

conn.close()