import tkinter as tk
from tkinter import ttk
import customtkinter as ctk


def create_table(frame, columns):
    table = ttk.Treeview(
        frame,
        columns = columns,
    )
