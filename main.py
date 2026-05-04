from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("FitPlan")

window.config(background="#66738b")

label = Label(window,
              text="FitPlan",
              font=('Canva Sans',92,'bold'),
              fg='white',
              bg='#66738b'
              )

button = Button(window,text='GET STARTED')
button.pack()

label.place(x=0, y=0)
button.place(x=190,y=160)

window.mainloop()