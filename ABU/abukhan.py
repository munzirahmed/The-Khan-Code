import tkinter
window = tkinter.Tk()
window.geometry("800x200")
photo1 = tkinter.PhotoImage(file="abu2.0.gif")
ImageLabel = tkinter.Label(window, image=photo1)
ImageLabel.pack()


