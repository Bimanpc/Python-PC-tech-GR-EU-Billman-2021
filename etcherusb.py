#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    May 02, 2023 07:28:09 PM EEST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import etcherusb_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")

        self.top = top

class Toplevel2:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+333+156")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Toplevel 1")
        top.configure(background="#d9d9d9")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.483, rely=0.867, height=24, width=47)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Etcher''')
        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.233, rely=0.778, height=24, width=357)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''https://www.balena.io/etcher#download-etcher''')

def start_up():
    etcherusb_support.main()

if __name__ == '__main__':
    etcherusb_support.main()




