from tkinter import *

ALL = N+S+W+E


class Application(Frame):
    
    def clicker1(self, event):
            print("Frame 1 was clicked at", event.x, event.y)
            
    def clicker2(self, event):
            print("Frame 2 was clicked at", event.x, event.y)
            
    def red(self):
        self.text.configure(fg="red")
    def blue(self):
        self.text.configure(fg="blue")
    def green(self):
        self.text.configure(fg="green")
    def black(self):
        self.text.configure(fg="black")
    def openz(self):
        self.path = self.entry.get()        
        try:
            with open(self.path, "r") as f:
                lines = f.readlines()
                result = ''.join(lines)
            self.text.insert('1.0', result)
        except:
            self.text.insert('1.0', "No such file or content")
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1, minsize="100px")
        self.master.columnconfigure(0, weight=1, minsize="170px")
        self.grid(sticky=ALL)
        for r in range(4):
            self.rowconfigure(r, weight=1)
        for c in range(5):
            self.columnconfigure(c, weight=1)

        f1 = Frame(self, bg="green")         
        f1.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=ALL)      
        l1 = Label(f1, text="Frame1", bg="green", fg="white")
        l1.bind("<Button-1>", self.clicker1) 
        l1.pack(side=TOP, fill=BOTH, expand=True)
        
        f2 = Frame(self, bg="blue")
        f2.grid(row=2, column=0, rowspan=2, columnspan=2, sticky=ALL)
        f2.bind("<Button-1>", self.clicker2)
        l2 = Label(f2, text="Frame2", bg="blue", fg="white")
        l2.bind("<Button-1>", self.clicker2) 
        l2.pack(side=TOP, fill=BOTH, expand=True)
        
        f3 = Frame(self, bg="red")     
        f3.grid(row=0, column=2, rowspan=3, columnspan=3, sticky=ALL)
        l3 = Label(f3, text="Frame3", bg="white", fg="black")
        l3.pack(side=TOP, fill=BOTH, expand=True)        
        
        self.entry = Entry(self)
        self.entry.grid(row=0, rowspan=1, column=2, columnspan=3, sticky=ALL)
        self.text = Text(self, height=7, width=10)
        self.text.grid(row=1, rowspan=3, column=2, columnspan=3, sticky=ALL)
        
        Button(self, command=self.red, text="Red").grid(row=4, column=0, sticky=E+W)
        Button(self, command=self.blue, text="Blue").grid(row=4, column=1, sticky=E+W)
        Button(self, command=self.green, text="Green").grid(row=4, column=2, sticky=E+W)
        Button(self, command=self.black, text="Black").grid(row=4, column=3, sticky=E+W)
        Button(self, command=self.openz, text="Open").grid(row=4, column=4, sticky=E+W)
    

root = Tk()
app = Application(master=root)
app.mainloop()
