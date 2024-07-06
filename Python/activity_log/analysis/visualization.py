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
        bg_color = '#faffaf',
        fg_color = '#faffaf',
    )

    m_y_frame.grid(
        row = 0,
        column = 0,
        columnspan = 2,
        pady = 10,
        padx = 10,
        sticky = 'nsew',
    )

    entries_frame = ctk.CTkFrame(
        analytics,
        bg_color = '#faffaf',
        fg_color = '#faffaf',
    )

    entries_frame.grid(
        row = 0,
        column = 2,
        columnspan = 2,
        pady = 10,
        padx = 10,
        sticky = 'nsew',
    )

    approved_frame = ctk.CTkFrame(
        analytics,
        bg_color = '#faffaf',
        fg_color = '#faffaf',
    )

    approved_frame.grid(
        row = 0,
        column = 4,
        columnspan = 2,
        pady = 10,
        padx = 10,
        sticky = 'nsew',
    )

    rejected_frame = ctk.CTkFrame(
        analytics,
        bg_color = '#faffaf',
        fg_color = '#faffaf',
    )

    rejected_frame.grid(
        row = 0,
        column = 6,
        columnspan = 2,
        pady = 10,
        padx = 10,
        sticky = 'nsew',
    )

    pending_frame = ctk.CTkFrame(
        analytics,
        bg_color = '#faffaf',
        fg_color = '#faffaf',
    )

    pending_frame.grid(
        row = 0,
        column = 8,
        columnspan = 2,
        pady = 10,
        padx = 10,
        sticky = 'nsew',
    )

    qualitative_frame = ctk.CTkFrame(
        frame,
    bg_color = '#0f67b1',
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
    
