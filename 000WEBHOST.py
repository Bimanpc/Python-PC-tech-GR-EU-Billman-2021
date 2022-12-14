import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("000WEBHOST")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_791=tk.Button(root)
        GButton_791["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_791["font"] = ft
        GButton_791["fg"] = "#000000"
        GButton_791["justify"] = "center"
        GButton_791["text"] = "000WEBHOST.COM"
        GButton_791.place(x=170,y=350,width=191,height=31)
        GButton_791["command"] = self.GButton_791_command

        GLabel_766=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_766["font"] = ft
        GLabel_766["fg"] = "#333333"
        GLabel_766["justify"] = "center"
        GLabel_766["text"] = "000WEBHOST"
        GLabel_766.place(x=180,y=170,width=238,height=80)

    def GButton_791_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
