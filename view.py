from tkinter import *

def createWindow():
    global window
    window = Tk()
    window.title("World Organizer")

    width = window.winfo_screenwidth()//2
    height = window.winfo_screenheight()//2

    window.geometry(f'{width}x{height}')

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    createMenubar()

    createSidebar()

    map = worldMap(window)

    map.grid(column=1, row=0)


    window.mainloop()

def createMenubar():
    global window

    menubar = Menu(window)
    fileMenu = Menu(menubar, tearoff=0)
    fileMenu.add_command(label="New", command=donothing)
    fileMenu.add_command(label="Exit", command=donothing)
    menubar.add_cascade(label="File", menu=fileMenu)

    window.config(menu=menubar)

def createSidebar():
    global window
    window.update()
    frame = Frame(window, bg=("gray"), width=30, height=window.winfo_height())

    frame.grid(column=0, row=0, sticky= "W")
    
def donothing():
    pass

class worldMap(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs, bg="Blue")
        self.bind("<Button-1>", self.placePoint)

    def addPoint(self, event):
        pass


    def placePoint(self, event):
        print(event.x, event.y)