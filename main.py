import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import threading
import time

# Color palette — define once, use everywhere
COLORS = {
    'baby_blue': '#9eb5df',
    'gray_blue': '#66738b',
    'red':       '#d41f1f',
    'green':     '#1fd483',
    'gray':      '#99a1af',
    'white':     '#ffffff',
    'dark_gray': '#4a5568'
}

class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS['gray_blue'])

        # Title
        title = tk.Label(self, text='FitPlan',
            font=('Arial', 64, 'bold'),
            bg=COLORS['gray_blue'],
            fg=COLORS['white'])
        title.pack(pady=(60, 5))


# Run the window
window = tk.Tk()
window.title('FitPlan')
window.geometry('1000x700')
window.configure(bg=COLORS['gray_blue'])

page = HomePage(window)
page.pack(fill='both', expand=True)

window.mainloop()