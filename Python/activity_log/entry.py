import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

entry = ctk.CTk()

entry.title('Activity Log | Entry')
entry.iconbitmap('')
entry.geometry('500x900')

#Entry DAte
e_date = ctk.CTkLabel(
    entry,
    text = 'Entry Date',
)
e_date.pack()

entry_date = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
)
entry_date.pack()

e_d = ctk.CTkButton(
    entry,
    text = 'Select Date',
    height = 18,
    width = 20,
)

e_d.pack(pady = 5)

#Date of upload
u_date = ctk.CTkLabel(
    entry,
    text = 'Date of Upload',
)
u_date.pack()

upload_date = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
)
upload_date.pack()

u_d = ctk.CTkButton(
    entry,
    text = 'Select Date',
    height = 18,
    width = 20,
)

u_d.pack(pady = 5)

#Owner
owner_label = ctk.CTkLabel(
    entry,
    text = 'Owner',
)
owner_label.pack()

owner_entry = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
)
owner_entry.pack(pady=5)

#Sub County
sub_county_label = ctk.CTkLabel(
    entry,
    text = 'sub_county',
)
sub_county_label.pack()

sub_county_entry = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
)
sub_county_entry.pack(pady=5)

#Description
description_label = ctk.CTkLabel(
    entry,
    text = 'Description',
)
description_label.pack()

description = ctk.CTkComboBox(
    entry,
    width = 150,
    height = 18,
    values = ['COMMERCIAL', 'RESIDENTIAL', 'MIXED USE', 'INDUSTRIAL', 'INSTITUTIONAL'],
)
description.pack(pady=5)

#Floors
floors_label = ctk.CTkLabel(
    entry,
    text = 'Floors',
)
floors_label.pack()

floors = ctk.CTkComboBox(
    entry,
    width = 150,
    height = 18,
    values = ['G', 'G+1', 'G+2', 'G+3', 'MEZZANINE'],
)
floors.pack(pady=5)

#Assigned

assigned_label = ctk.CTkLabel(
    entry,
    text = 'Assigned',
)
assigned_label.pack()

assigned = ctk.CTkComboBox(
    entry,
    width = 150,
    height = 18,
    values = ['Brian', 'Quincy', 'Sugoi', 'Gabriel', 'Opoyo'],
)
assigned.pack(pady=5)

#Date moved
m_date = ctk.CTkLabel(
    entry,
    text = 'Date Moved',
)
m_date.pack()

date_moved = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
)
date_moved.pack()

m_d = ctk.CTkButton(
    entry,
    text = 'Select Date',
    height = 18,
    width = 20,
)

m_d.pack(pady = 5)

#Days left
days = ctk.CTkLabel(
    entry,
    text = 'Days Left',
)

days.pack()

days_left = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
)

days_left.pack()

#Last follow-up
follow_up_date = ctk.CTkLabel(
    entry,
    text = 'Last Follow-Up',
)
follow_up_date.pack()

follow_up = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
)
follow_up.pack()

f_d = ctk.CTkButton(
    entry,
    text = 'Select Date',
    height = 18,
    width = 20,
)

f_d.pack(pady = 5)

#status
status_label = ctk.CTkLabel(
    entry,
    text = 'Status',
)
status_label.pack()

status = ctk.CTkComboBox(
    entry,
    width = 150,
    height = 18,
    values = ['PENDING', 'APPROVED', 'REJECTED', 'REVIEW'],
)

status.pack(pady=5)


entry.mainloop()