from tkinter import *
import customtkinter

def signin(window):
    frame = customtkinter.CTkFrame(window, width = 1000, height = 450)
    frame.pack(expand=True, fill='both')

    my_label = customtkinter.CTkLabel(
        frame,
        text = '',
        font = ('Helvetica', 20),
    )
    my_label.pack(pady=20)

    username_entry = customtkinter.CTkEntry(
        frame,
        placeholder_text = 'Username',
        height = 30,
        width = 200,
        corner_radius = 5,
    )
    username_entry.pack(pady = 10)

    password_entry = customtkinter.CTkEntry(
        frame,
        placeholder_text = 'Password',
        width = 200,
        height = 30,
    )
    password_entry.pack(pady=10)

    c_password_entry = customtkinter.CTkEntry(
        frame,
        placeholder_text = 'Confirm Password',
        width = 200,
        height = 30,
    )
    c_password_entry.pack(pady=10)

    signup_button = customtkinter.CTkButton(
        frame,
        text = 'Sign Up',
        width = 80,
        height = 30,
    )
    signup_button.pack(pady = 20)

    print('This is the signin page')