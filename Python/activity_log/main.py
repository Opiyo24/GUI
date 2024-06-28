from tkinter import *
import sqlite3
import customtkinter as ctk

# from utils.functions import *
# from views.login import login_page
# from views.signin import signin
from auth.authentication import User, is_authenticated, user_authenticated
from views.table_page import table_page
from database.database import *

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')

color1 = ''
color2 = ''
color3 = ''



window1 = ctk.CTk()
window1.title('Activity Log')
window1.eval("tk::PlaceWindow . center")
window1.minsize(900, 450)

window1.columnconfigure((0), weight = 1, uniform = 'a')
window1.rowconfigure((0), weight = 1, uniform = 'a')


frame2 = ctk.CTkFrame(window1, width = 1600, height = 800)
frame = ctk.CTkFrame(window1, width = 1000, height = 450)
frame.pack(expand=True, fill='both')

username = StringVar()
password = StringVar()
# warning = StringVar()

def validate():
    # conn = sqlite3.connect('activity_log.db')
    # cursor = conn.cursor()

    if is_authenticated(username, my_label, password):
        window1.destroy()
        # create_entry_table(conn)
        # table_page()
        window = ctk.CTk()

        window.title('Activity Log')
        window.iconbitmap('')
        window.geometry('1600x800')
        window.minsize(1600, 800)

        window.columnconfigure((0,1,2,3,4,5,6,7,8), weight = 1, uniform = 'a')
        window.rowconfigure((0,1,2,3,4,5,6), weight = 1, uniform = 'a')

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

my_label = ctk.CTkLabel(
    frame,
    text = '',
    font = ('Helvetica', 20),
)
my_label.pack(pady=40)

name_entry = ctk.CTkEntry(
    frame,
    placeholder_text = 'Username',
    height = 30,
    width = 300,
    corner_radius = 5,
    textvariable=username,
)
name_entry.pack(pady = 10)

password_entry = ctk.CTkEntry(
    frame,
    placeholder_text = 'Password',
    width = 300,
    height = 30,
    corner_radius = 5,
    textvariable=password,
)
password_entry.pack(pady=10)

login_button = ctk.CTkButton(
    frame,
    text = 'Login',
    height = 30,
    width = 80,
    command=lambda: validate(),
)
login_button.pack(pady = 20)

my_label = ctk.CTkLabel(
    frame,
    text = '',
    font = ('Helvetica', 20),
)
my_label.pack(pady=40)

print(user_authenticated)



window1.mainloop()