from tkinter import *

COLORS = {
     'baby_blue': '#9eb5df',
     'gray_blue': '#66738b',
     'red': '#d41f1f',
     'green': '#1fd483',
     'gray': '#99a1af',
     'white': '#ffffff',
     'dark_gray': '#4a5568'
 }

window = Tk()
window.geometry("420x420")
window.title("FitPlan")

window.config(background='#66738b')

label = Label(window,text="FitPlan",font=('Canva Sans',92,'bold'))
label = Label(window,text="FitPlan", font=('Canva Sans',92,'bold'), fg='white', bg='#66738b')

label.place(x=0, y=0)

button = Button(window,text='GET STARTED')
button.pack()

label.place(x=0, y=0)
button.place(x=190,y=160)

window.mainloop()