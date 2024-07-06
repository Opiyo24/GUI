from tkinter import *
import sqlite3
import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image

# from utils.functions import *
# from views.login import login_page
# from views.signin import signin
from auth.authentication import User, is_authenticated, user_authenticated
from views.table_page import *
from database.database import *
from utils.functions import *
from analysis.visualization import *

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')




window1 = ctk.CTk()
window1.title('Activity Log')
# window1.eval("tk::PlaceWindow . center")
window1.minsize(900, 600)
window1.maxsize(900, 600)

window1.columnconfigure((0, 1), weight = 1, uniform = 'a')
window1.rowconfigure((0), weight = 1, uniform = 'a')


# frame2 = ctk.CTkFrame(window1, width = 1600, height = 800)
# frame = ctk.CTkFrame(window1, width = 1000, height = 450)
# frame.pack(expand=True, fill='both')

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
            fg_color = '#142d4d',
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
            fg_color = '#979ca0',
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
            command = lambda: table_page(main_frame)
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
            command = lambda: dashboard(main_frame)
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
            command = lambda: members(main_frame)
        )
        m_button3.pack(
            fill = 'x',
            padx = 1,
            pady = 4,
        )
        window.mainloop()

background_frame = ctk.CTkFrame(
    window1,
    border_width = 0,
    bg_color = '#023047',
    fg_color = '#023047'
)

background_frame.grid(
    row = 0,
    column = 0,
    pady = 0,
    padx = 0,
    sticky = 'news',
)

image_path = 'images/login_image.png'
background_image = load_image(image_path, 455, 605)

canvas = ctk.CTkCanvas(
    background_frame,
    width = 450,
    height = 300,
)
canvas.pack(
    fill = 'both',
    expand = True,
)

canvas.create_image(
    0,
    0,
    anchor = 'nw',
    image = background_image,
)

input_frame = ctk.CTkFrame(
    window1,
    bg_color = '#023047',
    fg_color = '#023047'
)
input_frame.grid(
    row = 0,
    column = 1,
    sticky = 'news',
)

my_label = ctk.CTkLabel(
    input_frame,
    text = '',
    font = ('Helvetica', 20),
)
my_label.pack(pady=90)

username_label = ctk.CTkLabel(
    input_frame,
    text = 'Username',
    font = ('Helvetica', 12),
)

username_label.pack(
    pady = 0,
    padx = 80,
    anchor = 'w',)

name_entry = ctk.CTkEntry(
    input_frame,
    placeholder_text = 'Username',
    height = 30,
    width = 300,
    corner_radius = 5,
    textvariable=username,
)
name_entry.pack(pady = 2)

space_label = ctk.CTkLabel(
    input_frame,
    text = '',
)
space_label.pack(pady=0)

password_label = ctk.CTkLabel(
    input_frame,
    text = 'Password',
    font = ('Helvetica', 12),
)

password_label.pack(
    pady = 0,
    padx = 80,
    anchor = 'w',
)

password_entry = ctk.CTkEntry(
    input_frame,
    show = '*',
    placeholder_text = 'Password',
    width = 300,
    height = 30,
    corner_radius = 5,
    textvariable=password,
)
password_entry.pack(pady=2)

login_button = ctk.CTkButton(
    input_frame,
    text = 'Login',
    height = 30,
    width = 150,
    bg_color = '#3f3769',
    fg_color = '#4361ee',
    command=lambda: validate(),
)
login_button.pack(
    pady = 20,
    padx = 80,
    anchor = 'w',
)

my_label = ctk.CTkLabel(
    input_frame,
    text = '',
    font = ('Helvetica', 20),
)
my_label.pack(pady=40)

print(user_authenticated)



window1.mainloop()