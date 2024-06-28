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


ENTRY = ()

def entry_function():

    global ENTRY
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


#TODO: Style the entry window with place  
#Entry DAte
    entry_frame = ctk.CTkFrame(
        entry_window,
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
        values = ['', 'CHANGAMWE', 'JOMVU', 'KISAUNI', 'NYALI', 'LIKONI', 'MVITA'],
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
        values = ['', 'COMMERCIAL', 'RESIDENTIAL', 'MIXED USE', 'INDUSTRIAL', 'INSTITUTIONAL'],

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
        values = ['', 'G', 'G+1', 'G+2', 'G+3', 'MEZZANINE'],

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
        values = ['', 'Brian', 'Quincy', 'Sugut', 'Gabriel', 'Opoyo'],

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
        values = ['', 'PENDING', 'APPROVED', 'REJECTED', 'REVIEW'],
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
    cancel_button.pack(padx = 2,
                    pady = 30)

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
        new_list.append(issues)
        new_list.append(assigned)
        new_list.append(save_date(date_moved))
        new_list.append(days)
        new_list.append(plot_no)
        new_list.append(status)
        new_list.append(ref_no)
        ENTRY = tuple(new_list)

        print("Printing all entries")
        print(ENTRY)
    

        window.destroy()

        #insert data into sqlite database
        make_entry(ENTRY)
        #TODO: Update table data by refreshing
        
        for row in table.get_children():
            table.delete(row)

        row_value = ()

        entries = pull_entries()
        print(entries)

        for entry in entries:
            row_value = (
                    entry[1], entry[2], entry[3], entry[4], entry[5],
                    entry[6], entry[11], entry[8], entry[9], entry[10], entry[13], 
                    entry[12]
                )
            table.insert("", "end", values = row_value)


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


def table_page():
    
    window = ctk.CTk()

    global table, sort

    sort_by = ctk.StringVar()

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
        "Plot No",
        "Assigned",
        "Date Moved",
        "Days Left",
        "Ref No",
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
        command=lambda: entry_function(),
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
        command = sort_values,
        # textVariable = 'Sort_by',
    )
    sort.pack()
    # sort.bind("<<ComboboxSelected>>", lambda event: print("Hello, its time to sort"))

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


    row_value = ()

    entries = pull_entries()
    print(entries)

    for entry in entries:
        row_value = (
                entry[1], entry[2], entry[3], entry[4], entry[5],
                entry[6], entry[11], entry[8], entry[9], entry[10], entry[13], 
                entry[12]
            )
        table.insert("", "end", values = row_value)

    window.mainloop()

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

if __name__ == '__main__':
    table_page()





