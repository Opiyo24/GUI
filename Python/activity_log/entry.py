import tkinter as tk
from tkcalendar import DateEntry
import customtkinter as ctk
from uuid import uuid4

from utils.functions import days_count
from utils.date_picker import *
from database.database import *

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')

entry = ctk.CTk()

entry.title('Activity Log | Entry')
entry.iconbitmap('')
entry.geometry('700x400')
entry.minsize(700, 400)
entry.maxsize(700, 400)
entry.rowconfigure((0, 1, 2, 3, 4), weight = 1, uniform = 'a')
entry.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19), weight = 1, uniform = 'a')
entry.configure(bg='#f5f7f8')
entry.configure(fg='#f5f7f8')


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
Issues_entry = ctk.StringVar()
Remarks_entry = ctk.StringVar()


#Entry DAte
entry_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)
entry_frame.grid(
    row = 0,
    column = 0,
    columnspan = 4,
    sticky = 'news',
)
e = ctk.CTkLabel(
    entry_frame,
    text = '',
    height = 10,
)
e.pack()

entry_date = ctk.CTkLabel(
    entry_frame,
    text = 'Entry Date',
    font = ('Helvetica', 12),
    text_color = 'black',
)
entry_date.pack(
    anchor = 'w',
)

entry_date_entry = DateEntry(
    entry_frame,
    width = 18,
    height = 32,
    selectmode='day',
    date_pattern='m/d/yyyy',
    # padx = 10,
    textvariable=upload_date,
)
entry_date_entry.pack(
    anchor = 'w',
)

# Date of upload
upload_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)
upload_frame.grid(
    row = 0,
    column = 4,
    columnspan = 4,
    sticky = 'news',
)
e = ctk.CTkLabel(
    upload_frame,
    text = '',
    height = 10,
)
e.pack()
u_date = ctk.CTkLabel(
    upload_frame,
    text = 'Date of Upload',
    font = ('Helvetica', 12),
    text_color = 'black',
)
u_date.pack(
    anchor = 'w',
)

upload_date_entry = DateEntry(
    upload_frame,
    width = 18,
    height = 32,
    selectmode='day',
    date_pattern='m/d/yyyy',
    # padx = 10,
    textvariable=upload_date,
)
upload_date_entry.pack(
    anchor = 'w',
)

owner_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

owner_frame.grid(
    row = 0,
    column = 8,
    columnspan = 6,
    sticky = 'news',
)
e = ctk.CTkLabel(
    owner_frame,
    text = '',
    height = 10,
)
e.pack(anchor = 'w')
# #Owner
owner_label = ctk.CTkLabel(
    owner_frame,
    text = 'Owner',
    font = ('Helvetica', 12),
    text_color = 'black',
)
owner_label.pack(
    anchor = 'w',
    padx = 10,
    # pady = 10,
)

owner_entry_entry = ctk.CTkEntry(
    owner_frame,
    width = 250,
    height = 32,
    textvariable=owner_entry,
)
owner_entry_entry.pack(
    anchor = 'w',
    padx = 10,
    # pady = 10,
)


plot_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

plot_frame.grid(
    row = 0,
    column = 14,
    columnspan = 6,
    sticky = 'news',
)
e = ctk.CTkLabel(
    plot_frame,
    text = '',
    height = 10,
)
e.pack()

plot_no = ctk.CTkLabel(
    plot_frame,
    text = 'Plot No',
    font = ('Helvetica', 12),
    text_color = 'black',
)
plot_no.pack(anchor = 'w')

plot_no_entry = ctk.CTkEntry(
    plot_frame,
    width = 200,
    height = 32,
)
plot_no_entry.pack(anchor = 'w')

# #Sub County
sub_county_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

sub_county_frame.grid(
    row = 1,
    column = 0,
    columnspan = 6,
    sticky = 'news',
)
e = ctk.CTkLabel(
    sub_county_frame,
    text = '',
    height = 10,
)
e.pack()

sub_county_label = ctk.CTkLabel(
    sub_county_frame,
    text = 'Sub-County',
    font = ('Helvetica', 12),
    text_color = 'black',
)
sub_county_label.pack(anchor = 'w')

sub_county_combo = ctk.CTkComboBox(
    sub_county_frame,
    width = 200,
    height = 32,
    values = ['', 'CHANGAMWE', 'JOMVU', 'KISAUNI', 'NYALI', 'LIKONI', 'MVITA'],
    # textvariable=sub_county_entry,
)
sub_county_combo.pack(anchor = 'w')

# #Description
description_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

description_frame.grid(
    row = 1,
    column = 6,
    columnspan = 7,
    sticky = 'news',
)
e = ctk.CTkLabel(
    description_frame,
    text = '',
    height = 10,
)
e.pack()

description_label = ctk.CTkLabel(
    description_frame,
    text = 'Description',
    font = ('Helvetica', 12),
    text_color = 'black',
)
description_label.pack(anchor = 'w')

description_combo = ctk.CTkComboBox(
    description_frame,
    width = 150,
    height = 32,
    values = ['', 'COMMERCIAL', 'RESIDENTIAL', 'MIXED USE', 'INDUSTRIAL', 'INSTITUTIONAL'],

)
description_combo.pack(anchor = 'w')

# #Floors
floors_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

floors_frame.grid(
    row = 1,
    column = 13,
    columnspan = 7,
    sticky = 'news',
)
e = ctk.CTkLabel(
    floors_frame,
    text = '',
    height = 10,
)
e.pack()
floors_label = ctk.CTkLabel(
    floors_frame,
    text = 'Floors',
    font = ('Helvetica', 12),
    text_color = 'black',
)
floors_label.pack(anchor ='w')

floors_combo = ctk.CTkComboBox(
    floors_frame,
    width = 150,
    height = 32,
    values = ['', 'G', 'G+1', 'G+2', 'G+3', 'MEZZANINE'],

)
floors_combo.pack(anchor ='w')

# #Assigned
assigned_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

assigned_frame.grid(
    row = 2,
    column = 0,
    columnspan = 5,
    sticky = 'news',
)
e = ctk.CTkLabel(
    assigned_frame,
    text = '',
    height = 10,
)
e.pack()

assigned_label = ctk.CTkLabel(
    assigned_frame,
    text = 'Assigned',
    font = ('Helvetica', 12),
    text_color = 'black',
)
assigned_label.pack(anchor = 'w')

assigned_combo = ctk.CTkComboBox(
    assigned_frame,
    width = 150,
    height = 32,
    values = ['', 'Brian', 'Quincy', 'Sugoi', 'Gabriel', 'Opoyo'],

)
assigned_combo.pack(anchor = 'w')


#Empty frame
empty1_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

empty1_frame.grid(
    row = 2,
    column = 5,
    columnspan = 1,
    sticky = 'news',
)
# #Date moved
dm_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

dm_frame.grid(
    row = 2,
    column = 6,
    columnspan = 4,
    sticky = 'news',
)
e = ctk.CTkLabel(
    dm_frame,
    text = '',
    height = 10,
)
e.pack()

m_date = ctk.CTkLabel(
    dm_frame,
    text = 'Date Moved',
    font = ('Helvetica', 12),
    text_color = 'black',
)
m_date.pack(anchor = 'w')

date_moved_entry = DateEntry(
    dm_frame,
    selectmode='day',
    date_pattern='m/d/yyyy',
    textvariable=date_moved,
)
date_moved_entry.pack(anchor ='w')


#empty frame
empty3_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

empty3_frame.grid(
    row = 2,
    column = 10,
    columnspan = 1,
    sticky = 'news',
)
# #Last follow-up
last_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

last_frame.grid(
    row = 2,
    column = 11,
    columnspan = 5,
    sticky = 'news',
)
e = ctk.CTkLabel(
    last_frame,
    text = '',
    height = 10,
)
e.pack()

ref_number_label = ctk.CTkLabel(
    last_frame,
    text = 'Ref No',
    font = ('Helvetica', 12),
    text_color = 'black',
)

ref_number_label.pack(anchor = 'w')

ref_number_entry = ctk.CTkEntry(
    last_frame,
    height = 32,
)
ref_number_entry.pack(anchor = 'w')


#empty frame
empty3_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

empty3_frame.grid(
    row = 2,
    column = 16,
    columnspan = 1,
    sticky = 'news',
)
# #status
status_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

status_frame.grid(
    row = 2,
    column = 17,
    columnspan = 3,
    sticky = 'news',
)
e = ctk.CTkLabel(
    status_frame,
    text = '',
    height = 10,
)
e.pack()

status_label = ctk.CTkLabel(
    status_frame,
    text = 'Status',
    font = ('Helvetica', 12),
    text_color = 'black',
)
status_label.pack(anchor = 'w')

status_combo = ctk.CTkComboBox(
    status_frame,
    width = 150,
    height = 32,
    values = ['', 'PENDING', 'APPROVED', 'REJECTED', 'REVIEW'],
)
status_combo.pack(anchor = 'w')

# #Issues
issues_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

issues_frame.grid(
    row = 3,
    column = 0,
    columnspan = 10,
    sticky = 'news',
)

Issues_label = ctk.CTkLabel(
    issues_frame,
    text = 'Issues',
    font = ('Helvetica', 12),
    text_color = 'black',
)
Issues_label.pack(anchor = 'w')

Issues_entry = ctk.CTkEntry(
    issues_frame,
    width = 350,
    height =50,
    textvariable = Issues_entry,
)
Issues_entry.pack(anchor = 'w')


#empty frame
empty4_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

empty4_frame.grid(
    row = 3,
    column = 10,
    columnspan = 1,
    sticky = 'news',
)
# #Remarks
remarks_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

remarks_frame.grid(
    row = 3,
    column = 11,
    columnspan = 9,
    sticky = 'news',
)

Remarks_label = ctk.CTkLabel(
    remarks_frame,
    text = 'Remarks',
    font = ('Helvetica', 12),
    text_color = 'black',
)
Remarks_label.pack(anchor = 'w')

Remarks_entry = ctk.CTkEntry(
    remarks_frame,
    width = 320,
    height = 50,
    textvariable = Remarks_entry,
)
Remarks_entry.pack(anchor = 'w')


submit_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

submit_frame.grid(
    row = 4,
    column = 18,
    columnspan = 2,
    sticky = 'news',
)

submit_button = ctk.CTkButton(
    submit_frame,
    text = 'SUBMIT',
    height = 30,
    width = 24,
    # command = submit,
)
submit_button.pack(padx = 2,
                   pady = 30)

cancel_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

cancel_frame.grid(
    row = 4,
    column = 16,
    columnspan = 2,
    sticky = 'news',
)
cancel_button = ctk.CTkButton(
    cancel_frame,
    text = 'CANCEL',
    height = 30,
    width = 24,
    # command = submit,
)
cancel_button.pack(padx = 2,
                   pady = 30)

clear_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

clear_frame.grid(
    row = 4,
    column = 14,
    columnspan = 2,
    sticky = 'news',
)
clear_button = ctk.CTkButton(
    clear_frame,
    text = 'CLEAR',
    height = 30,
    width = 24,
    # bg_color = '#f5f7f8',
    # fg_color = '#f5f7f8',
    # command = clear,
)
clear_button.pack(padx = 2,
                   pady = 30)

empty_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

empty_frame.grid(
    row = 4,
    column = 0,
    columnspan = 1,
    sticky = 'news',
)

#empty frame
empty5_frame = ctk.CTkFrame(
    entry,
    bg_color = '#f5f7f8',
    fg_color = '#f5f7f8',
    # border_width = 2,
    # border_color = 'black',
)

empty5_frame.grid(
    row = 4,
    column = 1,
    columnspan = 13,
    sticky = 'news',
)


alert_label = ctk.CTkLabel(
    entry,
    text = '',
)
# alert_label.pack()


entry.mainloop()

# if __name__ == "__main__":
#     entry()

# def submit():
#     global ENTRY

#     if (entry_date.get() == '' or upload_date.get() == '' or owner_entry.get() == '' or
#             sub_county_entry.get() == '' or date_moved.get() == '' or follow_up.get() == '' or
#             description_combo.get() == '' or floors_combo.get() == '' or assigned_combo.get() == '' or status_combo.get() == ''):
#         alert_label.configure(text='All fields are required', text_color='red')
#     else:
#         days = days_count(entry_date.get(), date_moved.get())
#         # print(days)

#         new_list = list(ENTRY)
#         new_list.append(str(uuid4()))
#         new_list.append(save_date(entry_date.get()))
#         new_list.append(save_date(upload_date.get()))
#         new_list.append(owner_entry.get())
#         new_list.append(sub_county_entry.get())
#         new_list.append(description_combo.get())
#         new_list.append(floors_combo.get())
#         new_list.append(Issues_entry.get())
#         new_list.append(assigned_combo.get())
#         new_list.append(save_date(date_moved.get()))
#         new_list.append(days)
#         new_list.append(save_date(follow_up.get()))
#         new_list.append(status_combo.get())
#         new_list.append(Remarks_entry.get())
#         ENTRY = tuple(new_list)
#         # print(ENTRY)

#         entry.destroy()

#         #insert data into sqlite database
#         make_entry(ENTRY)

