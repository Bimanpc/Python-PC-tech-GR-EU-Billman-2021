Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>     1 #! /usr/bin/env python
    2 #  -*- coding: utf-8 -*-
    3 #
    4 # GUI module generated by PAGE version 6.2
    5 #  in conjunction with Tcl version 8.6
    6 #    May 30, 2021 07:18:05 PM EEST  platform: Windows NT
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
   22 import pc tech official_support
   23 
   24 def vp_start_gui():
   25     '''Starting point when module is the main routine.'''
   26     global val, w, root
   27     root = tk.Tk()
   28     top = Toplevel1 (root)
   29     pc tech official_support.init(root, top)
   30     root.mainloop()
   31 
   32 w = None
   33 def create_Toplevel1(rt, *args, **kwargs):
   34     '''Starting point when module is imported by another module.
   35        Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
   36     global w, w_win, root
   37     #rt = root
   38     root = rt
   39     w = tk.Toplevel (root)
   40     top = Toplevel1 (w)
   41     pc tech official_support.init(w, top, *args, **kwargs)
   42     return (w, top)
   43 
   44 def destroy_Toplevel1():
   45     global w
   46     w.destroy()
   47     w = None
   48 
   49 class Toplevel1:
   50     def __init__(self, top=None):
   51         '''This class configures and populates the toplevel window.
   52            top is the toplevel containing window.'''
   53         _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
   54         _fgcolor = '#000000'  # X11 color: 'black'
   55         _compcolor = '#d9d9d9' # X11 color: 'gray85'
   56         _ana1color = '#d9d9d9' # X11 color: 'gray85'
   57         _ana2color = '#ececec' # Closest X11 color: 'gray92'
   58 
   59         top.geometry("600x450+383+106")
   60         top.minsize(120, 1)
   61         top.maxsize(1370, 749)
   62         top.resizable(1,  1)
   63         top.title("PC YECH BY Biilaman'S")
   64         top.configure(background="#d9d9d9")
   65 
   66         self.http://pctechgreu.unaux.com/?z&i=1 = tk.Button(top)
   67         self.http://pctechgreu.unaux.com/?z&i=1.place(relx=0.383, rely=0.844
   68                 , height=34, width=127)
   69         self.http://pctechgreu.unaux.com/?z&i=1.configure(activebackground="#ececec")
   70         self.http://pctechgreu.unaux.com/?z&i=1.configure(activeforeground="#000000")
   71         self.http://pctechgreu.unaux.com/?z&i=1.configure(background="#d9d9d9")
   72         self.http://pctechgreu.unaux.com/?z&i=1.configure(disabledforeground="#a3a3a3")
   73         self.http://pctechgreu.unaux.com/?z&i=1.configure(foreground="#000000")
   74         self.http://pctechgreu.unaux.com/?z&i=1.configure(highlightbackground="#d9d9d9")
   75         self.http://pctechgreu.unaux.com/?z&i=1.configure(highlightcolor="black")
   76         self.http://pctechgreu.unaux.com/?z&i=1.configure(pady="0")
   77         self.http://pctechgreu.unaux.com/?z&i=1.configure(text='''SITE''')
   78 
   79         self.Message1 = tk.Message(top)
   80         self.Message1.place(relx=0.083, rely=0.333, relheight=0.207
   81                 , relwidth=0.267)
   82         self.Message1.configure(background="#d9d9d9")
   83         self.Message1.configure(foreground="#000000")
   84         self.Message1.configure(highlightbackground="#d9d9d9")
   85         self.Message1.configure(highlightcolor="black")
   86         self.Message1.configure(text='''PC TEECH OFFICIAL''')
   87         self.Message1.configure(width=160)
   88 
   89 if __name__ == '__main__':
   90     vp_start_gui()
   91 
   92 

