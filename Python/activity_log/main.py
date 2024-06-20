from tkinter import *
import customtkinter as ctk

# from utils.functions import *
# from views.login import login_page
# from views.signin import signin
from auth.authentication import User, is_authenticated, user_authenticated
from views.table_page import table_page

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
    if is_authenticated(username, my_label, password):
        window1.destroy()
        table_page()

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