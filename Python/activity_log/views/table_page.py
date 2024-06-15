import customtkinter as ctk

from utils.functions import create_table

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

window = ctk.CTk()

window.title('Activity Log')
window.iconbitmap('')
window.geometry('1600x800')
window.minsize(1600, 800)

window.columnconfigure((0,1,2,3,4,5,6,7,8), weight = 1, uniform = 'a')
window.rowconfigure((0,1,2,3,4,5,6), weight = 1, uniform = 'a')

cols = [
    "Entry Date",
    "Upload Date",
    "Owner",
    "Sub-County",
    "Description",
    "Floors",
    "Assigned",
    "Date Moved",
    "Days Left",
    "Last Follow-Up",
    "Status",
]

menu_frame = ctk.CTkFrame(
    window,
    border_width = 0,
    border_color = 'black',
    fg_color = 'green',
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
    fg_color = '#ecf496',
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
)
m_button3.pack(
    fill = 'x',
    padx = 1,
    pady = 4,
)

# name_label = ctk.CTkLabel(
#     menu_frame,
#     text = 'Username',
# )


date = ctk.CTkLabel(
    window,
    text = 'DD/MM/YYYY',
    font = ('Helvetica', 20, 'bold'),
)

date.grid(
    row = 0,
    column = 1,
)

back_button = ctk.CTkButton(
    window,
    text = 'Back',
    font = ('Helvetica', 20, 'bold'),
    height = 40,
    bg_color = 'transparent',
    fg_color = 'black',
    corner_radius = 10,
    border_width = 3,
)
back_button.grid(
    row = 0,
    column = 8,
)

entry_button = ctk.CTkButton(
    window,
    text = 'New Entry',
    height = 35,
    width = 50,
    bg_color = 'blue',
    fg_color = 'black',
    corner_radius = 10,
    border_width = 3,
)

entry_button.grid(
    row = 1,
    column = 1,
    # columnspan = 2,
    # sticky = 'news',
)

data_frame = ctk.CTkScrollableFrame(
    window,
    border_width = 1,
    border_color = 'black',
    corner_radius = 0,
)

data_frame.grid(
    row = 2,
    column = 1,
    rowspan = 5,
    columnspan = 8,
    sticky = 'news',
)

table = create_table(data_frame, cols)
table.pack(fill = 'both', expand = True)

window.mainloop()