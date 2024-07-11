from tkinter import *
import customtkinter

#set theme and color options
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.title('Opiyo GUI')
root.geometry('400x400')

my_button = customtkinter.CTkButton(
    root, 
    text='Hello World!!'
    )
my_button.pack(pady=80)

root.mainloop()