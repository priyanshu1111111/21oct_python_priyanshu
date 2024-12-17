import tkinter

screen=tkinter.Tk()
screen.geometry("800x700")
screen.config(bg="red")
screen.title("Kishan")

tkinter.Label(text="Firstname:",fg='black',bg="red",font='20').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Lastname:",fg='black',bg="red",font='20').grid(row=1,column=0,sticky='w')


tkinter.Entry().grid(row=0,column=1,sticky='w')
tkinter.Entry().grid(row=0,column=1,sticky='w')

tkinter.RADIOBUTTON(Value=0,te)

screen.mainloop()