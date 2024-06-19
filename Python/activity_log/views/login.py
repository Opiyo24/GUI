from tkinter import *
import customtkinter

from auth.authentication import User

username = StringVar()
password = StringVar()


def login_page(window):
    global username, password

    frame = customtkinter.CTkFrame(window, width = 1000, height = 450)
    frame.pack(expand=True, fill='both')

    my_label = customtkinter.CTkLabel(
        frame,
        text = '',
        font = ('Helvetica', 20),
    )
    my_label.pack(pady=40)

    name_entry = customtkinter.CTkEntry(
        frame,
        placeholder_text = 'Username',
        height = 30,
        width = 300,
        corner_radius = 5,
        textvariable=username
    )
    name_entry.pack(pady = 10)

    password_entry = customtkinter.CTkEntry(
        frame,
        placeholder_text = 'Password',
        width = 300,
        height = 30,
        corner_radius = 5,
        textvariable=password,
    )
    password_entry.pack(pady=10)

    login_button = customtkinter.CTkButton(
        frame,
        text = 'Login',
        height = 30,
        width = 80,
        command=authenticate,
    )
    login_button.pack(pady = 20)

    my_label = customtkinter.CTkLabel(
        frame,
        text = '',
        font = ('Helvetica', 20),
    )
    my_label.pack(pady=40)