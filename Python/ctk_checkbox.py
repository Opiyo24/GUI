from tkinter import *
import customtkinter

customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()

root.title('Custom Tkinter Checkboxes')
root.iconbitmap('')
root.geometry('700x450')

def game():
    if check_var.get() == 'on':
        my_label.configure(text='You clicked the thing')
    else:
        my_label.configure(text='You didnt click the thing')


check_var = customtkinter.StringVar(value = 'off')
my_check = customtkinter.CTkCheckBox(
    root,
    text='Would you like to play a game?',
    variable = check_var,
    onvalue = 'on',
    offvalue = 'off',
)
my_check.pack(pady=40)

my_button = customtkinter.CTkButton(
    root,
    text = 'Submit',
    command = game,
)
my_button.pack(pady=20)

my_label = customtkinter.CTkLabel(
    root,
    text = ''
)
my_label.pack(pady=20)

root.mainloop()