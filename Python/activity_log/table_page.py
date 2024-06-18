import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from entry import ENTRY
from utils.date_picker import *

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

window = ctk.CTk()

window.title('Activity Log')
window.iconbitmap('')
window.geometry('1600x800')
window.minsize(1600, 800)

window.columnconfigure((0,1,2,3,4,5,6,7,8), weight = 1, uniform = 'a')
window.rowconfigure((0,1,2,3,4,5,6), weight = 1, uniform = 'a')

cols = [
    "Entry Date",
    "Upload Date",
    "Owner",
    "Sub-County",
    "Description",
    "Floors",
    "Assigned",
    "Date Moved",
    "Days Left",
    "Last Follow-Up",
    "Status",
]

menu_frame = ctk.CTkFrame(
    window,
    border_width = 0,
    border_color = 'black',
    fg_color = 'green',
    corner_radius = 0,
)
menu_frame.grid(
    row = 0,
    column = 0,
    rowspan = 7,
    sticky = 'news',
)

main_frame = ctk.CTkFrame(
    window,
    border_width = 0,
    border_color = 'black',
    bg_color= 'blue',
    fg_color = '#ecf496',
)
main_frame.grid(
    row = 0,
    column = 1,
    rowspan = 7,
    columnspan = 8,
    sticky = 'news',
)

m_button1 = ctk.CTkButton(
    menu_frame,
    height = 50,
    text = 'Home',
    font = ('Helvetica', 20, 'bold'),
    # anchor = 'w',
    bg_color = 'transparent',
    fg_color = 'transparent',
    corner_radius = 0,
    border_width = 0,
)
m_button1.pack(
    fill = 'x',
    padx = 1,
    pady = 4,
)

m_button2 = ctk.CTkButton(
    menu_frame,
    height = 50,
    text = 'Dashboard',
    font = ('Helvetica', 20, 'bold'),
    bg_color = 'transparent',
    fg_color = 'transparent',
    corner_radius = 0,
    border_width = 0,
)
m_button2.pack(
    fill = 'x',
    padx = 1,
    pady = 4,
)

m_button3 = ctk.CTkButton(
    menu_frame,
    height = 50,
    font = ('Helvetica', 20, 'bold'),
    text = 'Members',
    bg_color = 'transparent',
    fg_color = 'transparent',
    corner_radius = 0,
    border_width = 0,
)
m_button3.pack(
    fill = 'x',
    padx = 1,
    pady = 4,
)

# name_label = ctk.CTkLabel(
#     menu_frame,
#     text = 'Username',
# )


date = ctk.CTkLabel(
    window,
    text = '',
    font = ('Helvetica', 20, 'bold'),
)

date.grid(
    row = 0,
    column = 1,
)
def update_date():
    date.configure(text = todays_date())

update_date()

back_button = ctk.CTkButton(
    window,
    text = 'Back',
    font = ('Helvetica', 20, 'bold'),
    height = 40,
    bg_color = 'transparent',
    fg_color = 'black',
    corner_radius = 10,
    border_width = 3,
)
back_button.grid(
    row = 0,
    column = 8,
)

entry_button = ctk.CTkButton(
    window,
    text = 'New Entry',
    height = 35,
    width = 50,
    bg_color = 'blue',
    fg_color = 'black',
    corner_radius = 10,
    border_width = 3,
)

entry_button.grid(
    row = 1,
    column = 1,
    # columnspan = 2,
    # sticky = 'news',
)

data_frame = ctk.CTkScrollableFrame(
    window,
    border_width = 1,
    border_color = 'black',
    corner_radius = 0,
)

data_frame.grid(
    row = 2,
    column = 1,
    rowspan = 5,
    columnspan = 8,
    sticky = 'news',
)

sort_frame = ctk.CTkFrame(
    window,
    border_width = 0,
    bg_color = 'transparent',
    fg_color = 'transparent',
)
sort_frame.grid(
    row = 1,
    column = 6,
    sticky = 'news',
)

sort_label = ctk.CTkLabel(
    sort_frame,
    text = 'Sort by:',
    font = ('Helvetica', 11),
)

sort_label.pack(
    anchor = 'w',
    padx = 10
)

sort = ctk.CTkComboBox(
    sort_frame,
    values = cols,
)
sort.pack()

filter_label_frame = tk.LabelFrame(
    window,
    text = 'Filter',
    font = ('Helvetica', 10),
    height = 60,
    # background = 'blue',
)
filter_label_frame.grid(
    row = 1,
    column = 7,
    columnspan = 2,
    sticky = 'news',
    pady = 10,
)

filter_label_frame.columnconfigure(0, weight = 1)

filter_1  = ctk.CTkComboBox(
    filter_label_frame,
    values = cols,
)
filter_1.grid(
    row = 0,
    column = 0,
)

filter_2 = ctk.CTkComboBox(
    filter_label_frame,
    values = cols,
)
filter_2.grid(
    row = 0,
    column = 1,
)

table = ttk.Treeview(
    data_frame,
    columns = cols,
    show = 'headings',
)
table.heading("Entry Date", text = "Entry Date")
table.heading("Upload Date", text = "Upload Date")
table.heading("Owner", text = "Owner")
table.heading("Sub-County", text = "Sub-County")
table.heading("Description", text = "Description")
table.heading("Floors", text = "Floors")    
table.heading("Assigned", text = "Assigned")
table.heading("Date Moved", text = "Date Moved")
table.heading("Days Left", text = "Days Left")
table.heading("Last Follow-Up", text = "Last Follow-Up")
table.heading("Status", text = "Status")
table.pack(
    fill = 'both',
    expand = True,
)

#Insert values - Data from ENTRIES - loop trough the list and insert values
# ENTRIES = ("1/1/2020", "5/1/2020", "John Doe", "Nairobi", "Lorem Ipsum", "5", "Jane Doe", "3/1/2020", "5", "4/1/2020", "Pending")
table.insert("", "end", values = ENTRY)

window.mainloop()