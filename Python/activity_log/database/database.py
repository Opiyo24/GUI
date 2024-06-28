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
                      plot_no TEXT,
                      assigned TEXT,
                      date_moved DATE,
                      days_left INTEGER,
                      ref_no TEXT,
                      status TEXT,
                      issues TEXT);
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
    
create_entry_table(conn)
    
def make_entry(data):

    try:
        conn = sqlite3.connect('activity_log.db')
        cursor = conn.cursor()

        sql = '''INSERT INTO log (id,entry_date,upload_date,owner,sub_county,description,floors,plot_no,assigned,date_moved,days_left,ref_no,status,issues) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

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
    
def pull_entries():
    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(ENTRIES).fetchall()

def determine(value):
    if value == "Entry Date":
        value = "entry_date"
    elif value == "Upload Date":
        value = "upload_date"
    elif value == "Owner":
        value = "owner"
    elif value == "Sub-County":
        value = "sub_county"
    elif value == "Description":
        value = "description"
    elif value == "Floors":
        value = "floors"
    elif value == "Plot No":
        value = "plot_no"
    elif value == "Assigned":
        value = "assigned"
    elif value == "Date Moved":
        value = "date_moved"
    elif value == "Days Left":
        value = "days_left"
    elif value == "Ref No":
        value = "ref_no"
    elif value == "Status":
        value = "status"
    elif value == "Issues":
        value = "issues"
    else:
        value = "entry_date"
    return value

# print(pull_entries())
def table_sort(value):
    value = determine(value)
    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(f'SELECT * FROM log ORDER BY "{value}"')
    

def criteria_values(value):
    value = determine(value)
    connection = sqlite3.connect('activity_log.db')
    with connection:
        abraba = connection.execute(f'SELECT DISTINCT {value} FROM log').fetchall()
        col_list = []
        for row in abraba:
            col_list.append(row[0])
        return col_list
    
def filter_entries(value1, value2):
    value1 = determine(value1)
    value2 = determine(value2)
    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(f'SELECT * FROM log WHERE "{value1}" = "{value2}"')
    
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
if __name__ == '__main__':
    criteria_values('Description')
    # print(pull_user(conn, 'james'))
    # print(pull_entries())
    # print(table_sort('Entry Date'))
    # print(filter_entries('Entry Date