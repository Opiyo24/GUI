import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from datetime import datetime


def check(widget):
    if widget.get() == '':
        widget.config(
            border_color = 'red'
        )
        return False
    return True



def days_count(start_date, end_date):
    start_date = datetime.strptime(start_date, "%m/%d/%Y").date()
    end_date = datetime.strptime(end_date, "%m/%d/%Y").date()
    return (end_date - start_date).days