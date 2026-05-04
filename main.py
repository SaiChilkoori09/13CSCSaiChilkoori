 #Import GUI models
import tkinter as tk
 from random import setstate
 from tkinter.font import names


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

