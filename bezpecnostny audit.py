import tkinter as tk
sirka=1280
vyska=600
root=tk.Tk()
canvas=tk.Canvas(root,width=sirka, height=vyska, bg='white')
canvas.pack()

def frame1():
    global frame, can
    frame=tk.Frame(root,width=sirka, height=vyska)
    frame.place(x=0,y=0)
    can=tk.Canvas(frame,width=sirka, height=vyska, bg='skyblue')
    can.pack()
frame1()
def vtransakcie():
    can.create_line(sirka//4-200, vyska//10+13,sirka//4+200, vyska//10+13, width=3)
    can.create_text(sirka//4, vyska//10, text='VŠETKY TRANSAKCIE BANKY', font='SourceSansPro 20')
    can.create_rectangle(sirka//4-250,vyska//10+35, sirka//4+250, vyska//10+65, fill='forestgreen', width=4)
    can.create_text(sirka//4,vyska//10+50, text='ÚSPEšNé TRANSAKCIE: (pocet)',font='SourceSansPro 12', fill='white')
    can.create_rectangle(sirka//4-250,vyska//10+85, sirka//4+250, vyska//10+105, fill='firebrick', outline='firebrick', width=5)
    can.create_text(sirka//4,vyska//10+95, text='NEÚSPEšNé TRANSAKCIE: ',font='SourceSansPro 12', fill='white')
    can.create_rectangle(sirka//4-250,vyska//10+102+4,sirka//4+250, vyska-4, outline='firebrick', width=5)
    can.create_rectangle(sirka//4-250+2,vyska//10+102+6,sirka//4+250-2, vyska-6, outline='black', width=4, fill='white')
    can.create_line(sirka//2,0,sirka//2,vyska,width=3)
    
def statistiky():
    can.create_rectangle(sirka//2+200, vyska//10-20,sirka//2+435, vyska//10+13, width=3, fill='white')
    can.create_text(sirka//2+sirka//4, vyska//10, text='ŠTATISTIKY', font='SourceSansPro 20')
    can.create_text(sirka//2+15, vyska//10+50, text='Priemerná výška vkladu:', font='SourceSansPro 20',anchor='w')
    can.create_text(sirka//2+15, vyska//10+80, text='Priemerný dlh na KK:', font='SourceSansPro 20',anchor='w')
    can.create_text(sirka//2+15, vyska//10+110, text='Priemerná výška transakcie:', font='SourceSansPro 20',anchor='w')

def filterf():
    global frame, can
    frame.destroy
    can.destroy
    frame=tk.Frame(root,width=sirka, height=vyska)
    frame.place(x=0,y=0)
    can=tk.Canvas(frame,width=sirka, height=vyska, bg='white')
    can.pack()
    can.create_rectangle(0,0,sirka,vyska, outline='skyblue', fill='skyblue')
    can.create_text(sirka//4, vyska//10+10, text='ČÍSLO KARTY:', font='SourceSansPro 20',anchor='e')
    entry1=tk.Entry().place(relx=.25,rely=.1)
    can.create_text(sirka//4, vyska//10+40, text='ČÍSLO ÚČTU:', font='SourceSansPro 20',anchor='e')
    entry2=tk.Entry().place(relx=.25,rely=.15)
    can.create_text(sirka//2+sirka//11, vyska//10+10, text='SUMA OD', font='SourceSansPro 20',anchor='e')
    entry3=tk.Entry().place(relx=.60,rely=.1)
    can.create_text(sirka//2+sirka//3, vyska//10+10, text='SUMA DO', font='SourceSansPro 20',anchor='e')
    entry4=tk.Entry().place(relx=.85,rely=.1)
    can.create_text(sirka//2+sirka//11, vyska//10+40, text='DÁTUM OD', font='SourceSansPro 20',anchor='e')
    entry3=tk.Entry().place(relx=.60,rely=.15)
    can.create_text(sirka//2+sirka//3, vyska//10+40, text='DÁTUM DO', font='SourceSansPro 20',anchor='e')
    entry4=tk.Entry().place(relx=.85,rely=.15)
    button2= tk.Button(text='FILTROVAŤ',command=filtrovat)
    button2.pack()
    button2.place(relx=.9, rely=.250, anchor="w")
    button3= tk.Button(text='<==',command=spat)
    button3.pack()
    button3.place(relx=.02, rely=.05, anchor="w")
def filtrovat():
    global frame, can
    can.create_rectangle(sirka//10,vyska//3,sirka-sirka//10, vyska, width=5, outline='deepskyblue')
    can.create_rectangle(sirka//10+2,vyska//3+2,sirka-sirka//10-2, vyska-2, width=4, outline='black', fill='white')
def spat():
    global frame, can
    frame.destroy
    can.destroy
    frame=tk.Frame(root,width=sirka, height=vyska)
    frame.place(x=0,y=0)
    can=tk.Canvas(frame,width=sirka, height=vyska, bg='skyblue')
    can.pack()
    statistiky()
    vtransakcie()
    button1= tk.Button(text='FILTER',command=filterf)
    button1.pack()
    button1.place(relx=.02, rely=.100, anchor="w")
statistiky()
vtransakcie()
button1= tk.Button(text='FILTER',command=filterf)
button1.pack()
button1.place(relx=.02, rely=.100, anchor="w")



   



