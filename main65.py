from tkinter import*
from tkinter import messagebox
window=Tk()
window.title("Events")
window.geometry("100x100")

def handle_key(event):
    print(event.char)
    window.bind("<Key>", handle_key)

def handle_click(event):
    print("Button is clicked.")

button=Button(text="Click Me")
button.pack()
window.bind("<Button-1>", handle_click)




def msg():
    messagebox.showwarning("Message", "Alert, Virus detected.")

button1=Button(window,text="Scan Virus",command=msg)
button1.place(x=40,y=80)


window.mainloop()

