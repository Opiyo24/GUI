from datetime import datetime

def todays_date():
    date = datetime.now()
    return date.strftime('%a %d %b %Y')


def save_date(value):
    date_string = value
    date_object = datetime.strptime(date_string, "%m/%d/%Y").date()
    return date_object





if __name__ == "__main__":
    print(datetime.now() - datetime.now())