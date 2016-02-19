from tkinter import *

ALL = N+S+W+E


class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1, minsize="100px")
        self.master.columnconfigure(0, weight=1, minsize="170px")
        self.grid(sticky=ALL)
        for r in range(4):
            self.rowconfigure(r, weight=1)
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c + 1)).grid(row=4, column=c, sticky=E+W)

        f1 = Frame(self, bg="green")
        f1.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=ALL)
        l1 = Label(f1, text="Frame1", bg="green", fg="white")
        l1.pack(side=TOP, fill=BOTH, expand=True)
        
        f2 = Frame(self, bg="blue")
        f2.grid(row=2, column=0, rowspan=2, columnspan=2, sticky=ALL)
        l2 = Label(f2, text="Frame2", bg="blue", fg="white")
        l2.pack(side=TOP, fill=BOTH, expand=True)
        
        f3 = Frame(self, bg="red")     
        f3.grid(row=0, column=2, rowspan=4, columnspan=3, sticky=ALL)
        l3 = Label(f3, text="Frame3", bg="red", fg="white")
        l3.pack(side=TOP, fill=BOTH, expand=True)

root = Tk()
app = Application(master=root)
app.mainloop()
