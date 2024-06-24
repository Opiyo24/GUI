import tkinter as tk
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

    global description_combo, floors_combo, assigned_combo, status_combo, alert_label

    entry_window = ctk.CTk()

    global entry_date, upload_date, owner_entry, sub_county_entry, date_moved, plot_no, description, floors, assigned, status, Issues_entry, ref_no

    entry_date = ctk.StringVar()
    upload_date = ctk.StringVar()
    owner_entry = ctk.StringVar()
    sub_county_entry = ctk.StringVar()
    date_moved = ctk.StringVar()
    plot_no = ctk.StringVar()
    description = ctk.StringVar()
    floors = ctk.StringVar()
    assigned = ctk.StringVar()
    status = ctk.StringVar()
    Issues_entry = ctk.StringVar()
    ref_no = ctk.StringVar()

    entry_window.title('Activity Log | Entry')
    entry_window.iconbitmap('')
    entry_window.geometry('500x900')



    #Entry DAte
    e_date = ctk.CTkLabel(
        entry_window,
        text = 'Entry Date',
    )
    e_date.pack()

    entry_date_entry = DateEntry(
        entry_window,
        selectmode='day',
        date_pattern='m/d/yyyy',
        textvariable=entry_date,
    )
    entry_date_entry.pack()

    #Date of upload
    # u_date = ctk.CTkLabel(
    #     entry_window,
    #     text = 'Date of Upload',
    # )
    # u_date.pack()

    # upload_date_entry = DateEntry(
    #     entry_window,
    #     selectmode='day',
    #     date_pattern='m/d/yyyy',
    #     textvariable=upload_date,
    # )
    # upload_date_entry.pack()

    # #Owner
    # owner_label = ctk.CTkLabel(
    #     entry_window,
    #     text = 'Owner',
    # )
    # owner_label.pack()

    # owner_entry_entry = ctk.CTkEntry(
    #     entry_window,
    #     width = 100,
    #     height = 18,
    #     textvariable=owner_entry,
    # )
    # owner_entry_entry.pack(pady=5)

    # #Sub County
    # sub_county_label = ctk.CTkLabel(
    #     entry_window,
    #     text = 'sub_county',
    # )
    # sub_county_label.pack()

    # sub_county_entry_entry = ctk.CTkEntry(
    #     entry_window,
    #     width = 100,
    #     height = 18,
    #     textvariable=sub_county_entry,
    # )
    # sub_county_entry_entry.pack(pady=5)

    # #Description
    # description_label = ctk.CTkLabel(
    #     entry_window,
    #     text = 'Description',
    # )
    # description_label.pack()

    # description_combo = ctk.CTkComboBox(
    #     entry_window,
    #     width = 150,
    #     height = 18,
    #     values = ['COMMERCIAL', 'RESIDENTIAL', 'MIXED USE', 'INDUSTRIAL', 'INSTITUTIONAL'],

    # )
    # description_combo.pack(pady=5)

    # #Floors
    # floors_label = ctk.CTkLabel(
    #     entry_window,
    #     text = 'Floors',
    # )
    # floors_label.pack()

    # floors_combo = ctk.CTkComboBox(
    #     entry_window,
    #     width = 150,
    #     height = 18,
    #     values = ['G', 'G+1', 'G+2', 'G+3', 'MEZZANINE'],

    # )
    # floors_combo.pack(pady=5)

    # #Assigned

    # assigned_label = ctk.CTkLabel(
    #     entry_window,
    #     text = 'Assigned',
    # )
    # assigned_label.pack()

    # assigned_combo = ctk.CTkComboBox(
    #     entry_window,
    #     width = 150,
    #     height = 18,
    #     values = ['Brian', 'Quincy', 'Sugoi', 'Gabriel', 'Opoyo'],

    # )
    # assigned_combo.pack(pady=5)

    # #Date moved
    # m_date = ctk.CTkLabel(
    #     entry_window,
    #     text = 'Date Moved',
    # )
    # m_date.pack()

    # date_moved_entry = DateEntry(
    #     entry_window,
    #     selectmode='day',
    #     date_pattern='m/d/yyyy',
    #     textvariable=date_moved,
    # )
    # date_moved_entry.pack()

    # #Last follow-up
    # plot_no = ctk.CTkLabel(
    #     entry_window,
    #     text = 'Plot No',
    # )
    # plot_no.pack()

    # plot_no_entry = ctk.CTkEntry(
    #     entry_window,
    #     width = 100,
    #     height = 18,
    #     textvariable=plot_no,
    # )
    # plot_no_entry.pack()


    # #status
    # status_label = ctk.CTkLabel(
    #     entry_window,
    #     text = 'Status',
    # )
    # status_label.pack()

    # status_combo = ctk.CTkComboBox(
    #     entry_window,
    #     width = 150,
    #     height = 18,
    #     values = ['PENDING', 'APPROVED', 'REJECTED', 'REVIEW'],

    # )

    # status_combo.pack(pady=5)

    # #Issues
    # Issues_label = ctk.CTkLabel(
    #     entry_window,
    #     text = 'Issues',
    # )
    # Issues_label.pack()

    # Issues_entry = ctk.CTkEntry(
    #     entry_window,
    #     width = 100,
    #     height = 18,
    #     textvariable = Issues_entry,
    # )
    # Issues_entry.pack(pady=5)

    # #Remarks
    # ref_no_label = ctk.CTkLabel(
    #     entry_window,
    #     text = 'Ref No',
    # )
    # ref_no_label.pack()

    # ref_no_entry = ctk.CTkEntry(
    #     entry_window,
    #     width = 100,
    #     height = 18,
    #     textvariable = ref_no_entry,
    # )
    # ref_no_entry.pack(pady=5)

    submit_button = ctk.CTkButton(
        entry_window,
        text = 'Submit',
        height = 18,
        width = 20,
        command = lambda: submit(entry_window),
    )

    submit_button.pack(pady = 10)

    alert_label = ctk.CTkLabel(
        entry_window,
        text = '',
    )
    alert_label.pack()


    entry_window.mainloop()


def submit(window):
    global ENTRY
    

    if (entry_date.get() == '' or upload_date.get() == '' or owner_entry.get() == '' or
            sub_county_entry.get() == '' or date_moved.get() == '' or plot_no.get() == '' or
            description_combo.get() == '' or floors_combo.get() == '' or assigned_combo.get() == '' or status_combo.get() == ''):
        alert_label.configure(text='All fields are required', text_color='red')
    else:
        days = days_count(entry_date.get(), date_moved.get())
        # print(days)

        new_list = list(ENTRY)
        new_list.append(str(uuid4()))
        new_list.append(save_date(entry_date.get()))
        new_list.append(save_date(upload_date.get()))
        new_list.append(owner_entry.get())
        new_list.append(sub_county_entry.get())
        new_list.append(description_combo.get())
        new_list.append(floors_combo.get())
        new_list.append(Issues_entry.get())
        new_list.append(assigned_combo.get())
        new_list.append(save_date(date_moved.get()))
        new_list.append(days)
        new_list.append(save_date(plot_no.get()))
        new_list.append(status_combo.get())
        new_list.append(ref_no.get())
        ENTRY = tuple(new_list)
        # print(ENTRY)

        window.destroy()

        #insert data into sqlite database
        make_entry(ENTRY)



def table_page():
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

    for entry in entries:
        row_value = (
                entry[1], entry[2], entry[3], entry[4], entry[5],
                entry[6], entry[7], entry[8], entry[9], entry[10], entry[11], 
                entry[12]
            )
        table.insert("", "end", values = row_value)

    window.mainloop()

if __name__ == '__main__':
    table_page()





