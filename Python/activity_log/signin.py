from tkinter import *
import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()

root.title('Activity Log | Welcome')
root.iconbitmap('')
root.geometry('900x450')

my_label = customtkinter.CTkLabel(
    root,
    text = '',
    font = ('Helvetica', 20),
)
my_label.pack(pady=20)

username_entry = customtkinter.CTkEntry(
    root,
    placeholder_text = 'Username',
    height = 30,
    width = 200,
    corner_radius = 5,
)
username_entry.pack(pady = 10)

password_entry = customtkinter.CTkEntry(
    root,
    placeholder_text = 'Password',
    width = 200,
    height = 30,
)
password_entry.pack(pady=10)

c_password_entry = customtkinter.CTkEntry(
    root,
    placeholder_text = 'Confirm Password',
    width = 200,
    height = 30,
)
c_password_entry.pack(pady=10)

signup_button = customtkinter.CTkButton(
    root,
    text = 'Sign Up',
    width = 80,
    height = 30,
)
signup_button.pack(pady = 20)

root.mainloop()