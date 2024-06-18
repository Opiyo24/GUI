import tkinter as tk
from tkcalendar import DateEntry

my_w = tk.Tk()
my_w.geometry("340x220")

cal = DateEntry(my_w, selectmode='day')
cal.grid(row=1, column=1, padx=15)

my_w.mainloop()
