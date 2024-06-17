import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from utils.functions import check, date_picker, days_count

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

entry = ctk.CTk()

entry.title('Activity Log | Entry')
entry.iconbitmap('')
entry.geometry('500x900')

ENTRY = ()

entry_date = ctk.StringVar()
upload_date = ctk.StringVar()
owner_entry = ctk.StringVar()
sub_county_entry = ctk.StringVar()
date_moved = ctk.StringVar()
# days_left = ctk.StringVar()
follow_up = ctk.StringVar()
description = ctk.StringVar()
floors = ctk.StringVar()
assigned = ctk.StringVar()
status = ctk.StringVar()


#Entry DAte
e_date = ctk.CTkLabel(
    entry,
    text = 'Entry Date',
)
e_date.pack()

entry_date_entry = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
    textvariable=entry_date,
)
entry_date_entry.pack()

e_d = ctk.CTkButton(
    entry,
    text = 'Select Date',
    height = 18,
    width = 20,
    command = date_picker,
)

e_d.pack(pady = 5)

#Date of upload
u_date = ctk.CTkLabel(
    entry,
    text = 'Date of Upload',
)
u_date.pack()

upload_date_entry = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
    textvariable=upload_date,
)
upload_date_entry.pack()

u_d = ctk.CTkButton(
    entry,
    text = 'Select Date',
    height = 18,
    width = 20,
    command = date_picker,
)

u_d.pack(pady = 5)

#Owner
owner_label = ctk.CTkLabel(
    entry,
    text = 'Owner',
)
owner_label.pack()

owner_entry_entry = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
    textvariable=owner_entry,
)
owner_entry_entry.pack(pady=5)

#Sub County
sub_county_label = ctk.CTkLabel(
    entry,
    text = 'sub_county',
)
sub_county_label.pack()

sub_county_entry_entry = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
    textvariable=sub_county_entry,
)
sub_county_entry_entry.pack(pady=5)

#Description
description_label = ctk.CTkLabel(
    entry,
    text = 'Description',
)
description_label.pack()

description_combo = ctk.CTkComboBox(
    entry,
    width = 150,
    height = 18,
    values = ['COMMERCIAL', 'RESIDENTIAL', 'MIXED USE', 'INDUSTRIAL', 'INSTITUTIONAL'],

)
description_combo.pack(pady=5)

#Floors
floors_label = ctk.CTkLabel(
    entry,
    text = 'Floors',
)
floors_label.pack()

floors_combo = ctk.CTkComboBox(
    entry,
    width = 150,
    height = 18,
    values = ['G', 'G+1', 'G+2', 'G+3', 'MEZZANINE'],

)
floors_combo.pack(pady=5)

#Assigned

assigned_label = ctk.CTkLabel(
    entry,
    text = 'Assigned',
)
assigned_label.pack()

assigned_combo = ctk.CTkComboBox(
    entry,
    width = 150,
    height = 18,
    values = ['Brian', 'Quincy', 'Sugoi', 'Gabriel', 'Opoyo'],

)
assigned_combo.pack(pady=5)

#Date moved
m_date = ctk.CTkLabel(
    entry,
    text = 'Date Moved',
)
m_date.pack()

date_moved_entry = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
    textvariable=date_moved,
)
date_moved_entry.pack()

m_d = ctk.CTkButton(
    entry,
    text = 'Select Date',
    height = 18,
    width = 20,
    command = date_picker,
)

m_d.pack(pady = 5)

#Days left
# days = ctk.CTkLabel(
#     entry,
#     text = 'Days Left',
#     command = days_count(entry_date, date_moved),
# )

# days.pack()

# days_left = ctk.CTkEntry(
#     entry,
#     width = 100,
#     height = 18,
# )

# days_left.pack()

#Last follow-up
follow_up_date = ctk.CTkLabel(
    entry,
    text = 'Last Follow-Up',
)
follow_up_date.pack()

follow_up_entry = ctk.CTkEntry(
    entry,
    width = 100,
    height = 18,
    textvariable=follow_up,
)
follow_up_entry.pack()

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

status_combo = ctk.CTkComboBox(
    entry,
    width = 150,
    height = 18,
    values = ['PENDING', 'APPROVED', 'REJECTED', 'REVIEW'],

)

status_combo.pack(pady=5)


def submit():
    global ENTRY

    if (entry_date.get() == '' or upload_date.get() == '' or owner_entry.get() == '' or
            sub_county_entry.get() == '' or date_moved.get() == '' or follow_up.get() == '' or
            description_combo.get() == '' or floors_combo.get() == '' or assigned_combo.get() == '' or status_combo.get() == ''):
        alert_label.configure(text='All fields are required', text_color='red')
    else:
        new_list = list(ENTRY)
        new_list.append(entry_date.get())
        new_list.append(upload_date.get())
        new_list.append(owner_entry.get())
        new_list.append(sub_county_entry.get())
        new_list.append(description_combo.get())
        new_list.append(floors_combo.get())
        new_list.append(assigned_combo.get())
        new_list.append(date_moved.get())
        new_list.append(lambda: days_count(entry_date, date_moved))
        new_list.append(follow_up.get())
        new_list.append(status_combo.get())
        ENTRY = tuple(new_list)
        print(ENTRY)


submit_button = ctk.CTkButton(
    entry,
    text = 'Submit',
    height = 18,
    width = 20,
    command = submit,
)

submit_button.pack(pady = 10)

alert_label = ctk.CTkLabel(
    entry,
    text = '',
)
alert_label.pack()


entry.mainloop()



