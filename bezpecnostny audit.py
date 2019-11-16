import tkinter
sirka=1280
vyska=600
canvas=tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()
echo '# Bezpe-nostn-audit' >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/Zdarilekova/Bezpe-nostn-audit.git
git push -u origin master
def vtransakcie():
    canvas.create_text(sirka//4, vyska//10, text='VŠETKY TRANSAKCIE BANKY', font='Arial 20')
    canvas.create_line(sirka//4-200, vyska//10+13,sirka//4+200, vyska//10+13, width=3)
    canvas.create_rectangle(sirka//4-250,vyska//10+35, sirka//4+250, vyska//10+65, fill='black')
    canvas.create_text(sirka//4,vyska//10+45, text='ÚSPEšNé TRANSAKCIE: (pocet)',font='Arial 15', fill='white')
    canvas.create_rectangle(sirka//4-250,vyska//10+85, sirka//4+250, vyska//10+105, fill='black')
    canvas.create_text(sirka//4,vyska//10+95, text='NEÚSPEšNé TRANSAKCIE: ',font='Arial 15', fill='white')
    canvas.create_rectangle(sirka//4-250,vyska//10+105,sirka//4+250, vyska)
    canvas.create_line(sirka//2,0,sirka//2,vyska,width=3) 
def statistiky():
    canvas.create_text(sirka//2+sirka//4, vyska//10, text='ŠTATISTIKY', font='Arial 20')
    canvas.create_line(sirka//2+200, vyska//10+13,sirka//2+450, vyska//10+13, width=3)
    canvas.create_text(sirka//2+15, vyska//10+50, text='Priemerná výška vkladu:', font='Arial 20',anchor='w')
    canvas.create_text(sirka//2+15, vyska//10+80, text='Priemerný dlh na KK:', font='Arial 20',anchor='w')
    canvas.create_text(sirka//2+15, vyska//10+110, text='Priemerná výška transakcie:', font='Arial 20',anchor='w')

def filterf():
    global entry1
    canvas.delete('all')
    canvas.create_text(sirka//4, vyska//10+10, text='ČÍSLO KARTY:', font='SourceSansPro 20',anchor='e')
    entry1=tkinter.Entry().place(relx=.25,rely=.1)
##    entry1.pack()
##    cislokarty=entry1.get()
##    w = Entry( master, option,cursor(dot))
    canvas.create_text(sirka//4, vyska//10+40, text='ČÍSLO ÚČTU:', font='SourceSansPro 20',anchor='e')
    entry2=tkinter.Entry().place(relx=.25,rely=.15)
    canvas.create_text(sirka//2+sirka//11, vyska//10+10, text='SUMA OD', font='SourceSansPro 20',anchor='e')
    entry3=tkinter.Entry().place(relx=.60,rely=.1)
    canvas.create_text(sirka//2+sirka//3, vyska//10+10, text='SUMA DO', font='SourceSansPro 20',anchor='e')
    entry4=tkinter.Entry().place(relx=.85,rely=.1)
    canvas.create_text(sirka//2+sirka//11, vyska//10+40, text='DÁTUM OD', font='SourceSansPro 20',anchor='e')
    entry3=tkinter.Entry().place(relx=.60,rely=.15)
    canvas.create_text(sirka//2+sirka//3, vyska//10+40, text='DÁTUM DO', font='SourceSansPro 20',anchor='e')
    entry4=tkinter.Entry().place(relx=.85,rely=.15)
    button2= tkinter.Button(text='FILTROVAŤ',command=filtrovat)
    button2.pack()
    button2.place(relx=.02, rely=.100, anchor="w")
    button3= tkinter.Button(text='<==',command=spat)
    button3.pack()
    button3.place(relx=.02, rely=.05, anchor="w")
def filtrovat():
    canvas.create_rectangle(sirka//10,vyska//3,sirka-sirka//10, vyska)
def spat():
    canvas.delete('all')
    entry1.destroy()
    statistiky()
    vtransakcie()
statistiky()
vtransakcie()
button1= tkinter.Button(text='FILTER',command=filterf)
button1.pack()
button1.place(relx=.02, rely=.100, anchor="w")

