import tkinter as tk
import customtkinter as ctk
import calendar
from datetime import datetime

def todays_date():
    date = datetime.now()
    return date.strftime('%a %d %b %Y')


def save_date(value):
    date_string = value
    date_object = datetime.strptime(date_string, "%m/%d/%Y").date()
    return date_object


print(datetime.now() - datetime.now())