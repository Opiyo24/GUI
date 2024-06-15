import customtkinter as ctk


def create_table(frame, columns):
    table = ctk.CTkTable(
        frame,
        columns = columns,
        show = 'headings',
        height = 100,
        bg_color = 'white',
        fg_color = 'black',
        corner_radius = 10,
        border_width = 3,
    )
    return table