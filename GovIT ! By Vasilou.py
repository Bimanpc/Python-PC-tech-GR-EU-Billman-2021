    1 #! /usr/bin/env python
    2 #  -*- coding: utf-8 -*-
    3 #
    4 # GUI module generated by PAGE version 6.2
    5 #  in conjunction with Tcl version 8.6
    6 #    Mar 31, 2022 07:26:43 PM EEST  platform: Windows NT
    7 
    8 import sys
    9 
   10 try:
   11     import Tkinter as tk
   12 except ImportError:
   13     import tkinter as tk
   14 
   15 try:
   16     import ttk
   17     py3 = False
   18 except ImportError:
   19     import tkinter.ttk as ttk
   20     py3 = True
   21 
   22 import govit_support
   23 
   24 def vp_start_gui():
   25     '''Starting point when module is the main routine.'''
   26     global val, w, root
   27     root = tk.Tk()
   28     govit_support.set_Tk_var()
   29     top = Toplevel1 (root)
   30     govit_support.init(root, top)
   31     root.mainloop()
   32 
   33 w = None
   34 def create_Toplevel1(rt, *args, **kwargs):
   35     '''Starting point when module is imported by another module.
   36        Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
   37     global w, w_win, root
   38     #rt = root
   39     root = rt
   40     w = tk.Toplevel (root)
   41     govit_support.set_Tk_var()
   42     top = Toplevel1 (w)
   43     govit_support.init(w, top, *args, **kwargs)
   44     return (w, top)
   45 
   46 def destroy_Toplevel1():
   47     global w
   48     w.destroy()
   49     w = None
   50 
   51 class Toplevel1:
   52     def __init__(self, top=None):
   53         '''This class configures and populates the toplevel window.
   54            top is the toplevel containing window.'''
   55         _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
   56         _fgcolor = '#000000'  # X11 color: 'black'
   57         _compcolor = '#d9d9d9' # X11 color: 'gray85'
   58         _ana1color = '#d9d9d9' # X11 color: 'gray85'
   59         _ana2color = '#ececec' # Closest X11 color: 'gray92'
   60 
   61         top.geometry("600x450+383+106")
   62         top.minsize(116, 1)
   63         top.maxsize(1366, 746)
   64         top.resizable(1,  1)
   65         top.title("New Toplevel")
   66         top.configure(background="#d9d9d9")
   67 
   68         self.Button1 = tk.Button(top)
   69         self.Button1.place(relx=0.267, rely=0.067, height=194, width=296)
   70         self.Button1.configure(activebackground="#ececec")
   71         self.Button1.configure(activeforeground="#000000")
   72         self.Button1.configure(background="#d9d9d9")
   73         self.Button1.configure(disabledforeground="#a3a3a3")
   74         self.Button1.configure(foreground="#000000")
   75         self.Button1.configure(highlightbackground="#d9d9d9")
   76         self.Button1.configure(highlightcolor="black")
   77         self.Button1.configure(pady="0")
   78         self.Button1.configure(text='''https://www.gov.gr/''')
   79 
   80         self.Checkbutton1 = tk.Checkbutton(top)
   81         self.Checkbutton1.place(relx=0.283, rely=0.556, relheight=0.056
   82                 , relwidth=0.105)
   83         self.Checkbutton1.configure(activebackground="#ececec")
   84         self.Checkbutton1.configure(activeforeground="#000000")
   85         self.Checkbutton1.configure(background="#d9d9d9")
   86         self.Checkbutton1.configure(disabledforeground="#a3a3a3")
   87         self.Checkbutton1.configure(foreground="#000000")
   88         self.Checkbutton1.configure(highlightbackground="#d9d9d9")
   89         self.Checkbutton1.configure(highlightcolor="black")
   90         self.Checkbutton1.configure(justify='left')
   91         self.Checkbutton1.configure(text='''Lets Govt !!''')
   92         self.Checkbutton1.configure(variable=govit_support.che46)
   93 
   94 if __name__ == '__main__':
   95     vp_start_gui()
   96 
   97 
