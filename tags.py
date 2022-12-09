import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_783=tk.Button(root)
        GButton_783["anchor"] = "nw"
        GButton_783["bg"] = "#1a64c4"
        ft = tkFont.Font(family='Times',size=10)
        GButton_783["font"] = ft
        GButton_783["fg"] = "#000000"
        GButton_783["justify"] = "center"
        GButton_783["text"] = "https://themetaxmas20.pages.dev/TheMetaXmas"
        GButton_783.place(x=160,y=400,width=295,height=58)
        GButton_783["command"] = self.GButton_783_command

        GMessage_139=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_139["font"] = ft
        GMessage_139["fg"] = "#333333"
        GMessage_139["justify"] = "center"
        GMessage_139["text"] = "https://themetaxmas20.pages.dev/TheMetaXmas"
        GMessage_139.place(x=160,y=90,width=259,height=172)

    def GButton_783_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
