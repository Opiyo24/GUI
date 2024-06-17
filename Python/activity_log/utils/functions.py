import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


def check(widget):
    if widget.get() == '':
        widget.config(
            border_color = 'red'
        )
        return False
    return True


def date_picker():
    date = 'date'
    return date

def days_count(start_date, end_date):
    return end_date - start_date