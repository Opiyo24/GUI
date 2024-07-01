import tkinter as tk
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import ttk
import customtkinter as ctk
from uuid import uuid4


# from entry import ENTRY
from utils.date_picker import *
from database.database import *
from utils.functions import days_count

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

global action
action = 'entry'

ENTRY = ()

def entry_function():

    global ENTRY, action, selected_entry
    global entry_date_entry, upload_date_entry, owner_entry_entry, sub_county_combo, plot_no_entry, description_combo, floors_combo, assigned_combo, date_moved_entry, ref_number_entry, status_combo, Issues_entry, Remarks_entry

    #TODO: Update window title to render todays date
    entry_window = ctk.CTk()
    entry_window.title('Activity Log | entry_window')
    entry_window.iconbitmap('')
    entry_window.geometry('700x400')
    entry_window.minsize(700, 400)
    entry_window.maxsize(700, 400)
    entry_window.rowconfigure((0, 1, 2, 3, 4), weight = 1, uniform = 'a')
    entry_window.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19), weight = 1, uniform = 'a')
    entry_window.configure(bg='#f5f7f8')
    entry_window.configure(fg='#f5f7f8')

    entry_date = ctk.StringVar()
    upload_date = ctk.StringVar()
    owner = ctk.StringVar()
    sub_county_combo = ctk.StringVar()
    date_moved = ctk.StringVar()
    plot_no = ctk.StringVar()
    description = ctk.StringVar()
    floors = ctk.StringVar()
    assigned = ctk.StringVar()
    status = ctk.StringVar()
    issues = ctk.StringVar()
    ref_no = ctk.StringVar()
    remarks = ctk.StringVar()

    entry_window.title('Activity Log | Entry')
    entry_window.iconbitmap('')
    entry_window.geometry('500x900')

    sub_county_vals = entries_list('sub_county')
    description_vals = entries_list('description')
    floors_vals = entries_list('floors')
    assigned_vals = entries_list('assigned')
    status_vals = entries_list('status')

    

#TODO: Style the entry window with place  
#Entry DAte
    entry_frame = ctk.CTkFrame(entry_window, bg_color = '#f5f7f8', fg_color = '#f5f7f8',)
    entry_frame.grid( row = 0, column = 0, columnspan = 4, sticky = 'news',)
    e = ctk.CTkLabel(entry_frame, text = '', height = 10,)
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
        textvariable=entry_date,
    )
    entry_date_entry.pack(
        anchor = 'w',
    )

    #Upload Date
    upload_frame = ctk.CTkFrame(
        entry_window,
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
        entry_window,
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
        textvariable=owner,
    )
    owner_entry_entry.pack(
        anchor = 'w',
        padx = 10,
        # pady = 10,
    )


    plot_frame = ctk.CTkFrame(
        entry_window,
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
        entry_window,
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
        values = sub_county_vals,
        # textvariable=sub_county_entry,
    )
    sub_county_combo.pack(anchor = 'w')

    # #Description
    description_frame = ctk.CTkFrame(
        entry_window,
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
        values = description_vals,

    )
    description_combo.pack(anchor = 'w')

    # #Floors
    floors_frame = ctk.CTkFrame(
        entry_window,
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
        values = floors_vals,

    )
    floors_combo.pack(anchor ='w')

    # #Assigned
    assigned_frame = ctk.CTkFrame(
        entry_window,
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
        values = assigned_vals,

    )
    assigned_combo.pack(anchor = 'w')


    #Empty frame
    empty1_frame = ctk.CTkFrame(
        entry_window,
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
        entry_window,
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
        entry_window,
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
        entry_window,
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
        entry_window,
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
        entry_window,
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
        values = status_vals,
    )
    status_combo.pack(anchor = 'w')

    # #Issues
    issues_frame = ctk.CTkFrame(
        entry_window,
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
        textvariable = issues,
    )
    Issues_entry.pack(anchor = 'w')


    #empty frame
    empty4_frame = ctk.CTkFrame(
        entry_window,
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
        entry_window,
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
        textvariable = remarks,
    )
    Remarks_entry.pack(anchor = 'w')


    submit_frame = ctk.CTkFrame(
        entry_window,
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
        command = lambda: submit(entry_window),
    )
    submit_button.pack(padx = 2,
                    pady = 30)

    cancel_frame = ctk.CTkFrame(
        entry_window,
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
        command = lambda: cancel_entry(entry_window),
    )
    # cancel_button.pack(padx = 2,
                    # pady = 30)

    clear_frame = ctk.CTkFrame(
        entry_window,
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
        command = clear,
    )
    clear_button.pack(padx = 2,
                    pady = 30)

    empty_frame = ctk.CTkFrame(
        entry_window,
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
        entry_window,
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


    entry_window.mainloop()


def detail_window():

    global ENTRY, action, selected_entry
    global entry_date_entry, upload_date_entry, owner_entry_entry, sub_county_combo, plot_no_entry, description_combo, floors_combo, assigned_combo, date_moved_entry, ref_number_entry, status_combo, Issues_entry, Remarks_entry

    #TODO: Update window title to render todays date
    entry_window = ctk.CTk()
    entry_window.title('Activity Log | entry_window')
    entry_window.iconbitmap('')
    entry_window.geometry('700x400')
    entry_window.minsize(700, 400)
    entry_window.maxsize(700, 400)
    entry_window.rowconfigure((0, 1, 2, 3, 4), weight = 1, uniform = 'a')
    entry_window.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19), weight = 1, uniform = 'a')
    entry_window.configure(bg='#f5f7f8')
    entry_window.configure(fg='#f5f7f8')

    entry_date = ctk.StringVar()
    upload_date = ctk.StringVar()
    owner = ctk.StringVar()
    sub_county_combo = ctk.StringVar()
    date_moved = ctk.StringVar()
    plot_no = ctk.StringVar()
    description = ctk.StringVar()
    floors = ctk.StringVar()
    assigned = ctk.StringVar()
    status = ctk.StringVar()
    issues = ctk.StringVar()
    ref_no = ctk.StringVar()
    remarks = ctk.StringVar()

    entry_window.title('Activity Log | Entry')
    entry_window.iconbitmap('')
    entry_window.geometry('500x900')

    sub_county_vals = entries_list('sub_county')
    description_vals = entries_list('description')
    floors_vals = entries_list('floors')
    assigned_vals = entries_list('assigned')
    status_vals = entries_list('status')

    pk=selected_entry[0]
    window = entry_window

    

#TODO: Style the entry window with place  
#Entry DAte
    entry_frame = ctk.CTkFrame(entry_window, bg_color = '#f5f7f8', fg_color = '#f5f7f8',)
    entry_frame.grid( row = 0, column = 0, columnspan = 4, sticky = 'news',)
    e = ctk.CTkLabel(entry_frame, text = '', height = 10,)
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
        textvariable=entry_date,
    )
    entry_date_entry.pack(
        anchor = 'w',
    )

    #Upload Date
    upload_frame = ctk.CTkFrame(
        entry_window,
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
        entry_window,
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
        textvariable=owner,
    )
    owner_entry_entry.pack(
        anchor = 'w',
        padx = 10,
        # pady = 10,
    )


    plot_frame = ctk.CTkFrame(
        entry_window,
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
        entry_window,
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
        values = sub_county_vals,
        # textvariable=sub_county_entry,
    )
    sub_county_combo.pack(anchor = 'w')

    # #Description
    description_frame = ctk.CTkFrame(
        entry_window,
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
        values = description_vals,

    )
    description_combo.pack(anchor = 'w')

    # #Floors
    floors_frame = ctk.CTkFrame(
        entry_window,
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
        values = floors_vals,

    )
    floors_combo.pack(anchor ='w')

    # #Assigned
    assigned_frame = ctk.CTkFrame(
        entry_window,
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
        values = assigned_vals,

    )
    assigned_combo.pack(anchor = 'w')


    #Empty frame
    empty1_frame = ctk.CTkFrame(
        entry_window,
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
        entry_window,
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
        entry_window,
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
        entry_window,
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
        entry_window,
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
        entry_window,
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
        values = status_vals,
    )
    status_combo.pack(anchor = 'w')

    # #Issues
    issues_frame = ctk.CTkFrame(
        entry_window,
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
        textvariable = issues,
    )
    Issues_entry.pack(anchor = 'w')


    #empty frame
    empty4_frame = ctk.CTkFrame(
        entry_window,
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
        entry_window,
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
        textvariable = remarks,
    )
    Remarks_entry.pack(anchor = 'w')


    submit_frame = ctk.CTkFrame(
        entry_window,
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
        command = lambda: edit(pk, window),
    )
    submit_button.pack(padx = 2,
                    pady = 30)

    cancel_frame = ctk.CTkFrame(
        entry_window,
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
        command = lambda: cancel_entry(entry_window),
    )
    # cancel_button.pack(padx = 2,
                    # pady = 30)

    delete_frame = ctk.CTkFrame(
        entry_window,
        bg_color = '#f5f7f8',
        fg_color = '#f5f7f8',
        # border_width = 2,
        # border_color = 'black',
    )

    delete_frame.grid(
        row = 4,
        column = 14,
        columnspan = 2,
        sticky = 'news',
    )
    delete_button = ctk.CTkButton(
        delete_frame,
        text = 'DELETE',
        height = 30,
        width = 24,
        # bg_color = '#f5f7f8',
        # fg_color = '#f5f7f8',
        command = lambda: delete(pk, window),
    )
    delete_button.pack(padx = 2,
                    pady = 30)

    empty_frame = ctk.CTkFrame(
        entry_window,
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
        entry_window,
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

    # print("Printing values")
    # print(selected_entry[0])
    # print(selected_entry[1])
    # print(selected_entry[2])
    # print(selected_entry[3])
    # print(selected_entry[4])
    # print(selected_entry[5])
    # print(selected_entry[6])
    # print(selected_entry[7])
    # print(selected_entry[8])
    # print(selected_entry[9])
    # print(selected_entry[10])
    # print(selected_entry[11])
    # print(selected_entry[12])
    # print(selected_entry[13])

    # ('1c880591-cdb6-4a45-b6b3-24a187be95b2', '2024-06-27', '2024-06-27', 'Kimani Allan', 'KISAUNI', 'INDUSTRIAL', 'G+1', 'None', 'Opoyo', '2024-07-05', 8, 'CCC/23', 'PENDING', 'P/654/2021')

    #TODO: Save remarks to database
    #TODO: Convert date values to string
    #TODO: create independent edit function
    #TODO: Update save function to update in stead of creating new entry

    # if action != 'entry':
    entry_d = convert_date_format(selected_entry[1])
    upload = convert_date_format(selected_entry[2])
    moved = convert_date_format(selected_entry[9])

    entry_date_entry.delete(0, '')
    upload_date_entry.delete(0, '')
    date_moved_entry.delete(0, '')
    entry_date_entry.insert(0, entry_d)
    upload_date_entry.insert(0, upload)
    owner_entry_entry.insert(0, selected_entry[3])
    sub_county_combo.set(selected_entry[4])
    plot_no_entry.insert(0, selected_entry[7])
    description_combo.set(selected_entry[5])
    floors_combo.set(selected_entry[6])
    assigned_combo.set(selected_entry[8])
    date_moved_entry.insert(0, moved)
    ref_number_entry.insert(0, selected_entry[11])
    status_combo.set(selected_entry[12])
    Issues_entry.insert(0, selected_entry[13])
    # Remarks_entry.insert(0, selected_entry[14])


    entry_window.mainloop()

def convert_date_format(date_str):

    year, month, day = date_str.split('-')
    formatted_date = f"{month}/{day}/{year}"
    
    return formatted_date

def reconvert(date_str):
        month, day, year = date_str.split('/')
        formatted_date = f"{year}-{month}-{day}"
        return formatted_date

def submit(window):

    from CustomTkinterMessagebox import CTkMessagebox

    #TODO: Deal with time formats for data manipulation
    #TODO: Destroy window,
    #TODO: Have the entry function return data in string format
    global ENTRY
    global entry_date_entry, upload_date_entry, owner_entry_entry, sub_county_combo, plot_no_entry, description_combo, floors_combo, assigned_combo, date_moved_entry, ref_number_entry, status_combo, Issues_entry, Remarks_entry 
    global table

    entry_date = entry_date_entry.get()
    upload_date = upload_date_entry.get()
    owner = owner_entry_entry.get()
    sub_county = sub_county_combo.get()
    plot_no = plot_no_entry.get()
    description = description_combo.get()
    floors = floors_combo.get()
    assigned = assigned_combo.get()
    date_moved = date_moved_entry.get()
    ref_no = ref_number_entry.get()
    status = status_combo.get()
    issues = Issues_entry.get()
    remarks = Remarks_entry.get()

    # print(f"Printing entry_date: {entry_date}")
    # print(f"Printing upload_date: {upload_date}")
    # print(f"Printing owner: {owner}")
    # print(f"Printing sub_county: {sub_county}")
    # print(f"Printing date_moved: {date_moved}")
    # print(f"Printing plot_no: {plot_no}")
    # print(f"Printing description: {description}")
    # print(f"Printing floors: {floors}")
    # print(f"Printing assigned: {assigned}")
    # print(f"Printing status: {status}")
    # print(f"Printing issues: {issues}")
    # print(f"Printing ref_no: {ref_no}")
    # print(f"Printing remarks: {remarks}")

    if len(ENTRY) != 0:
        CTkMessagebox.messagebox(title='WAIT', text='Just a moment, the previous entry is still being logged!', sound='on', button_text='OK')

    if (entry_date == '' or upload_date == '' or owner == '' or
            sub_county == '' or date_moved == '' or plot_no == '' or
            description == '' or floors == '' or assigned == '' or status == '' or issues == '' or ref_no == '' or remarks == ''):
        CTkMessagebox.messagebox(title='Empty Fields', text='Fill all fields!', sound='on', button_text='OK')
        print("Blanks identified")
    else:
        days = days_count(entry_date, date_moved)
        print("Succesfully evaluated")

        new_list = list(ENTRY)
        new_list.append(str(uuid4()))
        new_list.append(save_date(entry_date))
        new_list.append(save_date(upload_date))
        new_list.append(owner)
        new_list.append(sub_county)
        new_list.append(description)
        new_list.append(floors)
        new_list.append(plot_no)
        new_list.append(assigned)
        new_list.append(save_date(date_moved))
        new_list.append(days)
        new_list.append(ref_no)
        new_list.append(status)
        new_list.append(issues)
        new_list.append(remarks)
        ENTRY = tuple(new_list)

        print("Printing all entries")
        print(ENTRY)
    

        window.destroy()

        #insert data into sqlite database
        make_entry(ENTRY)

        successful_entry = list(ENTRY)
        
        while len(successful_entry) > 0:
            successful_entry.pop()

        ENTRY = tuple(successful_entry)
        print("Entry values saved and cleared successfully")
        
        #TODO: Update table data by refreshing
        
        for row in table.get_children():
            table.delete(row)

        row_value = ()

        entries = pull_entries()
        print(entries)

        for entry in entries:
            row_value = (
                    entry[1], entry[2], entry[3], entry[4], entry[5],
                    entry[6], entry[7], entry[8], entry[9], entry[10], entry[11], 
                    entry[12]
                )
            table.insert("", "end", values = row_value)

def edit(pk, window):
    global entry_date_entry, upload_date_entry, owner_entry_entry, sub_county_combo, plot_no_entry, description_combo, floors_combo, assigned_combo, date_moved_entry, ref_number_entry, status_combo, Issues_entry, Remarks_entry

    entry_d = entry_date_entry.get()
    upload_d = upload_date_entry.get()
    moved_d = date_moved_entry.get()

    global ENTRY, table
    connection = sqlite3.connect('activity_log.db')
    with connection:
        connection.execute("""UPDATE log SET entry_date = ?, upload_date = ?, owner = ?, sub_county = ?, description = ?, floors = ?, plot_no = ?, ref_no = ?, assigned = ?, date_moved = ?,days_left = ?, issues = ?, status = ? WHERE id = ?
    """, (reconvert(entry_d), reconvert(upload_d), owner_entry_entry.get(), sub_county_combo.get(), description_combo.get(), floors_combo.get(), plot_no_entry.get(), ref_number_entry.get(), assigned_combo.get(), reconvert(moved_d), days_count(entry_date_entry.get(), date_moved_entry.get()), Issues_entry.get(), status_combo.get(), pk
    ))
        print("Entry updated successfully")
    
    window.destroy()

        #insert data into sqlite database

    successful_entry = list(ENTRY)
    
    while len(successful_entry) > 0:
        successful_entry.pop()

    ENTRY = tuple(successful_entry)
    print("Entry values saved and cleared successfully")
    
    #TODO: Update table data by refreshing
    
    for row in table.get_children():
        table.delete(row)

    row_value = ()

    entries = pull_entries()
    print(entries)

    for entry in entries:
        row_value = (
                    entry[1], entry[2], entry[3], entry[4], entry[5],
                    entry[6], entry[7], entry[8], entry[9], entry[10], entry[11], 
                    entry[12]
                )
        table.insert("", "end", values = row_value)

def delete(pk, window):
    global ENTRY
    delete_entry(pk)
    window.destroy()

    successful_entry = list(ENTRY)
        
    while len(successful_entry) > 0:
        successful_entry.pop()

    ENTRY = tuple(successful_entry)
    print("Entry values saved and cleared successfully")
    
    #TODO: Update table data by refreshing
    
    for row in table.get_children():
        table.delete(row)

    row_value = ()

    entries = pull_entries()
    print(entries)

    for entry in entries:
        row_value = (
                    entry[1], entry[2], entry[3], entry[4], entry[5],
                    entry[6], entry[7], entry[8], entry[9], entry[10], entry[11], 
                    entry[12]
                )
        table.insert("", "end", values = row_value)

def edit_entry(event):
    global table, action, selected_entry
    global entry_date_entry, upload_date_entry, owner_entry_entry, sub_county_combo, plot_no_entry, description_combo, floors_combo, assigned_combo, date_moved_entry, ref_number_entry, status_combo, Issues_entry, Remarks_entry

    action == 'edit'

    selected_row = table.selection()
    if selected_row:
        item_id = selected_row[0]  # Get the first selected item
        item_values = table.item(item_id, "values")
        print("Printing the selected item")
        print(item_values)
        #(0'2024-07-01', 1'2024-07-01', 2'Imani Amani', 3'LIKONI', 4'COMMERCIAL', 5'MEZZANINE2', 6'XXL/CS', 7'ALAN', 8'2024-07-24', 9'23', 10'D/100/1999', 11'APPROVED')

        #SELECT * FROM log WHERE entry_date = "{item_values[0]}" AND upload_date = "{item_values[1]}" AND owner = "{item_values[2]}" AND sub_county = "{item_values[3]}" AND description = "{item_values[4]}" AND floors = "{item_values[5]}" AND plot_no = "{item_values[6]}" AND assigned = "{item_values[7]}" AND date_moved = "{item_values[8]}" AND days_left = "{item_values[9]}" AND ref_no = "{item_values[10]}" AND status = "{item_values[11]}"'
        #TODO: Sort table entry column mix up (plot no and ref_no)
        connection = sqlite3.connect('activity_log.db')
        with connection:
            selected_entry = connection.execute(f'SELECT * FROM log WHERE entry_date = "{item_values[0]}" AND upload_date = "{item_values[1]}" AND owner = "{item_values[2]}" AND sub_county = "{item_values[3]}" AND description = "{item_values[4]}" AND floors = "{item_values[5]}" AND ref_no = "{item_values[10]}" AND assigned = "{item_values[7]}" AND date_moved = "{item_values[8]}" AND days_left = "{item_values[9]}" AND status = "{item_values[11]}"').fetchone()
            print("Printing the entry")
            print(selected_entry)

        detail_window()

            # global ENTRY
            # ENTRY = entry

            # entry_function()
    #on selection, create a list variable of entry values
    # find entry corresponding from the database (where).fetchone()
    # populate the entry fields with the values
        #get treeview id
        #get first value in vlaues[treeview id]
    # update the entry with the new values where id = ID
    #save values to the database
    # pass

def clear():
    global entry_date_entry, upload_date_entry, owner_entry_entry, sub_county_combo, plot_no_entry, description_combo, floors_combo, assigned_combo, date_moved_entry, ref_number_entry, status_combo, Issues_entry, Remarks_entry

    entry_date_entry.delete(0, 'end')
    upload_date_entry.delete(0, 'end')
    owner_entry_entry.delete(0, 'end')
    sub_county_combo.set('')
    plot_no_entry.delete(0, 'end')
    description_combo.set('')
    floors_combo.set('')
    assigned_combo.set('')
    date_moved_entry.delete(0, 'end')
    ref_number_entry.delete(0, 'end')
    status_combo.set('')
    Issues_entry.delete(0, 'end')
    Remarks_entry.delete(0, 'end')

    print("Cleared all fields")

        
def cancel_entry(window):
    window.kill()


def table_page(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    global table, sort, filter_1, filter_2

    frame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')
    frame.columnconfigure((0,1,2,3,4,5,6,7), weight = 1, uniform = 'a')

    cols = [
        "Entry Date",
        "Upload Date",
        "Owner",
        "Sub-County",
        "Description",
        "Floors",
        "Plot No",
        "Assigned",
        "Date Moved",
        "Days Left",
        "Ref No",
        "Status",
    ]


    date = ctk.CTkLabel(
        frame,
        text = '',
        font = ('Helvetica', 20, 'bold'),
    )

    date.grid(
        row = 0,
        column = 0,
    )
    def update_date():
        date.configure(text = todays_date())

    update_date()

    back_button = ctk.CTkButton(
        frame,
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
        column = 7,
    )

    entry_button = ctk.CTkButton(
        frame,
        text = 'New Entry',
        height = 35,
        width = 50,
        bg_color = 'blue',
        fg_color = 'black',
        corner_radius = 10,
        border_width = 3,
        command=lambda: entry_function(),
    )

    entry_button.grid(
        row = 1,
        column = 0,
        # columnspan = 2,
        # sticky = 'news',
    )

    data_frame = ctk.CTkScrollableFrame(
        frame,
        border_width = 1,
        border_color = 'black',
        corner_radius = 0,
    )

    data_frame.grid(
        row = 2,
        column = 0,
        rowspan = 5,
        columnspan = 8,
        sticky = 'news',
    )

    sort_frame = ctk.CTkFrame(
        frame,
        border_width = 0,
        bg_color = 'transparent',
        fg_color = 'transparent',
    )
    sort_frame.grid(
        row = 1,
        column = 4,
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
        command = sort_values,
        # textVariable = 'Sort_by',
    )
    sort.pack()
    # sort.bind("<<ComboboxSelected>>", lambda event: print("Hello, its time to sort"))

    filter_label_frame = tk.LabelFrame(
        frame,
        text = 'Filter',
        font = ('Helvetica', 10),
        height = 60,
        # background = 'blue',
    )
    filter_label_frame.grid(
        row = 1,
        column = 5,
        columnspan = 2,
        sticky = 'news',
        pady = 10,
    )

    filter_label_frame.columnconfigure(0, weight = 1)

    filter_1  = ctk.CTkComboBox(
        filter_label_frame,
        values = cols,
        command = filter_values
    )
    filter_1.set('')
    filter_1.grid(
        row = 0,
        column = 0,
    )

    filter_2 = ctk.CTkComboBox(
        filter_label_frame,
        values = [],
        command = filter_values2
    )
    filter_2.set('')
    filter_2.grid(
        row = 0,
        column = 1,
    )
    #TODO: Add a 'clear rules' button
    clear_button = ctk.CTkButton(
        frame,
        text = 'Clear Rules',
        command = clear_rules,
    )
    clear_button.grid(
        row = 1,
        column = 7,
    )

    table = ttk.Treeview(
        data_frame,
        columns = cols,
        show = 'headings',
        height=30,
    )
    table.heading("Entry Date", text = "Entry Date")
    table.heading("Upload Date", text = "Upload Date")
    table.heading("Owner", text = "Owner")
    table.heading("Sub-County", text = "Sub-County")
    table.heading("Description", text = "Description")
    table.heading("Floors", text = "Floors") 
    table.heading("Plot No", text = "Plot No")   
    table.heading("Assigned", text = "Assigned")
    table.heading("Date Moved", text = "Date Moved")
    table.heading("Days Left", text = "Days Left")
    table.heading("Ref No", text = "Ref No")
    table.heading("Status", text = "Status")
    table.pack(
        fill = 'both',
        expand = True,
    )
    table.bind("<Double-1>", edit_entry)


    row_value = ()

    entries = pull_entries()
    print(entries)

    for entry in entries:
        row_value = (
                entry[1], entry[2], entry[3], entry[4], entry[5],
                entry[6], entry[7], entry[8], entry[9], entry[10], entry[11], 
                entry[12]
            )
        table.insert("", "end", values = row_value)


def sort_values(event):
    from database.database import table_sort
    global sort, table

    print("Hello fro inside the sort")

    sort_by = sort.get()
    values = table_sort(sort_by)

    print(sort_by)

    for row in table.get_children():
            table.delete(row)
        
    for entry in values:
        row_value = (
                entry[1], entry[2], entry[3], entry[4], entry[5],
                entry[6], entry[11], entry[8], entry[9], entry[10], entry[13], 
                entry[12]
            )
        table.insert("", "end", values = row_value)

    print(f"Sorting by {sort_by}")

def filter_values(event):
    from database.database import criteria_values
    global filter_1, filter_2, table, dist_values

    filter_1_value = filter_1.get()
    print(filter_1_value)
    dist_values = criteria_values(filter_1_value)
    print(dist_values)

    filter_2.configure(values = dist_values)

def filter_values2(event):
    from database.database import filter_entries
    global filter_1, filter_2, table

    criteria = filter_1.get()
    filter_value = filter_2.get()
    print(criteria)
    print(filter_value)
    values = filter_entries(criteria, filter_value)
    print("Printing table values")
    print(values)

    for row in table.get_children():
        table.delete(row)
        
    for entry in values:
        row_value = (
                entry[1], entry[2], entry[3], entry[4], entry[5],
                entry[6], entry[11], entry[8], entry[9], entry[10], entry[13], 
                entry[12]
            )
        table.insert("", "end", values = row_value)

def clear_rules():
    global table, sort, filter_1, filter_2

    sort.set('')
    filter_1.set('')
    filter_2.set('')

    for row in table.get_children():
        table.delete(row)

    entries = pull_entries()
    print(entries)

    for entry in entries:
        row_value = (
                entry[1], entry[2], entry[3], entry[4], entry[5],
                entry[6], entry[11], entry[8], entry[9], entry[10], entry[13], 
                entry[12]
            )
        table.insert("", "end", values = row_value)

    filter_1.set('')
    filter_2.set('')

    print("Cleared all rules")

def populate_table(widget, table):
    for row in widget.get_children():
        widget.delete(row)

    values = pull_entries2(table)
    print(values)
    
    for value in values:
        widget.insert("", "end", values = value)

def members(frame):
    import uuid
    #TODO: Clear other widgets in frame
    for widget in frame.winfo_children():
        widget.destroy()
    # del_cols()
    create_all_tables()
    
    frame.rowconfigure((0, 1), weight = 1, uniform = 'a')
    frame.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')
    #Sub county
    sub_county_frame = ctk.CTkFrame(
        frame,

    )
    sub_county_frame.grid(
        row = 0,
        column = 0,
        sticky = 'news',
    )

    sub_county_title = ctk.CTkLabel(
        sub_county_frame,
        text = 'Sub-County',
        text_color = 'black',
    )

    sub_county_title.pack(

    )

    sub_county_table = ttk.Treeview(
        sub_county_frame,
        columns = ['Sub-County'],
        show = 'headings',
    )
    sub_county_table.heading('Sub-County', text = 'Sub-County')
    sub_county_table.pack(
        fill = 'both',
        expand = True,
    )

    add_sub_county_frame = ctk.CTkFrame(
        sub_county_frame,

    )
    add_sub_county_frame.rowconfigure(0, weight = 1)
    add_sub_county_frame.columnconfigure((0, 1), weight = 1)
    add_sub_county_frame.pack()

    sub_county_entry = ctk.CTkEntry(
        add_sub_county_frame,
    )
    sub_county_entry.grid(
        row = 0,
        column = 0,
    )

    sub_county_add_button = ctk.CTkButton(
        add_sub_county_frame,
        text = 'Add',
        command = lambda: make_entry2(sub_county_table, sub_county_entry, sub_county_entry.get(), 'sub_county'),
    )
    sub_county_add_button.grid(
        row = 0,
        column = 1,
    )
    populate_table(sub_county_table, 'sub_county')
    
    #Description
    description_frame = ctk.CTkFrame(
        frame,
    )

    description_frame.grid(
        row = 1,
        column = 0,
        sticky = 'news',
    )

    description_title = ctk.CTkLabel(
        description_frame,
        text = 'Description',
        text_color = 'black',
    )

    description_title.pack(

    )

    description_table = ttk.Treeview(
        description_frame,
        columns = ['Description'],
        show = 'headings',
    )
    description_table.heading('Description', text = 'Description')
    description_table.pack(
        fill = 'both',
        expand = True,
    )

    add_description_frame = ctk.CTkFrame(
        description_frame,

    )
    add_description_frame.rowconfigure(0, weight = 1)
    add_description_frame.columnconfigure((0, 1), weight = 1)
    add_description_frame.pack()

    description_entry = ctk.CTkEntry(
        add_description_frame,
    )
    description_entry.grid(
        row = 0,
        column = 0,
    )

    description_add_button = ctk.CTkButton(
        add_description_frame,
        text = 'Add',
        command = lambda: make_entry2(description_table, description_entry, description_entry.get(), 'description'),
    )
    description_add_button.grid(
        row = 0,
        column = 1,
    )
    populate_table(description_table, 'description')

    #Floors
    floors_frame = ctk.CTkFrame(
        frame,
    )

    floors_frame.grid(
        row = 0,
        column = 1,
        rowspan = 2,
        sticky = 'news',
    )

    floors_title = ctk.CTkLabel(
        floors_frame,
        text = 'Floors',
        text_color = 'black',
    )

    floors_title.pack(

    )

    floors_table = ttk.Treeview(
        floors_frame,
        columns = ['Floors'],
        show = 'headings',
    )
    floors_table.heading('Floors', text = 'Floors')
    floors_table.pack(
        fill = 'both',
        expand = True,
    )

    add_floors_frame = ctk.CTkFrame(
        floors_frame,

    )
    add_floors_frame.rowconfigure(0, weight = 1)
    add_floors_frame.columnconfigure((0, 1), weight = 1)
    add_floors_frame.pack()

    floors_entry = ctk.CTkEntry(
        add_floors_frame,
    )
    floors_entry.grid(
        row = 0,
        column = 0,
    )

    floors_add_button = ctk.CTkButton(
        add_floors_frame,
        text = 'Add',
        command = lambda: make_entry2(floors_table, floors_entry, floors_entry.get(), 'floors'),
    )
    floors_add_button.grid(
        row = 0,
        column = 1,
    )
    populate_table(floors_table, 'floors')

    #Assigned
    assigned_frame = ctk.CTkFrame(
        frame,
    )

    assigned_frame.grid(
        row = 0,
        column = 2,
        sticky = 'news',
    )

    assigned_title = ctk.CTkLabel(
        assigned_frame,
        text = 'Assigned',
        text_color = 'black',
    )

    assigned_title.pack(

    )

    assigned_table = ttk.Treeview(
        assigned_frame,
        columns = ['Assigned'],
        show = 'headings',
    )
    assigned_table.heading('Assigned', text = 'Assigned')
    assigned_table.pack(
        fill = 'both',
        expand = True,
    )

    add_assigned_frame = ctk.CTkFrame(
        assigned_frame,

    )
    add_assigned_frame.rowconfigure(0, weight = 1)
    add_assigned_frame.columnconfigure((0, 1), weight = 1)
    add_assigned_frame.pack()

    assigned_entry = ctk.CTkEntry(
        add_assigned_frame,
    )
    assigned_entry.grid(
        row = 0,
        column = 0,
    )

    assigned_add_button = ctk.CTkButton(
        add_assigned_frame,
        text = 'Add',
        command = lambda: make_entry2(assigned_table, assigned_entry, assigned_entry.get(), 'assigned'),
    )
    assigned_add_button.grid(
        row = 0,
        column = 1,
    )
    populate_table(assigned_table, 'assigned')

    #Status
    status_frame = ctk.CTkFrame(
        frame,

    )

    status_frame.grid(
        row = 1,
        column = 2,
        sticky = 'news',
    )

    status_title = ctk.CTkLabel(
        status_frame,
        text = 'Status',
        text_color = 'black',
    )

    status_title.pack(

    )

    status_table = ttk.Treeview(
        status_frame,
        columns = ['Status'],
        show = 'headings',
    )
    status_table.heading('Status', text = 'Status')
    status_table.pack(
        fill = 'both',
        expand = True,
    )

    add_status_frame = ctk.CTkFrame(
        status_frame,

    )
    add_status_frame.rowconfigure(0, weight = 1)
    add_status_frame.columnconfigure((0, 1), weight = 1)
    add_status_frame.pack()

    status_entry = ctk.CTkEntry(
        add_status_frame,
    )
    status_entry.grid(
        row = 0,
        column = 0,
    )

    status_add_button = ctk.CTkButton(
        add_status_frame,
        text = 'Add',
        command = lambda: make_entry2(status_table, status_entry, status_entry.get(), 'status')
    )
    status_add_button.grid(
        row = 0,
        column = 1,
    )
    populate_table(status_table, 'status')



if __name__ == '__main__':
    table_page()