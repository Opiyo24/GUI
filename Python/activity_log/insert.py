import sqlite3


# Connect to the database

conn = sqlite3.connect('activity_log.db')

c = conn.cursor()


# Create a new record

values = [('9f8a3f6e-5c9b-49c2-8f5d-43f6a5c7d809', '2024-05-15', '2024-05-15', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'YYY/LV', 'JENNY', '2024-06-01', 25, 'P/200/2020', 'APPROVED', 'SORTED', 'SORTED'),('4c2a1d6f-8e9a-4a4e-8c58-9374745bdc06', '2024-03-20', '2024-03-20', 'Fatma Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT2', 'ZZZ/LV', 'VANESSA', '2024-04-10', 12, 'P/150/2018', 'REJECTED', 'SORTED', 'SORTED'),('1a2b3c4f-5d6e-7f8g-9h0j-1k2l3m4n5o6', '2024-01-05', '2024-01-05', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'XXX/LV', 'JENNY', '2024-02-01', 30, 'P/250/2021', 'APPROVED', 'SORTED', 'SORTED'),('8f7e6d5c-4b3a-2c1d-0f9e-8d7c6b5a4', '2024-09-10', '2024-09-10', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'YYY/LV', 'VANESSA', '2024-10-05', 20, 'P/300/2022', 'REJECTED', 'SORTED', 'SORTED'),('3d2c1b0a-9f8e-7d6c-5b4a-3f2e1d0c', '2024-11-15', '2024-11-15', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'ZZZ/LV', 'JENNY', '2024-12-01', 28, 'P/350/2023', 'APPROVED', 'SORTED', 'SORTED'),('6f5e4d3c-2b1a-9f8e-7d6c-5b4a-3f2e1d0c', '2024-02-20', '2024-02-20', 'Fatma Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT2', 'XXX/LV', 'VANESSA', '2024-03-10', 15, 'P/400/2017', 'REJECTED', 'SORTED', 'SORTED'),('9c8b7a6f-5d4e-3f2g-1h0j-2k3l4m5n6', '2024-06-01', '2024-06-01', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'YYY/LV', 'JENNY', '2024-07-01', 22, 'P/450/2016', 'APPROVED', 'SORTED', 'SORTED'),('4b3a2c1d-0f9e-8d7c-6b5a-4f3e2d1c', '2024-08-15', '2024-08-15', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'ZZZ/LV', 'VANESSA', '2024-09-05', 25, 'P/500/2015', 'REJECTED', 'SORTED', 'SORTED'),('1f2e3d4c-5b4a-3f2e-1d0c-9f8e-7d6c', '2024-04-10', '2024-04-10', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'XXX/LV', 'JENNY', '2024-05-01', 18, 'P/550/2024', 'APPROVED', 'SORTED', 'SORTED'),('8d7c6b5a-4f3e-2d1c-9f8e-7d6c-5b4a', '2024-10-20', '2024-10-20', 'Fatma Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT2', 'YYY/LV', 'VANESSA', '2024-11-10', 12, 'P/600/2014', 'REJECTED', 'SORTED', 'SORTED'),('3f2e1d0c-9f8e-7d6c-5b4a-3f2e-1d0c', '2024-03-01', '2024-03-01', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'ZZZ/LV', 'JENNY', '2024-04-01', 28, 'P/650/2013', 'APPROVED', 'SORTED', 'SORTED'),('6b5a4f3e-2d1c-9f8e-7d6c-5b4a-3f2e', '2024-05-20', '2024-05-20', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'XXX/LV', 'VANESSA', '2024-06-10', 20, 'P/700/2012', 'REJECTED', 'SORTED', 'SORTED'),('9f8e7d6c-5b4a-3f2e-1d0c-9f8e-7d6c', '2024-01-10', '2024-01-10', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'YYY/LV', 'JENNY', '2024-02-10', 25, 'P/750/2011', 'APPROVED', 'SORTED', 'SORTED'),('4f3e2d1c-9f8e-7d6c-5b4a-3f2e-1d0c', '2024-07-20', '2024-07-20', 'Fatma Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT2', 'ZZZ/LV', 'VANESSA', '2024-08-10', 15, 'P/800/2010', 'REJECTED', 'SORTED', 'SORTED'),('1d0c9f8e-7d6c-5b4a-3f2e-1d0c-9f8e', '2024-09-01', '2024-09-01', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'XXX/LV', 'JENNY', '2024-10-01', 22, 'P/850/2009', 'APPROVED', 'SORTED', 'SORTED'),('8e9f8a6f-5d4e-3f2g-1h0j-2k3l4m5n6', '2024-11-01', '2024-11-01', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'YYY/LV', 'VANESSA', '2024-12-01', 28, 'P/900/2008', 'REJECTED', 'SORTED', 'SORTED'),('3c2b1a9f-8e9a-4a4e-8c58-9374745bdc06', '2024-02-01', '2024-02-01', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'ZZZ/LV', 'JENNY', '2024-03-01', 18, 'P/950/2007', 'APPROVED', 'SORTED', 'SORTED')]


c.executemany("INSERT INTO log (id, entry_date, upload_date, owner, sub_county, description, floors, plot_no, assigned, date_moved, days_left, ref_no, status, issues, remarks) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", values)


# Commit the changes

conn.commit()


# Close the connection

conn.close()