import tkinter as tk
import customtkinter as ctk
import calendar
from datetime import datetime

def todays_date():
    date = datetime.now()
    return date.strftime('%a %d %b %Y')


print(todays_date())

def date_picker():
    pass


print(datetime.now() - datetime.now())