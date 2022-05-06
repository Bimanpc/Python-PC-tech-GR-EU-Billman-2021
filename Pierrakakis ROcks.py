from tkinter import *
from tkinter import ttk

ws = Tk()
ws.geometry('700x500')
ws.title('PythonGekkz')

f = ('Helvetica', 14)

Label(
    ws, 
    text='Full name',
    font=f
).place(x=10, y=10)

Entry(ws, font=f).place(x=100, y=10)

Label(
    ws,
    text='Email',
    font=f
).place(x=10, y=40)

Entry(ws, font=f).place(x=100, y=40)

Label(
    ws,
    text='Mobile',
    font=f
).place(x=10, y=70)

Entry(ws, font=f).place(x=100, y=70)

genwin = LabelFrame(
    ws,
    text='Date of birth',
    font=f
)
genwin.place(x=10, y=100)

Radiobutton(
    genwin,
    text='Male',
    value=1,
    font=f
).pack(side=LEFT)

Radiobutton(
    genwin,
    text='Female',
    value=2,
    font=f
).pack(side=LEFT)

Radiobutton(
    genwin,
    text='Others',
    value=3,
    font=f
).pack(side=LEFT)

dobwin = LabelFrame(
    ws,
    text='Gender',
    font=f
)
dobwin.place(x=10, y=170)

ttk.Combobox(
    dobwin,
    values=['01', '02', '03', '04', '05', '06' ],
    width=5,
    font=f
).pack(side=LEFT)

ttk.Combobox(
    dobwin,
    values=['Janaury', 'February', 'March', 'April', 'May', 'June' ],
    width=7,
    font=f
).pack(side=LEFT)

ttk.Combobox(
    dobwin,
    values=['1995', '1996', '1997', '1998', '1999', '2000' ],
    width=5,
    font=f
).pack(side=LEFT)

Checkbutton(
    ws,
    text= 'Accept Terms & Conditions',

).place(x=10, y=240)

Button(
    ws,
    text='Submit',
    command=None,
    font=f,
    width=10
).place(x=10, y=270)

Button(
    ws,
    text='Clear',
    command=None,
    font=f,
    width=10
).place(x=150, y=270)

ttk.Separator(
    ws,
    takefocus=0,
    orient=VERTICAL
).place(x=350, y=0, relheight=1)


logwin = LabelFrame(
    ws, 
    text='Login',
    font=f,
    padx=10,
    pady=10
)
logwin.place(x=360, y=10)

Label(
    logwin, 
    text='Email',
    font=f,
    pady=10
).grid(row=0, column=0, sticky='w')

Entry(
    logwin, 
    font=f,
    width=15
    ).grid(row=0, column=1)

Label(
    logwin,
    text='Password',
    font=f
).grid(row=1, column=0)

Entry(
    logwin, 
    font=f,
    width=15
).grid(row=1, column=1)

Button(
    logwin,
    text='Submit',
    command=None,
    font=f
).grid(row=2, column=1, sticky=EW, pady=10)

ws.mainloop()