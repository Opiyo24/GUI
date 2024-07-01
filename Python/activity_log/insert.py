import sqlite3


# Connect to the database

conn = sqlite3.connect('activity_log.db')

c = conn.cursor()

c.execute("DROP TABLE IF EXISTS table_name;")

c.execute("""
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
            remarks TEXT);
            """)


# Create a new record

values = [('cc', '2024-11-20', '2024-11-20', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'YYY/LV', 'JENNY', '2024-12-20', 22, 'P/450/2016', 'APPROVED', 'SORTED', 'SORTED'),
('649dba81-14c7-511d-b328-b89899adc995', '2024-08-15', '2024-08-15', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'ZZZ/LV', 'VANESSA', '2024-09-15', 25, 'P/500/2015', 'REJECTED', 'SORTED', 'SORTED'),
('723b0a78-7702-53e9-9502-bb7893e2508d', '2024-04-10', '2024-04-10', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'XXX/LV', 'JENNY', '2024-05-10', 18, 'P/550/2024', 'APPROVED', 'SORTED', 'SORTED'),
('b4eb4f9c-2f00-551d-843b-4039aed65b2f', '2024-10-20', '2024-10-20', 'Fatma Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT2', 'YYY/LV', 'VANESSA', '2024-11-20', 12, 'P/600/2014', 'REJECTED', 'SORTED', 'SORTED'),
('43c0896b-7357-576f-a16d-c091903680f4', '2024-03-01', '2024-03-01', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'ZZZ/LV', 'JENNY', '2024-04-01', 28, 'P/650/2013', 'APPROVED', 'SORTED', 'SORTED'),
('cb725ae0-8e8d-5fe1-9faf-684c7956a812', '2024-05-20', '2024-05-20', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'XXX/LV', 'VANESSA', '2024-06-20', 20, 'P/700/2012', 'REJECTED', 'SORTED', 'SORTED'),
('135c2e8b-5f0e-5ced-b7fb-e5e9962b8d3e', '2024-01-10', '2024-01-10', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'YYY/LV', 'JENNY', '2024-02-10', 25, 'P/750/2011', 'APPROVED', 'SORTED', 'SORTED'),
('4a3d2c1b-0e9f-8d7c-6b5a-3f2e1c', '2024-02-15', '2024-02-15', 'Fatma Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT2', 'ZZZ/LV', 'VANESSA', '2024-03-15', 27, 'P/800/2024', 'REJECTED', 'SORTED', 'SORTED'),
('f2807aa7-71ee-5028-ad9c-e3e73a605593', '2024-07-05', '2024-07-05', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'XXX/LV', 'JENNY', '2024-08-05', 23, 'P/850/2016', 'APPROVED', 'SORTED', 'SORTED'),
('ae319c1a-d6f8-52ab-b7f0-717d82021291', '2024-09-10', '2024-09-10', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'YYY/LV', 'VANESSA', '2024-10-10', 24, 'P/900/2015', 'REJECTED', 'SORTED', 'SORTED'),
('5eea1d0f-5773-58ef-a50e-5d97abd76153', '2024-11-25', '2024-11-25', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'ZZZ/LV', 'JENNY', '2024-12-25', 20, 'P/950/2024', 'APPROVED', 'SORTED', 'SORTED'),
('f50320fc-eddf-5f09-a43f-2515371877b0', '2024-04-15', '2024-04-15', 'Fatma Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT2', 'XXX/LV', 'VANESSA', '2024-05-15', 19, 'P/1000/2014', 'REJECTED', 'SORTED', 'SORTED'),
('9cb99c5d-2203-537d-b0a3-e817428a2a7e', '2024-05-10', '2024-05-10', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'YYY/LV', 'JENNY', '2024-06-10', 26, 'P/1050/2013', 'APPROVED', 'SORTED', 'SORTED'),
('f5656f45-47e7-5737-9665-2f194fc33450', '2024-01-25', '2024-01-25', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'ZZZ/LV', 'VANESSA', '2024-02-25', 28, 'P/1100/2012', 'REJECTED', 'SORTED', 'SORTED'),
('d6254933-f642-5097-9ad1-6b4d5809c7af', '2024-07-20', '2024-07-20', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'XXX/LV', 'JENNY', '2024-08-20', 22, 'P/1150/2011', 'APPROVED', 'SORTED', 'SORTED'),
('fc3da1ee-843d-546d-8e61-2d79074ad328', '2024-08-25', '2024-08-25', 'Fatma Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT2', 'YYY/LV', 'VANESSA', '2024-09-25', 21, 'P/1200/2024', 'REJECTED', 'SORTED', 'SORTED'),
('c7e46cd6-ebdb-5a19-977a-6cfdf50b50cc', '2024-09-15', '2024-09-15', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'ZZZ/LV', 'JENNY', '2024-10-15', 27, 'P/1250/2016', 'APPROVED', 'SORTED', 'SORTED'),
('254aec0b-e5ec-5ef1-a917-9b7265b615cf', '2024-10-30', '2024-10-30', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'XXX/LV', 'VANESSA', '2024-11-30', 25, 'P/1300/2015', 'REJECTED', 'SORTED', 'SORTED'),
('c3b55100-c0dd-55e6-b3da-10a2fd0cfcad', '2024-02-20', '2024-02-20', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'YYY/LV', 'JENNY', '2024-03-20', 18, 'P/1350/2024', 'APPROVED', 'SORTED', 'SORTED'),
('bf716057-018d-5478-b9cd-d06b976c3696', '2024-05-25', '2024-05-25', 'Fatma Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT2', 'ZZZ/LV', 'VANESSA', '2024-06-25', 23, 'P/1400/2014', 'REJECTED', 'SORTED', 'SORTED'),
('62ca6efd-c51f-5780-96f8-7969ce6afbbd', '2024-11-10', '2024-11-10', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'XXX/LV', 'JENNY', '2024-12-10', 22, 'P/1450/2013', 'APPROVED', 'SORTED', 'SORTED'),
('38c9c0f1-eb75-5d84-bbe0-d8927b00e588', '2024-03-20', '2024-03-20', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'YYY/LV', 'VANESSA', '2024-04-20', 27, 'P/1500/2012', 'REJECTED', 'SORTED', 'SORTED'),
('f0d98610-ed00-5b08-96a1-f8b1a602abb2', '2024-06-10', '2024-06-10', 'Aisha Juma Ali', 'KILIMANI', 'COMMERCIAL', 'GROUND FLOOR', 'ZZZ/LV', 'JENNY', '2024-07-10', 28, 'P/1550/2011', 'APPROVED', 'SORTED', 'SORTED'),
('e726de65-733f-5c02-b3a1-8b7517a5ef4c', '2024-08-05', '2024-08-05', 'Fatma Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT2', 'XXX/LV', 'VANESSA', '2024-09-05', 19, 'P/1600/2024', 'REJECTED', 'SORTED', 'SORTED'),
('6773180a-5c96-5317-9a31-e10bf3addec0', '2024-01-15', '2024-01-15', 'Juma Ali Kithuri', 'KILIMANI', 'COMMERCIAL', 'FIRST FLOOR', 'YYY/LV', 'JENNY', '2024-02-15', 24, 'P/1650/2016', 'APPROVED', 'SORTED', 'SORTED'),
('99a711d8-bd34-5887-8cf5-98fec41c63df', '2024-03-25', '2024-03-25', 'Venessa Ali Hassan', 'NYALI', 'RESIDENTIAL', 'BASEMENT1', 'ZZZ/LV', 'VANESSA', '2024-04-25', 21, 'P/1700/2015', 'REJECTED', 'SORTED', 'SORTED')]



c.executemany("INSERT INTO log (id, entry_date, upload_date, owner, sub_county, description, floors, plot_no, assigned, date_moved, days_left, ref_no, status, issues, remarks) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", values)


conn.commit()


# Close the connection

conn.close()