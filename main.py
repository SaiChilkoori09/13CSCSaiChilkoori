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

label.place(x=0, y=0)

window.mainloop()