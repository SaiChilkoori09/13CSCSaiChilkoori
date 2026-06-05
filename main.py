import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime
import threading
import time
from tkinter.ttk import Label

from PIL import ImageTk, Image

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

# Run the window
window = tk.Tk()
# window.geometry('1000x1000')
window.configure(bg=COLORS['gray_blue'])

canvas = tk.Canvas(window, width=200, height= 200, bg=COLORS['gray_blue'], borderwidth=0, highlightthickness=0)
canvas.pack()



class HomePage(tk.Frame):
    def __init__(window, parent):
        super().__init__(parent, bg=COLORS['gray_blue'])

    img = tk.PhotoImage(file="Images/dumbellicon.png")

    item = canvas.create_image(0, 0, image=img, anchor="nw")

    canvas.coords(item, 0, 0)

    # Title
    title = tk.Label(window, text='FitPlan',
        font=('Arial', 64, 'bold'),
        bg=COLORS['gray_blue'],
        fg=COLORS['white'])
    title.pack(pady=(60, 5))

    # RED LINE under FitPlan title
    red_line = tk.Frame(window, bg=COLORS['red'], height=3, width=400)
    red_line.pack(pady=(0, 10))
    red_line.pack_propagate(False)  # Maintain size


    #subtitle
    subtitle = tk.Label(window, text='Welcome!',
        font=('Arial', 24,),
        bg=COLORS['gray_blue'],
        fg=COLORS['white'])
    subtitle.pack(pady=(60, 6))

    subtitle = tk.Label(window, text='Build Workout Programs in Minutes and be healthier!',
        font=('Arial', 24,),
        bg=COLORS['gray_blue'],
        fg=COLORS['white'])
    subtitle.pack(pady=(60, 7))

    #Quote
    # quote = tk.Label(window, text='The last three or four reps is what makes the muscle grow.— Arnold Schwarzenegger',
    #     font=('Cinzel', 15),
    #     bg=COLORS['gray_blue'],
    #     fg = COLORS['white'])
    # quote.pack(pady=(60, 10))

    start_btn = tk.Button(window, text='GET STARTED',
        font=('Arial', 16, 'bold'),
        bg=COLORS['red'],
        fg=COLORS['white'],
        padx=30, pady=15, relief='flat', cursor='hand2')
    start_btn.pack(pady=20)

    # quote = tk.Label(window, text='"Success isnt always about greatness. Its about consistency." — Dwayne The Rock Johnson"',
    #     font=('Cinzel', 15),
    #     bg=COLORS['gray_blue'],
    #     fg=COLORS['white'])
    # quote.pack(pady=(60, 10))

    # Feature icons row WITH RED VERTICAL LINES
    features_frame = tk.Frame(window, bg=COLORS['gray_blue'])
    features_frame.pack(pady=20)

    features = [('Sign Up', Image.open("Images/bookicon.png")), ('Plan Workouts', '🏋️'), ('Log Sessions', '📖')]

    for i, (feature_text, icon) in enumerate(features):
        # Feature container
        c = tk.Frame(features_frame, bg=COLORS['gray_blue'])
        c.grid(row=0, column=i * 2, padx=40)

        # Icon
        tk.Label(c, text=icon, font=('Arial', 28),
                    bg=COLORS['gray_blue'],
                    fg=COLORS['white']).pack()

        # Feature text
        tk.Label(c, text=feature_text, font=('Arial', 11, 'bold'),
                    bg=COLORS['gray_blue'],
                    fg=COLORS['white']).pack()

        # Red line breaks
        if i < len(features) - 1:
            separator = tk.Frame(features_frame, bg=COLORS['red'], width=3, height=80)
            separator.grid(row=0, column=i * 2 + 1, padx=0)
            separator.grid_propagate(False)  # Maintain size

window.mainloop()