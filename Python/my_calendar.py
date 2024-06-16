import tkinter as tk
from tkinter import ttk
from calendar import monthrange
from datetime import datetime, timedelta

def popup_calendar():
    # Create a new window for the calendar
    calendar_window = tk.Toplevel(root)
    calendar_window.title("Calendar")

    # Create a calendar widget
    calendar = ttk.Calendar(calendar_window, selectmode="day", year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
    calendar.pack(pady=10)

    # Create a button to select the date
    def select_date():
        date = calendar.selection_get()
        date_str = date.strftime("%Y-%m-%d")
        entry.delete(0, tk.END)
        entry.insert(0, date_str)
        calendar_window.destroy()

    select_button = tk.Button(calendar_window, text="Select Date", command=select_date)
    select_button.pack(pady=10)

root = tk.Tk()
root.title("Calendar Popup Example")

# Create an entry field for the date
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Create a button to open the calendar
button = tk.Button(root, text="Open Calendar", command=popup_calendar)
button.pack(pady=10)

root.mainloop()