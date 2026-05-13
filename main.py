import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import threading
import time

# Color palette
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

        #line break
        canvas.create_line((50, 50, 250, 50), fill="#d41f1f", width=3)
        canvas.pack(pady=(60, 50))

        #subtitle
        subtitle = tk.Label(self, text='Welcome!',
            font=('Arial', 24,),
            bg=COLORS['gray_blue'],
            fg=COLORS['white'])
        subtitle.pack(pady=(60, 6))

        subtitle = tk.Label(self, text='Build Workout Programs in Minutes and be healthier!',
            font=('Arial', 24,),
            bg=COLORS['gray_blue'],
            fg=COLORS['white'])
        subtitle.pack(pady=(60, 7))

        #Quote
        quote = tk.Label(self, text='The last three or four reps is what makes the muscle grow.— Arnold Schwarzenegger',
            font=(cinzel_font, 15),
            bg=COLORS['gray_blue'],
            fg = COLORS['white'])
        quote.pack(pady=(60, 10))

        start_btn = tk.Button(self, text='GET STARTED',
            font=('Arial', 16, 'bold'),
            bg=COLORS['red'],
            fg=COLORS['white'],
            padx=30, pady=15, relief='flat', cursor='hand2')
        start_btn.pack(pady=20)

        quote = tk.Label(self, text='"Success isnt always about greatness. Its about consistency." — Dwayne The Rock Johnson"',
            font=(cinzel_font, 15),
            bg=COLORS['gray_blue'],
            fg=COLORS['white'])
        quote.pack(pady=(60, 10))


# Run the window
window = tk.Tk()
window.geometry('1000x700')
window.configure(bg=COLORS['gray_blue'])

canvas = tk.Canvas(window, width=200, height= 200, bg=COLORS['gray_blue'], borderwidth=0, highlightthickness=0)
canvas.pack()

page = HomePage(window)
page.pack(fill='both', expand=True)

window.mainloop()