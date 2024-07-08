import sqlite3

from utils.date_picker import *

date_str = todays_date()
date = datetime.strptime(date_str, '%a %d %b %Y')

# Now you can use strftime on the datetime object
month = date.strftime('%m')
year = date.strftime('%Y')

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
                      issues TEXT,
                      remarks TEXT,
                      month TEXT GENERATED ALWAYS AS (strftime('%m', entry_date)),
                      year TEXT GENERATED ALWAYS AS (strftime('%Y', entry_date)));
                      """)

NEW_COLUMN_MONTH = ("""ALTER TABLE log ADD COLUMN month TEXT GENERATED ALWAYS AS (strftime('%m', date));""")

ENTRIES = ("""
    SELECT * FROM log WHERE month = ? AND year = ? ORDER BY entry_date ASC;
""")

CREATE_DESCRIPTION_TABLE = ("""
CREATE TABLE IF NOT EXISTS description (
                        name TEXT NOT NULL
);
""")

CREATE_STATUS_TABLE = ("""
CREATE TABLE IF NOT EXISTS status (
                        name TEXT NOT NULL
);
""")

CREATE_ASSIGNED_TABLE = ("""
CREATE TABLE IF NOT EXISTS assigned (
                        name TEXT NOT NULL
);
""")

CREATE_SUB_COUNTY_TABLE = ("""
CREATE TABLE IF NOT EXISTS sub_county (
                        name TEXT NOT NULL
);
""")

CREATE_FLOORS_TABLE = ("""
CREATE TABLE IF NOT EXISTS floors (
                        name TEXT NOT NULL
);
""")

conn = sqlite3.connect('activity_log.db')
cursor = conn.cursor()

def create_entry_table():
    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(CREATE_ENTRY_TABLE)

def add_month_year_columns():
    connection = sqlite3.connect('activity_log.db')
    cursor = connection.cursor()

    # Check if the month column exists
    cursor.execute("PRAGMA table_info(log)")
    columns = [column_info[1] for column_info in cursor.fetchall()]
    
    # if 'month' not in columns:
    #     # Add the month column
    #     cursor.execute("ALTER TABLE log ADD COLUMN month TEXT GENERATED ALWAYS AS (strftime('%m', entry_date))")

    # # Check if the year column exists
    # if 'year' not in columns:
    #     # Add the year column
    #     cursor.execute("ALTER TABLE log ADD COLUMN year TEXT GENERATED ALWAYS AS (strftime('%Y', entry_date))")

    if 'upload_year' not in columns:
        # Add the year column
        cursor.execute("ALTER TABLE log ADD COLUMN upload_year TEXT GENERATED ALWAYS AS (strftime('%Y', upload_date))")

    connection.commit()
    connection.close()
    
# create_entry_table(conn)
    
def make_entry(data):

    try:
        conn = sqlite3.connect('activity_log.db')
        cursor = conn.cursor()

        sql = '''INSERT INTO log (id,entry_date,upload_date,owner,sub_county,description,floors,plot_no,assigned,date_moved,days_left,ref_no,status,issues,remarks) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

        with conn:
            cursor.execute(sql, data)
            conn.commit()
        
        conn.close()
        print('Entry logged successfully')
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
    global month, year

    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(ENTRIES, (month, year)).fetchall()
    
def delete_entry(pk):
    connection = sqlite3.connect('activity_log.db')
    with connection:
        connection.execute(f'DELETE FROM log WHERE id = "{pk}"')
        print("Entry deleted successfully")

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
        return connection.execute(f'SELECT * FROM log WHERE month = "{month}" and year = "{year}" ORDER BY "{value}"')
    

def criteria_values(value):
    value = determine(value)
    connection = sqlite3.connect('activity_log.db')
    with connection:
        abraba = connection.execute(f'SELECT DISTINCT {value} FROM log where month = "{month}" and year = "{year}"').fetchall()
        col_list = []
        for row in abraba:
            col_list.append(row[0])
        return col_list
    
def filter_entries(value1, value2):
    value1 = determine(value1)
    # value2 = determine(value2)
    connection = sqlite3.connect('activity_log.db')
    with connection:
        print("Column name:", value1)
        print("Value:", value2)
        cursor = connection.cursor()
        query = f"SELECT * FROM log WHERE {value1} = ? AND month = ? AND year = ? ORDER BY entry_date ASC"
        cursor.execute(query, (value2, month, year))
        rows = cursor.fetchall()
        cursor.close()
        
        print("Printing from database script")
        print(rows)
        
    return rows
    
def create_floors_table():
    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(CREATE_FLOORS_TABLE)
    
def create_status_table():
    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(CREATE_STATUS_TABLE)
    
def create_assigned_table():
    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(CREATE_ASSIGNED_TABLE)
    
def create_sub_county_table():
    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(CREATE_SUB_COUNTY_TABLE)
    
def create_description_table():
    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(CREATE_DESCRIPTION_TABLE)
    
def create_users_table():
    connection = sqlite3.connect('activity_log.db')
    with connection:
        return connection.execute(CREATE_USERS_TABLE)
    
def make_entry2(table_widget, widget, data, table):
    widget.delete(0, 'end')
    connection = sqlite3.connect('activity_log.db')
    try:
        with connection:
            connection.execute(f'INSERT INTO {table} VALUES (?)', (data,))
            connection.commit()
            print(f"{table} entry made successfully")
            for row in table_widget.get_children():
                table_widget.delete(row)

            values = pull_entries2(table)
            print(values)
            
            for value in values:
                table_widget.insert("", "end", values = value)
            return True
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False
    
def pull_entries2(table):
    connection = sqlite3.connect('activity_log.db')
    try:
        with connection:
            entries = connection.execute(f'SELECT * FROM {table}').fetchall()
            print("Printing entries.")
            print(entries)
            return entries
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False

def entries_list(table):
    entries = pull_entries2(table)
    entries_list = ['']
    for entry in entries:
        entries_list.append(entry[0])
    print("Printig entries list")
    print(entries_list)
    return entries_list

def delete_table(table_name):
    connection = sqlite3.connect('activity_log.db')
    try:
        with connection:
            connection.execute(f'DROP TABLE IF EXISTS {table_name}')
            connection.commit()
            print(f"Table {table_name} deleted successfully")
            return True

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return False

def del_cols():
    delete_table('description')
    delete_table('status')
    delete_table('assigned')
    delete_table('sub_county')
    delete_table('floors')

def create_all_tables():
    create_entry_table()
    create_floors_table()
    create_status_table()
    create_assigned_table()
    create_sub_county_table()
    create_description_table()
    create_users_table()
    # add_month_year_columns()
    


    

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
    # criteria_values('Description')
    # print(pull_user(conn, 'james'))
    # print(pull_entries())
    # print(table_sort('Entry Date'))
    # print(filter_entries('Entry Date
    # date_parameters()
    # delete_table('description')
    # delete_table('status')
    # delete_table('assigned')
    # delete_table('sub_county')
    # delete_table('floors')
    pass