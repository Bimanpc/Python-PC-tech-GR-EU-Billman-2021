import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Visual TK 5 PCEU")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_406=tk.Button(root)
        GButton_406["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_406["font"] = ft
        GButton_406["fg"] = "#000000"
        GButton_406["justify"] = "center"
        GButton_406["text"] = "visualtk.com"
        GButton_406.place(x=210,y=70,width=149,height=30)
        GButton_406["command"] = self.GButton_406_command

        GMessage_319=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_319["font"] = ft
        GMessage_319["fg"] = "#333333"
        GMessage_319["justify"] = "center"
        GMessage_319["text"] = "Super STARS GEEKING 4 PC WITH Python!!!!!!!"
        GMessage_319.place(x=90,y=80,width=390,height=314)

        GButton_307=tk.Button(root)
        GButton_307["bg"] = "#90f090"
        ft = tkFont.Font(family='Times',size=10)
        GButton_307["font"] = ft
        GButton_307["fg"] = "#fad400"
        GButton_307["justify"] = "left"
        GButton_307["text"] = "Lets Geekit!!!"
        GButton_307["relief"] = "flat"
        GButton_307.place(x=180,y=270,width=268,height=109)
        GButton_307["command"] = self.GButton_307_command

    def GButton_406_command(self):
        print("command")


    def GButton_307_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
