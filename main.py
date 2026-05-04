 #Import GUI models
import tkinter as tk
 from random import setstate
 from tkinter.font import names

 COLORS = {
     'baby_blue': '#9eb5df',
     'gray_blue': '#66738b',
     'red': '#d41f1f',
     'green': '#1fd483',
     'gray': '#99a1af',
     'white': '#ffffff',
     'dark_gray': '#4a5568'
 }


 class Excercise:


    def __init__(self, name, sets, reps. weight, notes=""):
    self.name = names
    self.sets = sets
    self.reps = reps
    self.weight = weight
    self.notes = notes

    def to_dict(self):
        return {
            'name': self.name,
            'sets': self.sets,
            'reps': self.reps,
            'weight': self.weight,
            'notes': self.notes
        }


class PlannerApp:
    def __init__(self, root):
        self.root = root

#For the  title, screen size and background
        self.root.title("FitPlan")
        self.root.geometry("1024x600")
        self.root.configure(bg="#66738b")

