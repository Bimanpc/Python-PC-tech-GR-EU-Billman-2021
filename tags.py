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

        GButton_213=tk.Button(root)
        GButton_213["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_213["font"] = ft
        GButton_213["fg"] = "#000000"
        GButton_213["justify"] = "center"
        GButton_213["text"] = "https://sourceforge.net/projects/autoscreen/"
        GButton_213.place(x=80,y=310,width=337,height=143)
        GButton_213["command"] = self.GButton_213_command

        GLabel_274=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_274["font"] = ft
        GLabel_274["fg"] = "#333333"
        GLabel_274["justify"] = "center"
        GLabel_274["text"] = "ScreenCapture"
        GLabel_274.place(x=100,y=80,width=70,height=25)

        GLabel_540=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_540["font"] = ft
        GLabel_540["fg"] = "#333333"
        GLabel_540["justify"] = "center"
        GLabel_540["text"] = "Win10/11"
        GLabel_540.place(x=100,y=90,width=70,height=25)

    def GButton_213_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
