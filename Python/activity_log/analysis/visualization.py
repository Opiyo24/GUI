import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from customtkinter import *

def dashboard(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    global table, sort, filter_1, filter_2

    frame.columnconfigure((0,1,2,3,4,5,6,7), weight = 1, uniform = 'a')
    frame.rowconfigure((0,1,2,3,4,5,6), weight = 1, uniform = 'a')

    analytics = ctk.CTkFrame(
        frame,
        # border_color = 'black',
        # border_width = 5,
        bg_color = '#3fa2f6',
        fg_color = '#3fa2f6',
    )
    analytics.rowconfigure(0, weight = 1)
    analytics.columnconfigure((0 ,1, 2, 3, 4, 5, 6, 7, 8, 9), weight = 1, uniform = 'a')

    analytics.grid(
        row = 0,
        column = 0,
        rowspan = 1,
        columnspan = 8,
        sticky = 'nsew',
    )

    m_y_frame = ctk.CTkFrame(
        analytics,
        fg_color = '#f6f5f5',
        border_width = 1,
        border_color = '#686d76',
        corner_radius = 20,
    )

    m_y_frame.rowconfigure((0, 1), weight = 1, uniform = 'a')
    
    m_y_frame.grid(
        row = 0,
        column = 0,
        columnspan = 2,
        pady = 2,
        padx = 10,
        sticky = 'nsew',
    )

    entries_frame = ctk.CTkFrame(
        analytics,
        fg_color = '#f6f5f5',
        border_width = 1,
        border_color = '#686d76',
        corner_radius = 20,
    )

    entries_frame.grid(
        row = 0,
        column = 2,
        columnspan = 2,
        pady = 2,
        padx = 20,
        sticky = 'nsew',
    )

    approved_frame = ctk.CTkFrame(
        analytics,
        fg_color = '#f6f5f5',
        border_width = 1,
        border_color = '#686d76',
        corner_radius = 20,
    )

    approved_frame.grid(
        row = 0,
        column = 4,
        columnspan = 2,
        pady = 2,
        padx = 20,
        sticky = 'nsew',
    )

    pending_frame = ctk.CTkFrame(
        analytics,
        fg_color = '#f6f5f5',
        border_width = 1,
        border_color = '#686d76',
        corner_radius = 20,
    )

    pending_frame.grid(
        row = 0,
        column = 6,
        columnspan = 2,
        pady = 2,
        padx = 20,
        sticky = 'nsew',
    )
    
    rejected_frame = ctk.CTkFrame(
        analytics,
        fg_color = '#f6f5f5',
        border_width = 1,
        border_color = '#686d76',
        corner_radius = 20,
    )

    rejected_frame.grid(
        row = 0,
        column = 8,
        columnspan = 2,
        pady = 2,
        padx = 20,
        sticky = 'nsew',
    )

    qualitative_frame = ctk.CTkFrame(
        frame,
        fg_color = '#0f67b1',
    )

    qualitative_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight = 1, uniform = 'a')
    qualitative_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19), weight = 1, uniform = 'a')

    qualitative_frame.grid(
        row = 1,
        column = 0,
        rowspan = 6,
        columnspan = 8,
        sticky = 'nsew',
    
    )

    yearly_frame = ctk.CTkFrame(
        qualitative_frame,
        border_color = 'black',
        border_width = 5,
    )

    yearly_frame.columnconfigure((0, 1), weight = 1, uniform = 'a')
    yearly_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight = 1, uniform = 'a')

    yearly_frame.grid(
        row = 0,
        column = 0,
        rowspan = 8,
        columnspan = 5,
        pady = 20,
        padx = 20,
        sticky = 'nsew',
    )
    
    average_frame = ctk.CTkFrame(
        qualitative_frame,
        border_color = '#686a68',
        border_width = 3,
        fg_color = '#f7f9f2',
        corner_radius = 30,
    )

    average_frame.grid(
        row = 0,
        column = 6,
        rowspan = 4,
        columnspan = 4,
        pady = 20,
        padx = 20,
        sticky = 'nsew',
    )

    description_frame = ctk.CTkFrame(
        qualitative_frame,
        border_color = 'black',
        border_width = 5,
    )

    description_frame.grid(
        row = 5,
        column = 6,
        rowspan = 5,
        columnspan = 4,
        pady = 10,
        padx = 10,
        sticky = 'nsew',
    )

    sub_county_frame = ctk.CTkFrame(
        qualitative_frame,
        border_color = 'black',
        border_width = 5,
    )

    sub_county_frame.columnconfigure((0, 1), weight = 1, uniform = 'a')
    sub_county_frame.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22), weight = 1, uniform = 'a')

    sub_county_frame.grid(
        row = 0,
        column = 11,
        rowspan = 10,
        columnspan = 6,
        padx = 10,
        sticky = 'nsew',
    )

    floors_frame = ctk.CTkFrame(
        qualitative_frame,
        border_color = 'black',
        border_width = 5,
    )

    floors_frame.grid(
        row = 0,
        column = 17,
        rowspan = 10,
        columnspan = 3,
        pady = 10,
        padx = 10,
        sticky = 'nsew',
    )
    
    selected_month = ctk.CTkComboBox(
        m_y_frame,
        values = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        height = 30,
        width = 50,
    )

    selected_month.grid(
        row = 0,
        column = 0,
        pady = 10,
        padx = 20,
        sticky = 'nsew',
    )

    selected_year = ctk.CTkComboBox(
        m_y_frame,
        values = ['2021', '2022', '2023', '2024', '2025'],
        height = 30,
    )

    selected_year.grid(
        row = 1,
        column = 0,
        pady = 10,
        padx = 20,
        sticky = 'nsew',
    )

    entries = ctk.CTkLabel(
        entries_frame,
        height = 70,
        text = '101',
        font = ('Arial', 60, 'bold'),
        text_color = '#191a19',
    )

    entries.pack(
        anchor = 'nw',
        padx = 20,
    )

    entries_description = ctk.CTkLabel(
        entries_frame,
        text = 'Total entries made',
        font = ('Arial', 15),
        text_color = 'black',
    )

    entries_description.pack(
        anchor = 'se',
        padx = 10,
    )

    approved_entries = ctk.CTkLabel(
        approved_frame,
        height = 70,
        text = '70',
        font = ('Arial', 60, 'bold'),
        text_color = '#05e61f',
    )

    approved_entries.pack(
        anchor = 'nw',
        padx = 20,
    )

    approved_entries_description = ctk.CTkLabel(
        approved_frame,
        text = 'Number of approved entries.',
        font = ('Arial', 15),
        text_color = 'black',
    )

    approved_entries_description.pack(
        anchor = 'se',
        padx = 10,
    )

    pending_entries = ctk.CTkLabel(
        pending_frame,
        height = 70,
        text = '10',
        font = ('Arial', 60, 'bold'),
        text_color = '#686a68',
    )

    pending_entries.pack(
        anchor = 'nw',
        padx = 20,
    )

    pending_entries_description = ctk.CTkLabel(
        pending_frame,
        text = 'Number of pending entries.',
        font = ('Arial', 15),
        text_color = 'black',
    )

    pending_entries_description.pack(
        anchor = 'se',
        padx = 10,
    )

    rejected_entries = ctk.CTkLabel(
        rejected_frame,
        height = 70,
        text = '20',
        font = ('Arial', 60, 'bold'),
        text_color = '#f50505',
    )

    rejected_entries.pack(
        anchor = 'nw',
        padx = 20,
    )

    rejected_entries_description = ctk.CTkLabel(
        rejected_frame,
        text = 'Number of rejected entries.',
        font = ('Arial', 15),
        text_color = 'black',
    )

    rejected_entries_description.pack(
        anchor = 'se',
        padx = 10,
    )

    first_year = ctk.CTkFrame(
        yearly_frame,
        border_color = 'black',
        fg_color = 'white',
        border_width = 1,
    )

    first_year.rowconfigure((0, 1, 2, 3), weight = 1, uniform = 'a')
    first_year.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')

    first_year.grid(
        row = 1,
        column = 0,
        pady = 10,
        padx = 10,
        columnspan = 2,
        rowspan = 4,
        sticky = 'news',
    )

    label1 = ctk.CTkLabel(
        yearly_frame,
        text = '',
        height = 50,
    )
    label1.grid(
        row = 5,
        column = 0,
        rowspan = 1,
        columnspan = 2,
        sticky = 'news',
    )

    second_year = ctk.CTkFrame(
        yearly_frame,
        border_color = 'black',
        fg_color = 'white',
        border_width = 1,
    )

    second_year.rowconfigure((0, 1, 2, 3), weight = 1, uniform = 'a')
    second_year.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')

    second_year.grid(
        row = 6,
        column = 0,
        rowspan = 4,
        columnspan = 2,
        sticky = 'news',
    )

    analysis_label = ctk.CTkLabel(
        yearly_frame,
        text = 'Yearly Analysis',
        font = ('Arial', 20, 'bold'),
        fg_color = 'black',
    )

    analysis_label.grid(
        row = 0,
        column = 0,
        columnspan = 2,
        sticky = 'ew',
    )

    #FIRST YEAR
    #label
    first_year_label = ctk.CTkLabel(
        first_year,
        text = '2021',
        text_color = '#f7f9f2',
        font = ('Arial', 95),
        fg_color = '#191a19',
    )

    first_year_label.grid(
        row = 0,
        column = 0,
        rowspan = 3,
        columnspan = 2,
        sticky = 'news',
    )

    #approved
    first_year_approved = ctk.CTkLabel(
        first_year,
        text = '70',
        text_color = '#05e61f',
        font = ('Arial', 24, 'bold'),
        fg_color = '#f7f9f2',
    )

    first_year_approved.grid(
        row = 0,
        column = 2,
        sticky = 'news',
    )
    #pending
    first_year_pending = ctk.CTkLabel(
        first_year,
        text = '10',
        text_color = '#686a68',
        font = ('Arial', 24, 'bold'),
        fg_color = '#f7f9f2',
    )

    first_year_pending.grid(
        row = 1,
        column = 2,
        sticky = 'news',
    )

    #rejected
    first_year_rejected = ctk.CTkLabel(
        first_year,
        text = '10',
        text_color = '#f50505',
        font = ('Arial', 24, 'bold'),
        fg_color = '#f7f9f2',
    )

    first_year_rejected.grid(
        row = 2,
        column = 2,
        sticky = 'news',
    )

    #entries
    first_year_entries = ctk.CTkLabel(
        first_year,
        text = '90',
        text_color = '#191a19',
        font = ('Arial', 40, 'bold'),
        fg_color = '#f7f9f2',
    )

    first_year_entries.grid(
        row = 3,
        column = 0,
        sticky = 'news',
    )

    #percentage
    first_year_percentage = ctk.CTkLabel(
        first_year,
        text = '40%',
        text_color = '#191a19',
        font = ('Arial', 25, 'bold'),
        fg_color = '#f7f9f2',
    )

    first_year_percentage.grid(
        row = 3,
        column = 1,
        sticky = 'news',
    )

    #empty label
    first_year_empty = ctk.CTkLabel(
        first_year,
        text = '',
        bg_color = '#191a19',
        fg_color = '#191a19',
    )

    first_year_empty.grid(
        row = 3,
        column = 2,
        sticky = 'news',
    )


    #SECOND YEAR
    #label
    second_year_label = ctk.CTkLabel(
        second_year,
        text = '2022',
        text_color = '#f7f9f2',
        font = ('Arial', 95),
        fg_color = '#191a19',
    )

    second_year_label.grid(
        row = 0,
        column = 0,
        rowspan = 3,
        columnspan = 2,
        sticky = 'news',
    )

    #approved
    second_year_approved = ctk.CTkLabel(
        second_year,
        text = '70',
        text_color = '#05e61f',
        font = ('Arial', 24, 'bold'),
        fg_color = '#f7f9f2',
    )

    second_year_approved.grid(
        row = 0,
        column = 2,
        sticky = 'news',
    )
    #pending
    second_year_pending = ctk.CTkLabel(
        second_year,
        text = '10',
        text_color = '#686a68',
        font = ('Arial', 24, 'bold'),
        fg_color = '#f7f9f2',
    )

    second_year_pending.grid(
        row = 1,
        column = 2,
        sticky = 'news',
    )

    #rejected
    second_year_rejected = ctk.CTkLabel(
        second_year,
        text = '10',
        text_color = '#f50505',
        font = ('Arial', 24, 'bold'),
        fg_color = '#f7f9f2',
    )

    second_year_rejected.grid(
        row = 2,
        column = 2,
        sticky = 'news',
    )

    #entries
    second_year_entries = ctk.CTkLabel(
        second_year,
        text = '90',
        text_color = '#191a19',
        font = ('Arial', 40, 'bold'),
        fg_color = '#f7f9f2',
    )

    second_year_entries.grid(
        row = 3,
        column = 0,
        sticky = 'news',
    )

    #percentage
    second_year_percentage = ctk.CTkLabel(
        second_year,
        text = '40%',
        text_color = '#191a19',
        font = ('Arial', 25, 'bold'),
        fg_color = '#f7f9f2',
    )

    second_year_percentage.grid(
        row = 3,
        column = 1,
        sticky = 'news',
    )

    #empty label
    second_year_empty = ctk.CTkLabel(
        second_year,
        text = '',
        bg_color = '#191a19',
        fg_color = '#191a19',
    )

    second_year_empty.grid(
        row = 3,
        column = 2,
        sticky = 'news',
    )

    #AVERAGE FRAME
    average = ctk.CTkLabel(
        average_frame,
        text = '23',
        text_color = '#191a19',
        font = ('Arial', 110),
    )

    average.pack(
        anchor = 'nw',
        pady = 10,
        padx = 10,
    )

    average_description = ctk.CTkLabel(
        average_frame,
        text = 'Average days in system.',
        font = ('Arial', 15),
        text_color = 'black',
    )

    average_description.pack(
        anchor = 'se',
        pady = 10,
        padx = 10,
    )



### SUB COUNTIES

    ###CHANGAMWE
    Changamwe = ctk.CTkFrame(
        sub_county_frame,
        border_color = '#686a68',
        fg_color = '#faf6f0',
        border_width = 2,
        corner_radius = 20,
    )

    Changamwe.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')
    Changamwe.rowconfigure((0, 1, 2), weight = 1, uniform = 'a')

    Changamwe.grid(
        row = 0,
        column = 0,
        rowspan = 3,
        columnspan = 2,
        sticky = 'news',
    )

    Changamwe_name = ctk.CTkLabel(
        Changamwe,
        text = 'Changamwe',
        text_color = '#191a19',
        font = ('Arial', 25, 'bold'),
        fg_color = '#f7f9f2',
    )

    Changamwe_name.grid(
        row = 0,
        column = 0,
        columnspan = 7,
        rowspan = 2,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Changamwe_entries = ctk.CTkLabel(
        Changamwe,
        text = '10',
        text_color = 'black',
        font = ('Arial', 25, 'bold'),
    )

    Changamwe_entries.grid(
        row = 2,
        column = 0,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Changamwe_percentage = ctk.CTkLabel(
        Changamwe,
        text = '10%',
        text_color = 'black',
        font = ('Arial', 15, 'bold'),
    )

    Changamwe_percentage.grid(
        row = 2,
        column = 1,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Changamwe_approved = ctk.CTkLabel(
        Changamwe,
        text = '10',
        text_color = '#05e61f',
        font = ('Arial', 20),
    )

    Changamwe_approved.grid(
        row = 2,
        column = 4,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Changamwe_pending = ctk.CTkLabel(
        Changamwe,
        text = '10',
        text_color = '#686a68',
        font = ('Arial', 20),
    )

    Changamwe_pending.grid(
        row = 2,
        column = 5,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Changamwe_rejected = ctk.CTkLabel(
        Changamwe,
        text = '10',
        text_color = '#f50505',
        font = ('Arial', 20),
    )

    Changamwe_rejected.grid(
        row = 2,
        column = 6,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    ###JOMVU
    Jomvu = ctk.CTkFrame(
        sub_county_frame,
        border_color = '#686a68',
        fg_color = '#faf6f0',
        border_width = 2,
        corner_radius = 20,
    )

    Jomvu.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')
    Jomvu.rowconfigure((0, 1, 2), weight = 1, uniform = 'a')

    Jomvu.grid(
        row = 4,
        column = 0,
        rowspan = 3,
        columnspan = 2,
        sticky = 'news',
    )

    Jomvu_name = ctk.CTkLabel(
        Jomvu,
        text = 'Jomvu',
        text_color = '#191a19',
        font = ('Arial', 25, 'bold'),
        fg_color = '#f7f9f2',
    )

    Jomvu_name.grid(
        row = 0,
        column = 0,
        columnspan = 7,
        rowspan = 2,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Jomvu_entries = ctk.CTkLabel(
        Jomvu,
        text = '10',
        text_color = 'black',
        font = ('Arial', 25, 'bold'),
    )

    Jomvu_entries.grid(
        row = 2,
        column = 0,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Jomvu_percentage = ctk.CTkLabel(
        Jomvu,
        text = '10%',
        text_color = 'black',
        font = ('Arial', 15, 'bold'),
    )

    Jomvu_percentage.grid(
        row = 2,
        column = 1,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Jomvu_approved = ctk.CTkLabel(
        Jomvu,
        text = '10',
        text_color = '#05e61f',
        font = ('Arial', 20),
    )

    Jomvu_approved.grid(
        row = 2,
        column = 4,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Jomvu_pending = ctk.CTkLabel(
        Jomvu,
        text = '10',
        text_color = '#686a68',
        font = ('Arial', 20),
    )

    Jomvu_pending.grid(
        row = 2,
        column = 5,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Jomvu_rejected = ctk.CTkLabel(
        Jomvu,
        text = '10',
        text_color = '#f50505',
        font = ('Arial', 20),
    )

    Jomvu_rejected.grid(
        row = 2,
        column = 6,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    ###KISAUNI
    Kisauni = ctk.CTkFrame(
        sub_county_frame,
        border_color = '#686a68',
        fg_color = '#faf6f0',
        border_width = 2,
        corner_radius = 20,
    )

    Kisauni.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')
    Kisauni.rowconfigure((0, 1, 2), weight = 1, uniform = 'a')

    Kisauni.grid(
        row = 8,
        column = 0,
        rowspan = 3,
        columnspan = 2,
        sticky = 'news',
    )

    Kisauni_name = ctk.CTkLabel(
        Kisauni,
        text = 'Kisauni',
        text_color = '#191a19',
        font = ('Arial', 25, 'bold'),
        fg_color = '#f7f9f2',
    )

    Kisauni_name.grid(
        row = 0,
        column = 0,
        columnspan = 7,
        rowspan = 2,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Kisauni_entries = ctk.CTkLabel(
        Kisauni,
        text = '10',
        text_color = 'black',
        font = ('Arial', 25, 'bold'),
    )

    Kisauni_entries.grid(
        row = 2,
        column = 0,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Kisauni_percentage = ctk.CTkLabel(
        Kisauni,
        text = '10%',
        text_color = 'black',
        font = ('Arial', 15, 'bold'),
    )

    Kisauni_percentage.grid(
        row = 2,
        column = 1,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Kisauni_approved = ctk.CTkLabel(
        Kisauni,
        text = '10',
        text_color = '#05e61f',
        font = ('Arial', 20),
    )

    Kisauni_approved.grid(
        row = 2,
        column = 4,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Kisauni_pending = ctk.CTkLabel(
        Kisauni,
        text = '10',
        text_color = '#686a68',
        font = ('Arial', 20),
    )

    Kisauni_pending.grid(
        row = 2,
        column = 5,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Kisauni_rejected = ctk.CTkLabel(
        Kisauni,
        text = '10',
        text_color = '#f50505',
        font = ('Arial', 20),
    )

    Kisauni_rejected.grid(
        row = 2,
        column = 6,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    ##Likoni
    Likoni = ctk.CTkFrame(
        sub_county_frame,
        border_color = '#686a68',
        fg_color = '#faf6f0',
        border_width = 2,
        corner_radius = 20,
    )

    Likoni.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')
    Likoni.rowconfigure((0, 1, 2), weight = 1, uniform = 'a')

    Likoni.grid(
        row = 12,
        column = 0,
        rowspan = 3,
        columnspan = 2,
        sticky = 'news',
    )

    Likoni_name = ctk.CTkLabel(
        Likoni,
        text = 'Likoni',
        text_color = '#191a19',
        font = ('Arial', 25, 'bold'),
        fg_color = '#f7f9f2',
    )

    Likoni_name.grid(
        row = 0,
        column = 0,
        columnspan = 7,
        rowspan = 2,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Likoni_entries = ctk.CTkLabel(
        Likoni,
        text = '10',
        text_color = 'black',
        font = ('Arial', 25, 'bold'),
    )

    Likoni_entries.grid(
        row = 2,
        column = 0,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Likoni_percentage = ctk.CTkLabel(
        Likoni,
        text = '10%',
        text_color = 'black',
        font = ('Arial', 15, 'bold'),
    )

    Likoni_percentage.grid(
        row = 2,
        column = 1,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Likoni_approved = ctk.CTkLabel(
        Likoni,
        text = '10',
        text_color = '#05e61f',
        font = ('Arial', 20),
    )

    Likoni_approved.grid(
        row = 2,
        column = 4,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Likoni_pending = ctk.CTkLabel(
        Likoni,
        text = '10',
        text_color = '#686a68',
        font = ('Arial', 20),
    )

    Likoni_pending.grid(
        row = 2,
        column = 5,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Likoni_rejected = ctk.CTkLabel(
        Likoni,
        text = '10',
        text_color = '#f50505',
        font = ('Arial', 20),
    )

    Likoni_rejected.grid(
        row = 2,
        column = 6,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    ##Mvita
    Mvita = ctk.CTkFrame(
        sub_county_frame,
        border_color = '#686a68',
        fg_color = '#faf6f0',
        border_width = 2,
        corner_radius = 20,
    )

    Mvita.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')
    Mvita.rowconfigure((0, 1, 2), weight = 1, uniform = 'a')

    Mvita.grid(
        row = 16,
        column = 0,
        rowspan = 3,
        columnspan = 2,
        sticky = 'news',
    )

    Mvita_name = ctk.CTkLabel(
        Mvita,
        text = 'Mvita',
        text_color = '#191a19',
        font = ('Arial', 25, 'bold'),
        fg_color = '#f7f9f2',
    )

    Mvita_name.grid(
        row = 0,
        column = 0,
        columnspan = 7,
        rowspan = 2,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Mvita_entries = ctk.CTkLabel(
        Mvita,
        text = '10',
        text_color = 'black',
        font = ('Arial', 25, 'bold'),
    )

    Mvita_entries.grid(
        row = 2,
        column = 0,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Mvita_percentage = ctk.CTkLabel(
        Mvita,
        text = '10%',
        text_color = 'black',
        font = ('Arial', 15, 'bold'),
    )

    Mvita_percentage.grid(
        row = 2,
        column = 1,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Mvita_approved = ctk.CTkLabel(
        Mvita,
        text = '10',
        text_color = '#05e61f',
        font = ('Arial', 20),
    )

    Mvita_approved.grid(
        row = 2,
        column = 4,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Mvita_pending = ctk.CTkLabel(
        Mvita,
        text = '10',
        text_color = '#686a68',
        font = ('Arial', 20),
    )

    Mvita_pending.grid(
        row = 2,
        column = 5,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Mvita_rejected = ctk.CTkLabel(
        Mvita,
        text = '10',
        text_color = '#f50505',
        font = ('Arial', 20),
    )

    Mvita_rejected.grid(
        row = 2,
        column = 6,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    ##Nyali
    Nyali = ctk.CTkFrame(
        sub_county_frame,
        border_color = '#686a68',
        fg_color = '#faf6f0',
        border_width = 2,
        corner_radius = 20,
    )

    Nyali.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight = 1, uniform = 'a')
    Nyali.rowconfigure((0, 1, 2), weight = 1, uniform = 'a')

    Nyali.grid(
        row = 20,
        column = 0,
        rowspan = 3,
        columnspan = 2,
        sticky = 'news',
    )

    Nyali_name = ctk.CTkLabel(
        Nyali,
        text = 'Nyali',
        text_color = '#191a19',
        font = ('Arial', 25, 'bold'),
        fg_color = '#f7f9f2',
    )

    Nyali_name.grid(
        row = 0,
        column = 0,
        columnspan = 7,
        rowspan = 2,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Nyali_entries = ctk.CTkLabel(
        Nyali,
        text = '10',
        text_color = 'black',
        font = ('Arial', 25, 'bold'),
    )

    Nyali_entries.grid(
        row = 2,
        column = 0,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Nyali_percentage = ctk.CTkLabel(
        Nyali,
        text = '10%',
        text_color = 'black',
        font = ('Arial', 15, 'bold'),
    )

    Nyali_percentage.grid(
        row = 2,
        column = 1,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Nyali_approved = ctk.CTkLabel(
        Nyali,
        text = '10',
        text_color = '#05e61f',
        font = ('Arial', 20),
    )

    Nyali_approved.grid(
        row = 2,
        column = 4,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Nyali_pending = ctk.CTkLabel(
        Nyali,
        text = '10',
        text_color = '#686a68',
        font = ('Arial', 20),
    )

    Nyali_pending.grid(
        row = 2,
        column = 5,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )

    Nyali_rejected = ctk.CTkLabel(
        Nyali,
        text = '10',
        text_color = '#f50505',
        font = ('Arial', 20),
    )

    Nyali_rejected.grid(
        row = 2,
        column = 6,
        sticky = 'news',
        pady = 5,
        padx = 10,
    )
