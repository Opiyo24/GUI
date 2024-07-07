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

    yearly_frame.grid(
        row = 1,
        column = 0,
        rowspan = 8,
        columnspan = 5,
        pady = 20,
        padx = 20,
        sticky = 'nsew',
    )
    
    average_frame = ctk.CTkFrame(
        qualitative_frame,
        border_color = 'black',
        border_width = 5,
    )

    average_frame.grid(
        row = 0,
        column = 6,
        rowspan = 4,
        columnspan = 4,
        pady = 10,
        padx = 10,
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

    sub_county_frame.grid(
        row = 0,
        column = 11,
        rowspan = 10,
        columnspan = 6,
        pady = 10,
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
        font = ('Arial', 60),
        text_color = 'black',
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
        font = ('Arial', 60),
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
        font = ('Arial', 60),
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
        font = ('Arial', 60),
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
    first_year.pack(
        # anchor = 'nw',
    )

    label1 = ctk.CTkLabel(
        yearly_frame,
        text = '',
        height = 50,
    )
    label1.pack()

    second_year = ctk.CTkFrame(
        yearly_frame,
        border_color = 'black',
        fg_color = 'white',
        border_width = 1,
    )
    second_year.pack(
    )