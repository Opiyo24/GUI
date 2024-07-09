import sqlite3
import math

# List of months in database - entry date
def entry_months():
    """
    Returns a list of months in the database
    """
    options = (
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    )
    connection = sqlite3.connect('activity_log.db')
    
    with connection:
        cursor = connection.cursor()
        months = cursor.execute("SELECT DISTINCT month FROM log").fetchall()
    
    indices = [int(month[0].lstrip('0')) for month in months]
    
    sorted_indices = sorted(indices)
    
    MONTHS = [options[index-1] for index in sorted_indices]
    # print("Printing MONTHS")
    # print(MONTHS)
    return MONTHS

# List of years in database - entry date
def entry_years():
    """
    Returns a list of years in the database
    """
    connection = sqlite3.connect('activity_log.db')
    
    with connection:
        cursor = connection.cursor()
        years = cursor.execute("SELECT DISTINCT year FROM log").fetchall()
    
    YEARS = [year[0] for year in years]
    #No comma, not sure whether is a list
    # print("Printing YEARS")
    # print(YEARS)
    return YEARS

def check_months(month:str) -> str:
    if month == 'January' or month == 'JANUARY' or month == 'january' or month == '01':
        return '01'
    elif month == 'February' or month == 'FEBRUARY' or month == 'february' or month == '02':
        return '02'
    elif month == 'March' or month == 'MARCH' or month == 'march' or month == '03':
        return '03'
    elif month == 'April' or month == 'APRIL' or month == 'april' or month == '04':
        return '04'
    elif month == 'May' or month == 'MAY' or month == 'may' or month == '05':
        return '05'
    elif month == 'June' or month == 'JUNE' or month == 'june' or month == '06':
        return '06'
    elif month == 'July' or month == 'JULY' or month == 'july' or month == '07':
        return '07'
    elif month == 'August' or month == 'AUGUST' or month == 'august' or month == '08':
        return '08'
    elif month == 'September' or month == 'SEPTEMBER' or month == 'september' or month == '09':
        return '09'
    elif month == 'October' or month == 'OCTOBER' or month == 'october' or month == '10':
        return '10'
    elif month == 'November' or month == 'NOVEMBER' or month == 'november' or month == '11':
        return '11'
    elif month == 'December' or month == 'DECEMBER' or month == 'december' or month == '12':
        return '12'
    else:
        return 'Invalid month'

def check_sub_county(sub_county:str) -> str:
    #sub_counties = ['CHANGAMWE', 'JOMVU', 'KISAUNI', 'LIKONI', 'NYALI', 'MVITA']
    if sub_county == 'CHANGAMWE' or sub_county == 'Changamwe' or sub_county == 'changamwe':
        return 'CHANGAMWE'
    elif sub_county == 'JOMVU' or sub_county == 'Jomvu' or sub_county == 'jomvu':
        return 'JOMVU'
    elif sub_county == 'KISAUNI' or sub_county == 'Kisauni' or sub_county == 'kisauni':
        return 'KISAUNI'
    elif sub_county == 'LIKONI' or sub_county == 'Likoni' or sub_county == 'likoni':
        return 'LIKONI'
    elif sub_county == 'NYALI' or sub_county == 'Nyali' or sub_county == 'nyali':
        return 'NYALI'
    elif sub_county == 'MVITA' or sub_county == 'Mvita' or sub_county == 'mvita':
        return 'MVITA'
    else:
        return 'Invalid sub-county'

def check_years(year) -> str:
    if year in ['2019', 2019]:
        return '2019'
    elif year in ['2020', 2020]:
        return '2020'
    elif year in ['2021', 2021]:
        return '2021'
    elif year in ['2022', 2022]:
        return '2022'
    elif year in ['2023', 2023]:
        return '2023'
    elif year in ['2024', 2024]:
        return '2024'
    elif year in ['2025', 2025]:
        return '2025'
# Total number of entries within selected month
def number_of_entries(month:str, year:str) -> int:
    """
    Returns the number of entries in the corresponding month
    """
    month = check_months(month)
    year = check_years(year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        months = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ?", (month,year)).fetchone()

    # print("Printing months")
    # print(months)
    number = int(months[0])

    # print("Printing number")
    # print(number)
    return number

# Total number of approved entries within selected month
def number_of_approved_entries(month:str, year:str) -> int:
    """
    Returns the number of approved entries in the corresponding month
    """
    month = check_months(month)
    year = check_years(year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        months = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND status = 'APPROVED'", (month, year)).fetchone()

    number = int(months[0])
    return number

# Total number of pending entries within selected month
def number_of_pending_entries(month:str, year:str) -> int:
    """
    Returns the number of pending entries in the corresponding month
    """
    month = check_months(month)
    year = check_years(year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        months = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ?AND status = 'PENDING'", (month, year)).fetchone()

    number = int(months[0])
    return number

# Total number of rejected entries within selected month
def number_of_rejected_entries(month:str, year:str) -> int:
    """
    Returns the number of rejected entries in the corresponding month
    """
    month = check_months(month)
    year = check_years(year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        months = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ?AND status = 'REJECTED'", (month, year)).fetchone()

    number = int(months[0])
    return number

# List of years in database - date of upload (Current year and past year)
def upload_years():
    """
    Returns a list of years in the database
    """
    connection = sqlite3.connect('activity_log.db')
    
    with connection:
        cursor = connection.cursor()
        years = cursor.execute("SELECT DISTINCT upload_year FROM log").fetchall()
    
    YEARS = [year[0] for year in years]
    #No comma, not sure whether is a list
    # print("Printing YEARS")
    # print(YEARS)
    return YEARS

# Total number of entries for each year of upload
def yearly_entries(current_month, current_year, year) -> int:
    """
    Returns the number of entries in the corresponding year
    """
    year = check_years(year)
    current_month = check_months(current_month)
    current_year = check_years(current_year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        years = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND upload_year = ?", (current_month, current_year, year)).fetchone()

    number = int(years[0])
    return number

# Percentage of year entries of the total number of entries for selected month
def percentage_of_year_entries(month:str, current_year:str, year:str) -> float:
    """
    Returns the percentage of entries in the corresponding month
    """
    month = check_months(month)
    current_year = check_years(current_year)
    year = check_years(year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        month_count = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ?", (month, current_year)).fetchone()
        total = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND upload_year = ?", (month, current_year, year)).fetchone()

    percentage = (int(total[0])/int(month_count[0]))*100
    # print("Printing percentage")
    # print(percentage)
    final_value = round(percentage, 1)
    # print("Printing final_value")
    # print(final_value)
    return final_value
# Total number of approved entries for each year of upload
def yearly_approved_entries(current_month:str, current_year:str, year:str) -> int:
    """
    Returns the number of approved entries in the corresponding year
    """
    current_month = check_months(current_month)
    current_year = check_years(current_year)
    year = check_years(year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        years = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND upload_year = ? AND status = 'APPROVED'", (current_month, current_year, year)).fetchone()

    number = int(years[0])

    # print("Printing number")
    # print(number)
    return number

# Total number of pending entries for each year of upload
def yearly_pending_entries(current_month:str, current_year:str, year:str) -> int:
    """
    Returns the number of pending entries in the corresponding year
    """
    current_month = check_months(current_month)
    current_year = check_years(current_year)
    year = check_years(year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        years = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND upload_year = ? AND status = 'PENDING'", (current_month, current_year, year)).fetchone()

    number = int(years[0])
    return number

# Total number of rejected entries for each year of upload
def yearly_rejected_entries(current_month:str, current_year:str, year:str) -> int:
    """
    Returns the number of rejected entries in the corresponding year
    """
    current_month = check_months(current_month)
    current_year = check_years(current_year)
    year = check_years(year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        years = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND upload_year = ? AND status = 'REJECTED'", (current_month, current_year, year)).fetchone()

    number = int(years[0])
    return number

# Average number of days application in system (days left)
def average_days_left(current_month:str, current_year:str) -> int:
    """
    Returns the average number of days left for an application in the system
    """
    month = check_months(current_month)
    current_year = check_years(current_year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        days = cursor.execute("SELECT AVG(days_left) FROM log where month = ? AND year = ?", (month, current_year)).fetchone()

    number = int(days[0])
    # print("Printing number")
    # print(number)
    return number
# Number of entries oer sub-county
def entries_per_sub_county(current_month:str, current_year:str, sub_county:str) -> int:
    """
    Returns the number of entries in the corresponding sub-county
    """
    month = check_months(current_month)
    current_year = check_years(current_year)
    sub_county = check_sub_county(sub_county)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        entries = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND sub_county = ?", (month, current_year, sub_county)).fetchone()

    number = int(entries[0])
    # print("Printing number")
    # print(number)
    return number
# Percentage of entries per sub county of the total number of entries for selected month
def sub_county_percentage(current_month:str, current_year:str, sub_county:str) -> float:
    """
    Returns the percentage of entries in the corresponding sub-county
    """
    month = check_months(current_month)
    current_year = check_years(current_year)
    sub_county = check_sub_county(sub_county)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        month_count = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ?", (month, current_year)).fetchone()
        total = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND sub_county = ?", (month, current_year, sub_county)).fetchone()

    percentage = (int(total[0])/int(month_count[0]))*100
    final_value = round(percentage, 1)
    return final_value
# Total number of approved entries per sub county
def approved_entries_per_sub_county(current_month:str, current_year:str, sub_county:str) -> int:
    """
    Returns the number of approved entries in the corresponding sub-county
    """
    month = check_months(current_month)
    current_year = check_years(current_year)
    sub_county = check_sub_county(sub_county)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        entries = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND sub_county = ? AND status = 'APPROVED'", (month, current_year, sub_county)).fetchone()

    number = int(entries[0])
    return number
# Total number of pending entries per sub county
def pending_entries_per_sub_county(current_month:str, current_year:str, sub_county:str) -> int:
    """
    Returns the number of pending entries in the corresponding sub-county
    """
    month = check_months(current_month)
    current_year = check_years(current_year)
    sub_county = check_sub_county(sub_county)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        entries = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND sub_county = ? AND status = 'PENDING'", (month, current_year, sub_county)).fetchone()

    number = int(entries[0])
    return number
# Total number of rejected entries per sub county
def rejected_entries_per_sub_county(current_month:str, current_year:str, sub_county:str) -> int:
    """
    Returns the number of rejected entries in the corresponding sub-county
    """
    month = check_months(current_month)
    current_year = check_years(current_year)
    sub_county = check_sub_county(sub_county)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        entries = cursor.execute("SELECT COUNT(*) FROM log WHERE month = ? AND year = ? AND sub_county = ? AND status = 'REJECTED'", (month, current_year, sub_county)).fetchone()

    number = int(entries[0])
    return number
# List of floors and number of enries for each floor
def floor_entries(current_month, current_year):
    """
    Returns the number of entries in the corresponding floor
    """
    month = check_months(current_month)
    current_year = check_years(current_year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        entries = cursor.execute("SELECT floors, COUNT(*) FROM log WHERE month = ? AND year = ? GROUP BY floors", (month, current_year)).fetchall()

    # print("Printing floors")
    # print(entries)
    # # [('BASEMENT 1', 1), ('BASEMENT4', 1), ('FIRST FLOOR', 1), ('G+2', 1), ('G+3', 1), ('GROUND FLOOR', 1)]
    return entries

# List pof development types and number of entries for each development type
def description_entries(current_month, current_year):
    """
    Returns the number of entries in the corresponding development type
    """
    month = check_months(current_month)
    current_year = check_years(current_year)
    connection = sqlite3.connect('activity_log.db')

    with connection:
        cursor = connection.cursor()
        entries = cursor.execute("SELECT description, COUNT(*) FROM log WHERE month = ? AND year = ? GROUP BY description", (month, current_year)).fetchall()

    # print("Printing description types")
    # print(entries)
    # #[('COMMERCIAL', 3), ('EDICATIONAL', 1), ('INDUSTRIAL', 1), ('MIXED USE', 1)]

    return entries

if __name__ == '__main__':
    entry_months()
    entry_years()
    number_of_entries('JULY')
    upload_years()
    percentage_of_year_entries('JULY', '2024', '2023')
    yearly_approved_entries('JULY', '2024', '2024')
    average_days_left('JULY', '2024')
    entries_per_sub_county('JULY', '2024', 'Changamwe')
    floor_entries('JULY', '2024')
    description_entries('JULY', '2024')