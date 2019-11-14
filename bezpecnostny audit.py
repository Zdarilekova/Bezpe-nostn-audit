import tkinter
sirka=1280
vyska=720
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
vtransakcie()
##from tkinter import *  
##  
##top = Tk()  
##sb = Scrollbar(top)  
##sb.pack(side = RIGHT, fill = Y)  
##  
##mylist = Listbox(top, yscrollcommand = sb.set )  
##  
##for line in range(30):  
##    mylist.insert(END, "Number " + str(line))  
##  
##mylist.pack( side = LEFT )  
##sb.config( command = mylist.yview )  
def statistiky():
    canvas.create_text(sirka//2+sirka//4, vyska//10, text='ŠTATISTIKY', font='Arial 20')
        canvas.create_line(sirka//4-200, vyska//10+13,sirka//4+200, vyska//10+13, width=3)
   

