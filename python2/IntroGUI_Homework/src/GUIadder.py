from tkinter import *

class Application(Frame):
    """app main window class"""
    def __init__(self, master=None):
        """Main frame init """
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        """Add all widgets to the main frame"""

        top_frame = Frame(self)
        top_frame.pack(side=TOP)
        self.textA = Entry(top_frame)
        self.labelA = Label(top_frame, text="Value A")
        self.labelA.pack(side=TOP)
        self.textA.pack()
        self.textB = Entry(top_frame)
        self.labelB = Label(top_frame, text="Value B")      
        self.labelB.pack(side=TOP)
        self.textB.pack()
        
        w = Label(top_frame, text="A + B =")
        w.pack(side=TOP)
        w.pack()
        
        self.label = Label(top_frame)       
        self.label.pack()
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        
        self.button = Button(bottom_frame, text="Add", command=self.handle)
        self.button.pack(side=LEFT)
        
        self.QUIT = Button(bottom_frame, text="Quit", command=self.quit)
        self.QUIT.pack(side=LEFT)
        
    def handle(self):
        """Get both values and if float, add them up"""
        txt1 = self.textA.get()
        txt2 = self.textB.get()
        try:
            self.label.config(text = str(float(txt1) + float(txt2)) )
        except ValueError:
            self.label.config(text = '***ERROR***')
    	
root = Tk()
app = Application(master=root)
app.mainloop()