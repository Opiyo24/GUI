from tkinter import *
import customtkinter

root = customtkinter.CTk()

root.title('Combobox')
root.iconbitmap('')
root.geometry('700x450')

def color_picker(choice):
    output_label.configure(
        text=choice,
        text_color = choice,
    )

my_label = customtkinter.CTkLabel(
    root,
    text = 'Pick a color',
    font = ('Helvetica', 18),
)
my_label.pack(pady=40)

colors = ["Red", "Green", "Blue"]
my_combo = customtkinter.CTkComboBox(
    root,
    values = colors,
    command = color_picker,
)
my_combo.pack(pady=0)

output_label = customtkinter.CTkLabel(
    root,
    text = '',
    font = ('Helvetica', 18),
)
output_label.pack(pady=20)

root.mainloop()