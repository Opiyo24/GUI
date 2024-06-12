from tkinter import *
import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()

root.title('Activity Log | Welcome Back')
root.iconbitmap('')
root.geometry('900x450')

my_label = customtkinter.CTkLabel(
    root,
    text = '',
    font = ('Helvetica', 20),
)
my_label.pack(pady=40)

name_entry = customtkinter.CTkEntry(
    root,
    placeholder_text = 'Username',
    height = 30,
    width = 300,
    corner_radius = 5,
)
name_entry.pack(pady = 10)

password_entry = customtkinter.CTkEntry(
    root,
    placeholder_text = 'Password',
    width = 300,
    height = 30,
    corner_radius = 5,
)
password_entry.pack(pady=10)

login_button = customtkinter.CTkButton(
    root,
    text = 'Login',
    height = 30,
    width = 80,
)
login_button.pack(pady = 20)

root.mainloop()