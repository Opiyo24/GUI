from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename='superhero')

root.title('My Calendar')
root.geometry('340x220')

def datey():
    #Grab the date
    my_label.config(text=f"You picked: {my_date.entry.get()}")

#Create calendar widget
my_date = tb.DateEntry(
    root,
    bootstyle="danger",
)
my_date.pack(pady=50)

#Extract date value
my_button = tb.Button(
    root,
    text='Get Date',
    bootstyle = 'danger outline',
    command = datey,
)
my_button.pack(pady = 20)

my_label = tb.Label(
    root,
    text = 'Ypu picked: ',
)
my_label.pack(pady =20)

root.mainloop()