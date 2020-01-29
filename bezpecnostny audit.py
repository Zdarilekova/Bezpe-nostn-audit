import tkinter as tk
from tkinter import *
import calendar
import datetime
import sys
import os
sirka=1280
vyska=720
root=tk.Tk()
canvas=tk.Canvas(root,width=sirka, height=vyska, bg='#71CAE7')
canvas.pack()
    
def frame0():
    global frame, canv,root,menuImg, labelMenuImg, meno, heslo
    
    frame=tk.Frame(root,width=sirka, height=vyska)
    frame.place(x=0,y=0)
    canv=tk.Canvas(frame,width=sirka, height=vyska, bg='#71CAE7')
    canv.pack()
    canv.create_text(sirka//2, 50, text='BEZPEČNOSTNÝ AUDIT', font='Arial 30')
    canv.create_text(sirka//2, vyska//2-50, text='MENO:', font='Arial 30', anchor='w')
    canv.create_text(sirka//2, vyska//2, text='HESLO:', font='Arial 30', anchor='w')
    meno = tk.Entry(canv, font = "Helvetica 15 ", width=25)
    meno.pack()
    meno.place(x = sirka//2 + 150, y = vyska//10*4+10)
    heslo = tk.Entry(canv, font = "Helvetica 15 ", width=25)
    heslo.pack()
    heslo.place(x = sirka//2 + 150, y = vyska//10*4+60)
    menuImg = tk.PhotoImage(master=canv,file='menu.png')
    labelMenuImg = tk.Label(image = menuImg,borderwidth=0)
    labelMenuImgimage = menuImg
    labelMenuImg.pack()
    labelMenuImg.place(x=0.03*sirka,y=vyska-(0.55*vyska), anchor="w")
def login():
    global meno, heslo, canv
    loginName = meno.get()
    loginPassword = heslo.get()
    if (os.path.exists('ZAMESTNANCI_LOCK.txt')):
        canvas.after(2000,login)
    elif(os.path.exists('ZAMESTNANCI_LOCK.txt')==False):
        zamestnanciLockSubor = open('ZAMESTNANCI_LOCK.txt','w+')
        suborlogin=open('ZAMESTNANCI.txt', 'r+')
        riadoksuborlogin=suborlogin.readline().strip()
        polelogin=[]
        for riadoksuborlogin in suborlogin:
            riadoksuborlogin=riadoksuborlogin.strip()
            menoaheslo=riadoksuborlogin.split(';')
            polelogin.append(menoaheslo)
            if loginName==menoaheslo[0] and loginPassword==menoaheslo[1]:
                frame1()   
            else:
                canv.create_text(sirka//4*3-30, vyska//2+35, text='NESPRÁVNE MENO ALEBO HESLO', fill='red', font='Arial 15')
        suborlogin.close() 
        zamestnanciLockSubor.close()
        os.remove('ZAMESTNANCI_LOCK.txt')
frame0()

def frame1():
    global frame, can,root
    frame=tk.Frame(root,width=sirka, height=vyska)
    frame.place(x=0,y=0)
    can=tk.Canvas(frame,width=sirka, height=vyska, bg='#71CAE7')
    can.pack()
    statistiky()
    vtransakcie()
    button1= tk.Button(text='FILTER',background = 'black', foreground = "#71CAE7",command=filterf)
    button1.pack()
    button1.place(relx=.02, rely=.100, anchor="w")
    button3= tk.Button(text='Odhlásiť sa',background = 'black', foreground = "#71CAE7",command=odhlasit)
    button3.pack()
    button3.place(relx=.9, rely=.05, anchor="w")

def vtransakcie():
    global root,poleus
    can.create_line(sirka//4-200, vyska//10+13,sirka//4+200, vyska//10+13, width=3)
    if (os.path.exists('TRANSAKCIE_PAYWALL_LOCK.txt')) and (os.path.exists('TRANSAKCIE_KARTY_LOCK.txt'))and (os.path.exists('TRANSAKCIE_UCTY_LOCK.txt')):
        canvas.after(2000,vtransakcie)
    elif(os.path.exists('TRANSAKCIE_PAYWALL_LOCK.txt')==False) or (os.path.exists('TRANSAKCIE_KARTY_LOCK.txt')==False) or (os.path.exists('TRANSAKCIE_UCTY_LOCK.txt')==False):
        transakcie_paywall_LockSubor = open('TRANSAKCIE_PAYWALL_LOCK.txt','w+')
        transakcie_karty_LockSubor = open('TRANSAKCIE_KARTY_LOCK.txt','w+')
        transakcie_ucty_LockSubor = open('TRANSAKCIE_UCTY_LOCK.txt','w+')
        puspesne=open('TRANSAKCIE_PAYWALL.txt', 'r+')
        puspesne2=open('TRANSAKCIE_KARTY.txt', 'r+')
        puspesne3=open('TRANSAKCIE_UCTY.txt', 'r+')
        pocetuspesne=0
        pocetneuspesne=0
        poleus=[]
        riadok4=puspesne.readline().strip()
        scrollbar = tk.Scrollbar(root)
        scrollbar.place(x=sirka//4+250-2, y=vyska-6, height=vyska-200, width=20)
        trans_list = tk.Listbox(root, font='Arial 15')
        trans_list.place(x=sirka//4-250+2,y=vyska//10+102+6,width=500,height=vyska-vyska//10+102+6)
        for riadok4 in puspesne:
            riadok4 = riadok4.strip()
            l=riadok4.split(';')
            cisuspesne=l[7]
            poleus.append(cisuspesne)
            if cisuspesne=='1':
                pocetuspesne+=1
                
            else:
                pocetneuspesne+=1
                trans_list.insert(END, 'Číslo Transakcie'+'  '+l[3])
                trans_list.insert(END, 'Číslo Účtu Obchodníka'+'  '+l[6])
                trans_list.insert(END, '')  
                trans_list.config(yscrollcommand=scrollbar.set)
                scrollbar.config(command=trans_list.yview)
        
        can.create_text(sirka//4, vyska//10, text='VŠETKY TRANSAKCIE', font='Arial 20')
        can.create_rectangle(sirka//4-250,vyska//10+35, sirka//4+250, vyska//10+65, fill='forestgreen', width=4)
        can.create_text(sirka//4,vyska//10+50, text='ÚSPEšNé TRANSAKCIE:'+' '+str(pocetuspesne),font='Arial 12', fill='white')
        can.create_rectangle(sirka//4-250,vyska//10+85, sirka//4+250, vyska//10+105, fill='firebrick', outline='firebrick', width=5)
        can.create_text(sirka//4,vyska//10+95, text='NEÚSPEšNé TRANSAKCIE: '+str(pocetneuspesne),font='Arial 12', fill='white')
        can.create_rectangle(sirka//4-250,vyska//10+102+4,sirka//4+250, vyska-4, outline='firebrick', width=5)
        can.create_rectangle(sirka//4-250+2,vyska//10+102+6,sirka//4+250-2, vyska-6, outline='black', width=4, fill='white')
        can.create_line(sirka//2,0,sirka//2,vyska,width=3)
        puspesne.close()
        puspesne2.close()
        puspesne3.close()
        transakcie_paywall_LockSubor.close()
        transakcie_karty_LockSubor.close()
        transakcie_ucty_LockSubor.close()
        os.remove('TRANSAKCIE_PAYWALL_LOCK.txt')
        os.remove('TRANSAKCIE_KARTY_LOCK.txt')    
        os.remove('TRANSAKCIE_UCTY_LOCK.txt')    

def statistiky():
    can.create_rectangle(sirka//2+200, vyska//10-20,sirka//2+435, vyska//10+13, width=3, fill='white')
    can.create_text(sirka//2+sirka//4, vyska//10, text='ŠTATISTIKY', font='Arial 20')
##   ............
    if (os.path.exists('TRANSAKCIE_UCTY_LOCK.txt')):
        canvas.after(2000,statistiky)
    elif(os.path.exists('TRANSAKCIE_UCTY_LOCK.txt')==False):
        transakcie_ucty_LockSubor = open('TRANSAKCIE_UCTY_LOCK.txt','w+')
        vklad=open('TRANSAKCIE_UCTY.txt','r+')
        riadok1=vklad.readline().strip()
        vyskav=0
        pocetvkladov=0
        for riadok1 in vklad:
            b=riadok1.split(';')
            suma=b[5]
            ##idst=b[6] ##id suvisiacej transakcie
            suma1=str(suma)
            
            if float(suma1)>0:
                vyskav+=float(suma)
                pocetvkladov+=1
        can.create_text(sirka//2+15, vyska//10+50, text='Priemerná výška vkladu:'+' '+str(vyskav//pocetvkladov), font='Arial 20',anchor='w')
        vklad.close()
        transakcie_ucty_LockSubor.close()
        os.remove('TRANSAKCIE_UCTY_LOCK.txt')

## ....................
    if (os.path.exists('KARTY_LOCK.txt')):
        canvas.after(2000,statistiky)
    elif(os.path.exists('KARTY_LOCK.txt')==False):
        karty_LockSubor = open('KARTY_LOCK.txt','w+')
        dlh=open('KARTY.txt', 'r+')
        riadok=dlh.readline().strip()
        pocetr=0
        spolu=0
        for riadok in dlh:
            a=riadok.split(';')
            dlznasuma=a[7]
            pocetr+=1
            spolu+=float(dlznasuma)
        dlzobap=spolu//pocetr
        can.create_text(sirka//2+15, vyska//10+90, text='Priemerný dlh na kreditnej karte:'+' '+str(dlzobap), font='Arial 20',anchor='w')
        dlh.close()
        karty_LockSubor.close()
        os.remove('KARTY_LOCK.txt')
##..........................................
    if (os.path.exists('TRANSAKCIE_UCTY_LOCK.txt')) and (os.path.exists('TRANSAKCIE_KARTY_LOCK.txt')) and(os.path.exists('TRANSAKCIE_PAYWALL_LOCK.txt')):
        canvas.after(2000,statistiky)
    elif(os.path.exists('TRANSAKCIE_UCTY_LOCK.txt')==False) and (os.path.exists('TRANSAKCIE_KARTY_LOCK.txt')==False) and (os.path.exists('TRANSAKCIE_PAYWALL_LOCK.txt')==False):
        transakcie_ucty_LockSubor = open('TRANSAKCIE_UCTY_LOCK.txt','w+')
        transakcie_karty_LockSubor = open('TRANSAKCIE_KARTY_LOCK.txt','w+')
        transakcie_paywall_LockSubor = open('TRANSAKCIE_PAYWALL_LOCK.txt','w+')
        pvt1=open('TRANSAKCIE_UCTY.txt','r')
        pvt2=open('TRANSAKCIE_PAYWALL.txt','r')
        pvt3=open('TRANSAKCIE_KARTY.txt','r')
        r1=pvt1.readline().strip()
        r2=pvt2.readline().strip()
        r3=pvt3.readline().strip()
        spolu=0
        spolu1=0
        spolu2=0
        spolu3=0
        priemer=0
        for r1 in pvt1:
            h1=r1.split(';')
            pvt11=h1[5]
            if float(h1[5])>=0:
                spolu1+=float(pvt11)
                priemer+=1
        for r2 in pvt2:
            h2=r2.split(';')
            pvt22=h2[2]
            if float(h2[2])>=0:
                spolu2+=float(pvt22)
                priemer+=1
        for r3 in pvt3:
            h3=r3.split(';')
            pvt33=h3[3]
            if float(h3[3])>=0:
                spolu3+=float(pvt33)
                priemer+=1
        spolu=spolu1+spolu2+spolu3
        can.create_text(sirka//2+15, vyska//10+130, text='Priemerná výška transakcie:  '+str(spolu//priemer), font='Arial 20',anchor='w')
        pvt1.close()
        transakcie_ucty_LockSubor.close()
        os.remove('TRANSAKCIE_UCTY_LOCK.txt')
        pvt2.close()
        transakcie_paywall_LockSubor.close()
        os.remove('TRANSAKCIE_PAYWALL_LOCK.txt')
        pvt3.close()
        transakcie_karty_LockSubor.close()
        os.remove('TRANSAKCIE_KARTY_LOCK.txt')
##........................................................................................................................
    if (os.path.exists('TRANSAKCIE_UCTY_LOCK.txt')) and(os.path.exists('TRANSAKCIE_PAYWALL_LOCK.txt')):
        canvas.after(2000,statistiky)
    elif(os.path.exists('TRANSAKCIE_UCTY_LOCK.txt')==False)and (os.path.exists('TRANSAKCIE_PAYWALL_LOCK.txt')==False):
        transakcie_ucty_LockSubor = open('TRANSAKCIE_UCTY_LOCK.txt','w+')
        transakcie_paywall_LockSubor = open('TRANSAKCIE_PAYWALL_LOCK.txt','w+')
        ppdt=open('TRANSAKCIE_PAYWALL.txt','r+')
        ppdt2=open('TRANSAKCIE_UCTY.txt','r+')
        ri1=ppdt.readline().strip()
        ri2=ppdt2.readline().strip()
        poledt=[]
        viac=1
        for ri1 in ppdt:
            ri1=ri1.strip()
            m=ri1.split(';')
            ppdt1=m[8]
            poledt.append(ppdt1)
        for ri2 in ppdt2:
            ri2=ri2.strip()
            gg=ri2.split(';')
            ppdt22=gg[7]
            poledt.append(ppdt22)
        if poledt!=[]:
            for i in range(len(poledt)-1):
                if poledt[i]!=poledt[i+1]:
                    viac+=1
        print(viac)
        priemer=len(poledt)//viac
        can.create_text(sirka//2+15, vyska//10+170, text='Priemerný počet denných transakcií:  '+str(priemer), font='Arial 20',anchor='w')
        ppdt.close()
        transakcie_ucty_LockSubor.close()
        os.remove('TRANSAKCIE_UCTY_LOCK.txt')
        ppdt2.close()
        transakcie_paywall_LockSubor.close()
        os.remove('TRANSAKCIE_PAYWALL_LOCK.txt')
##.....................................    
def vsetkytlist():
    global frame, can, root, datumod, cislokarty, poleck, polecu, cislouctu,d,c, cislokarty, cisuctu, cislouctu1, cislokarty1,riadok3, riadok2, poles,poledate, poled, datumod, datumdo, sumaod, sumado

    scrollbar = tk.Scrollbar(root)
    scrollbar.place(x=sirka-120,y=200, height=vyska-200, width=20)
    ##    ...................
    if (os.path.exists('TRANSAKCIE_PAYWALL_LOCK.txt')) and(os.path.exists('UCTY_LOCK.txt'))and(os.path.exists('KARTY_LOCK.txt')) and (os.path.exists('TRANSAKCIE_KARTY_LOCK.txt')):
        canvas.after(2000,statistiky)
    elif(os.path.exists('UCTY_LOCK.txt')==False)and (os.path.exists('TRANSAKCIE_PAYWALL_LOCK.txt')==False) and (os.path.exists('KARTY_LOCK.txt')==False) and (os.path.exists('TRANSAKCIE_KARTY_LOCK.txt')==False):
        transakcie_paywall_LockSubor = open('TRANSAKCIE_PAYWALL_LOCK.txt','w+')
        karty_LockSubor = open('KARTY_LOCK.txt','w+')
        ucty_LockSubor = open('UCTY_LOCK.txt','w+')
        transakcie_karty_LockSubor = open('TRANSAKCIE_KARTY_LOCK.txt','w+')
        cislokarty1=open('KARTY.txt', 'r')
        riadok2=cislokarty1.readline().strip()
        cislouctu1=open('UCTY.txt', 'r')
        riadok3=cislouctu1.readline().strip()
        datum1=open('TRANSAKCIE_PAYWALL.txt','r')
        riadok5=datum1.readline().strip()
        cislokarty2=open('TRANSAKCIE_KARTY.txt', 'r')
        riadok6=cislokarty2.readline().strip()
        trans_list = tk.Listbox(root, font='Arial 15')
        trans_list.place(x=100,y=200,width=sirka-220,height=vyska-200)
        polecu=[]
        poleck=[]
        poled=[]
        poles=[]
        poledate=[]
        poleidkarty=[]
        poleidkartytk=[]  #pri transakciach kariet
        polesumatk=[]
        poleiducetobchodnika=[]
        poledatumtk=[]
        poledatumtransakcie=[]
        for x in range(50):
##            for riadok3 in cislouctu1:
##                d=riadok3.split(';')
##                cisuctu=d[2]
##                polecu.append(cisuctu)
            for riadok5 in datum1:
                t=riadok5.split(';')
                datum=t[8]
                poled.append(datum)
                suma=t[2]
                poles.append(suma)
                idkarty=t[1]
                poleidkarty.append(idkarty)
                cisuctu=t[6]
                polecu.append(cisuctu)
            for riadok2 in cislokarty1:
                c=riadok2.split(';')
                ciskarty=c[3]
                poleck.append(ciskarty)
            for riadok6 in cislokarty2:
                tkr=riadok6.split(';')
                idckokarty=tkr[1]  #pri transakciach kariet
                poleidkartytk.append(idckokarty)
                sumatk=tkr[2]
                polesumatk.append(sumatk)
                iducetobchodnika=tkr[3]
                poleiducetobchodnika.append(iducetobchodnika)
                datum2=tkr[4]
                poledatumtk.append(datum2)
        for i in range(len(poles)):
            rozdel = list(poled[i])
            den=rozdel[0:2]
            x=''
            denjoin=x.join(den)
            mesiac=rozdel[2:4]
            mesiacjoin=x.join(mesiac)
            rok=rozdel[4:8]
            rokjoin=x.join(rok)
            poledate.append(denjoin+'.'+mesiacjoin+'.'+rokjoin)
            trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkarty[i])-1]+70*' ' +'SUMA'+'  '+poles[i]+'€')
            trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[i]+50*' ' +'DÁTUM'+'  '+poledate[i])
            trans_list.insert(END, '')
        for i in range(len(poleidkartytk)):
            rozdel = list(poledatumtk[i])
            den=rozdel[0:2]
            x=''
            denjoin=x.join(den)
            mesiac=rozdel[2:4]
            mesiacjoin=x.join(mesiac)
            rok=rozdel[4:8]
            rokjoin=x.join(rok)
            poledatumtransakcie.append(denjoin+'.'+mesiacjoin+'.'+rokjoin)
            trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkartytk[i])-1]+70*' ' +'SUMA'+'  '+polesumatk[i]+'€')
            trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[int(poleiducetobchodnika[i])-1]+50*' ' +'DÁTUM'+'  '+poledatumtransakcie[i])
            trans_list.insert(END, '')
        trans_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=trans_list.yview)
        datum1.close()
        transakcie_paywall_LockSubor.close()
        os.remove('TRANSAKCIE_PAYWALL_LOCK.txt')
        cislouctu1.close()
        ucty_LockSubor.close()
        os.remove('UCTY_LOCK.txt')
        cislokarty1.close()
        karty_LockSubor.close()
        os.remove('KARTY_LOCK.txt')
        cislokarty2.close()
        transakcie_karty_LockSubor.close()
        os.remove('TRANSAKCIE_KARTY_LOCK.txt')
def filterf():
    global frame, can, root, datumod, cislokarty, poleck, polecu, cislouctu,d,c, cislokarty,poleidkarty,polesumatk, cisuctu, cislouctu1, cislokarty1,riadok3, riadok2, poles,poledate, poled,poleidkartytk,poleiducetobchodnika,poledatumtk,poledatumtransakcie, datumod, datumdo, sumaod, sumado
    frame.destroy
    can.destroy
    frame=tk.Frame(root,width=sirka, height=vyska)
    frame.place(x=0,y=0)
    can=tk.Canvas(frame,width=sirka, height=vyska, bg='#71CAE7')
    can.pack()
    scrollbar = tk.Scrollbar(root)
    scrollbar.place(x=sirka-120,y=200, height=vyska-200, width=20)
    ##    ...................
    if (os.path.exists('TRANSAKCIE_PAYWALL_LOCK.txt')) and(os.path.exists('UCTY_LOCK.txt'))and(os.path.exists('KARTY_LOCK.txt')) and (os.path.exists('TRANSAKCIE_KARTY_LOCK.txt')):
        canvas.after(2000,statistiky)
    elif(os.path.exists('UCTY_LOCK.txt')==False)and (os.path.exists('TRANSAKCIE_PAYWALL_LOCK.txt')==False) and (os.path.exists('KARTY_LOCK.txt')==False) and (os.path.exists('TRANSAKCIE_KARTY_LOCK.txt')==False):
        transakcie_paywall_LockSubor = open('TRANSAKCIE_PAYWALL_LOCK.txt','w+')
        karty_LockSubor = open('KARTY_LOCK.txt','w+')
        ucty_LockSubor = open('UCTY_LOCK.txt','w+')
        transakcie_karty_LockSubor = open('TRANSAKCIE_KARTY_LOCK.txt','w+')
        cislokarty1=open('KARTY.txt', 'r')
        riadok2=cislokarty1.readline().strip()
        cislouctu1=open('UCTY.txt', 'r')
        riadok3=cislouctu1.readline().strip()
        datum1=open('TRANSAKCIE_PAYWALL.txt','r')
        riadok5=datum1.readline().strip()
        cislokarty2=open('TRANSAKCIE_KARTY.txt', 'r')
        riadok6=cislokarty2.readline().strip()
        trans_list = tk.Listbox(root, font='Arial 15')
        trans_list.place(x=100,y=200,width=sirka-220,height=vyska-200)
        polecu=[]
        poleck=[]
        poled=[]
        poles=[]
        poledate=[]
        poleidkarty=[]
        poleidkartytk=[]  #pri transakciach kariet
        polesumatk=[]
        poleiducetobchodnika=[]
        poledatumtk=[]
        poledatumtransakcie=[]
        for x in range(50):
##            for riadok3 in cislouctu1:
##                d=riadok3.split(';')
##                cisuctu=d[2]
##                polecu.append(cisuctu)
            for riadok5 in datum1:
                t=riadok5.split(';')
                datum=t[8]
                poled.append(datum)
                suma=t[2]
                poles.append(suma)
                idkarty=t[1]
                poleidkarty.append(idkarty)
                cisuctu=t[6]
                polecu.append(cisuctu)
            for riadok2 in cislokarty1:
                c=riadok2.split(';')
                ciskarty=c[3]
                poleck.append(ciskarty)
            for riadok6 in cislokarty2:
                tkr=riadok6.split(';')
                idckokarty=tkr[1]  #pri transakciach kariet
                poleidkartytk.append(idckokarty)
                sumatk=tkr[2]
                polesumatk.append(sumatk)
                iducetobchodnika=tkr[3]
                poleiducetobchodnika.append(iducetobchodnika)
                datum2=tkr[4]
                poledatumtk.append(datum2)
        for i in range(len(poles)):
            rozdel = list(poled[i])
            den=rozdel[0:2]
            x=''
            denjoin=x.join(den)
            mesiac=rozdel[2:4]
            mesiacjoin=x.join(mesiac)
            rok=rozdel[4:8]
            rokjoin=x.join(rok)
            poledate.append(denjoin+'.'+mesiacjoin+'.'+rokjoin)
            trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkarty[i])-1]+70*' ' +'SUMA'+'  '+poles[i]+'€')
            trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[i]+70*' ' +'DÁTUM'+'  '+poledate[i])
            trans_list.insert(END, '')
        for i in range(len(poleidkartytk)):
            rozdel = list(poledatumtk[i])
            den=rozdel[0:2]
            x=''
            denjoin=x.join(den)
            mesiac=rozdel[2:4]
            mesiacjoin=x.join(mesiac)
            rok=rozdel[4:8]
            rokjoin=x.join(rok)
            poledatumtransakcie.append(denjoin+'.'+mesiacjoin+'.'+rokjoin)
            trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkartytk[i])-1]+70*' ' +'SUMA'+'  '+polesumatk[i]+'€')
            trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[int(poleiducetobchodnika[i])-1]+50*' ' +'DÁTUM'+'  '+poledatumtransakcie[i])
            trans_list.insert(END, '')
        trans_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=trans_list.yview)
##................................................................    
        can.create_text(sirka//4, vyska//10+15, text='ČÍSLO KARTY:', font='Arial 20',anchor='e')
        cislokarty=tk.Entry(font="Helvetica 15 ", width=15)
        cislokarty.pack()
        cislokarty.place(x = sirka//4+20 , y = vyska//10)
        
        can.create_text(sirka//4, vyska//10+55, text='ČÍSLO ÚČTU:', font='Arial 20',anchor='e')
        cislouctu=tk.Entry(font="Helvetica 15 ", width=15)
        cislouctu.pack()
        cislouctu.place(x = sirka//4+20 , y = vyska//10+40)
        
        can.create_text(sirka//2+sirka//11, vyska//10+15, text='SUMA OD', font='Arial 20',anchor='e')
        sumaod=tk.Entry(font="Helvetica 15 ", width=10)
        sumaod.pack()
        sumaod.place(x = sirka//2+130 , y = vyska//10)
        
        can.create_text(sirka//2+sirka//3, vyska//10+15, text='SUMA DO', font='Arial 20',anchor='e')
        sumado=tk.Entry(font="Helvetica 15 ", width=10)
        sumado.pack()
        sumado.place(x = sirka//7*6 , y = vyska//10)
        
        can.create_text(sirka//2+sirka//11, vyska//10+55, text='DÁTUM OD', font='Arial 20',anchor='e')
        datumod=tk.Entry(font="Helvetica 15 ", width=10)
        datumod.pack()
        datumod.place(x = sirka//2+130 , y = vyska//10+40)
        
        can.create_text(sirka//2+sirka//3, vyska//10+55, text='DÁTUM DO', font='Arial 20',anchor='e')
        datumdo=tk.Entry(font="Helvetica 15 ", width=10)
        datumdo.pack()
        datumdo.place(x = sirka//7*6 , y = vyska//10+40)
        
        button2= tk.Button(text='FILTROVAŤ',background = 'black', foreground = "#71CAE7",command=filtrovat)
        button2.pack()
        button2.place(relx=.9, rely=.250, anchor="w")
        button3= tk.Button(text='<==', background = 'black', foreground = "#71CAE7",command=spat)
        button3.pack()
        button3.place(relx=.02, rely=.05, anchor="w")
        buttonvsetkytransakcie= tk.Button(text='všetky transakcie',background = 'black', foreground = "#71CAE7", command= vsetkytlist)
        buttonvsetkytransakcie.pack()
        buttonvsetkytransakcie.place(relx=.1, rely=.250, anchor="w")
        def kalendar(rozlis1):
            global rozlis
            rozlis=rozlis1
            if sys.version[0] == '2':
                import Tkinter as tk
            else:
                import tkinter as tk

            class Calendar:
                def __init__(self, parent, values):
                    self.values = values
                    self.parent = parent
                    self.cal = calendar.TextCalendar(calendar.SUNDAY)
                    self.year = datetime.date.today().year
                    self.month = datetime.date.today().month
                    self.wid = []
                    self.day_selected = 1
                    self.month_selected = self.month
                    self.year_selected = self.year
                    self.day_name = ''
                    self.setup(self.year, self.month)

                def clear(self):
                    for w in self.wid[:]:
                        w.grid_forget()
                        #w.destroy()
                        self.wid.remove(w)

                def go_prev(self):
                    if self.month > 1:
                        self.month -= 1
                    else:
                        self.month = 12
                        self.year -= 1
                    #self.selected = (self.month, self.year)
                    self.clear()
                    self.setup(self.year, self.month)

                def go_next(self):
                    if self.month < 12:
                        self.month += 1
                    else:
                        self.month = 1
                        self.year += 1

                    #self.selected = (self.month, self.year)
                    self.clear()
                    self.setup(self.year, self.month)

                def selection(self, day, name):
                    self.day_selected = day
                    self.month_selected = self.month
                    self.year_selected = self.year
                    self.day_name = name
                    #data
                    self.values['day_selected'] = day
                    self.values['month_selected'] = self.month
                    self.values['year_selected'] = self.year
                    self.values['day_name'] = name
                    self.values['month_name'] = calendar.month_name[self.month_selected]
                    self.clear()

                    self.setup(self.year, self.month)

                def setup(self, y, m):
                    left = tk.Button(self.parent, text='<', command=self.go_prev)
                    self.wid.append(left)
                    left.grid(row=0, column=1)
                    header = tk.Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
                    self.wid.append(header)
                    header.grid(row=0, column=2, columnspan=3)
                    right = tk.Button(self.parent, text='>', command=self.go_next)
                    self.wid.append(right)
                    right.grid(row=0, column=5)
                    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
                    for num, name in enumerate(days):
                        t = tk.Label(self.parent, text=name[:3])
                        self.wid.append(t)
                        t.grid(row=1, column=num)
                    for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
                        for d, day in enumerate(week):
                            if day:
                                #print(calendar.day_name[day])
                                b = tk.Button(self.parent, width=1, text=day, command=lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
                                self.wid.append(b)
                                b.grid(row=w, column=d)

                    sel = tk.Label(self.parent, height=2, text='{} {} {} {}'.format(
                        self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
                    self.wid.append(sel)
                    sel.grid(row=8, column=0, columnspan=7)
                    ok = tk.Button(self.parent, width=5, text='OK', command= self.kill_and_save)
                    self.wid.append(ok)
                    ok.grid(row=9, column=2, columnspan=3, pady=10)

                def kill_and_save(self):
                    self.parent.destroy()

            if __name__ == '__main__':

                class Control:
                    def __init__(self, parent):
                        self.parent = parent
                        self.choose_btn = tk.Button(self.parent, text='VYBER',command=self.popup)
                        self.show_btn = tk.Button(self.parent, text='VYPÍŠ',command=self.print_selected_date)
                        self.choose_btn.grid()
                        self.show_btn.grid()
                        self.data = {}
                    def popup(self):
                        child = tk.Toplevel()
                        cal = Calendar(child, self.data)

                    def print_selected_date(self):
                        print(self.data)
                        if rozlis==1:
                            datumod = tk.Entry(root)
                            datumod.delete(0, tk.END)
                        else:
                            datumdo = tk.Entry(root)
                            datumdo.delete(0, tk.END)
                        pom = ''  
                        pom+=str(self.data['day_selected'])+'.'+str(self.data['month_selected'])+'.'+str(self.data['year_selected'])
                        
                        change_entry(pom)
                root=tk.Tk()         
                app = Control(root)
        kalendarod=tk.Button(text='kalendár',background = 'black', foreground = "#71CAE7", command=lambda: kalendar(0))
        kalendarod.pack()
        kalendarod.place(relx=.85, rely=.200)
        kalendardo=tk.Button(text='kalendár',background = 'black', foreground = "#71CAE7", command=lambda: kalendar(1))
        kalendardo.pack()
        kalendardo.place(relx=.6, rely=.200)
        datum1.close()
        transakcie_paywall_LockSubor.close()
        os.remove('TRANSAKCIE_PAYWALL_LOCK.txt')
        cislouctu1.close()
        ucty_LockSubor.close()
        os.remove('UCTY_LOCK.txt')
        cislokarty1.close()
        karty_LockSubor.close()
        os.remove('KARTY_LOCK.txt')
        cislokarty2.close()
        transakcie_karty_LockSubor.close()
        os.remove('TRANSAKCIE_KARTY_LOCK.txt')
def change_entry(pom):
    global poledatumod, poledatumdo
    
    if rozlis==1:
        datumod.delete(0, tk.END)
        datumod.insert(0,pom)
        poledatumod=pom.split('.')
        
    else:
        datumdo.delete(0, tk.END)
        datumdo.insert(0,pom)
        poledatumdo=pom.split('.')
        
def filtrovat():
    global frame, can, cislokarty, ciskarty, poleck, polecu, cislouctu, poled, poles,poleidkarty,polesumatk, datumod, datumdo, sumaod, sumado, poledatumod, poledatumdo,can, poledate, poleidkartytk,poleiducetobchodnika,poledatumtk,poledatumtransakcie
    scrollbar = tk.Scrollbar(root)
    scrollbar.place(x=sirka-120,y=200, height=vyska-200, width=20)
    fcisk=cislokarty.get()
    fcisu=cislouctu.get()
    fdod=datumod.get()
    fddo=datumdo.get()
    fsod=sumaod.get()
    fsdo=sumado.get()
    print(fcisk)
    ##    ...................
    if (os.path.exists('UCTY_LOCK.txt'))and(os.path.exists('KARTY_LOCK.txt')):
        canvas.after(2000,statistiky)
    elif(os.path.exists('UCTY_LOCK.txt')==False)and (os.path.exists('KARTY_LOCK.txt')==False):
        karty_LockSubor = open('KARTY_LOCK.txt','w+')
        ucty_LockSubor = open('UCTY_LOCK.txt','w+')
        cislokarty1=open('KARTY.txt', 'r+')
        riadok2=cislokarty1.readline().strip()
        cislouctu1=open('UCTY.txt', 'r+')
        riadok3=cislouctu1.readline().strip()
        trans_list = tk.Listbox(root, font='Arial 15')
        trans_list.place(x=100,y=200,width=sirka-220,height=vyska-200)
        poledate=[]
        for i in range(len(poled)):
            rozdel = list(poled[i])
            den=rozdel[0:2]
            x=''
            denjoin=x.join(den)
            mesiac=rozdel[2:4]
            mesiacjoin=x.join(mesiac)
            rok=rozdel[4:8]
            rokjoin=x.join(rok)
            poledate.append(denjoin+'.'+mesiacjoin+'.'+rokjoin)
            k1=datumod.get()
            k2=datumdo.get()
            poledatumod=k1.split('.')
            poledatumdo=k2.split('.')
            if fcisu==polecu[i]:
                trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[i]+70*' ' +'DÁTUM'+'  '+ poledate[i])
                trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkarty[i])-1]+70*' ' +'SUMA'+'  '+poles[i]+'€')
                trans_list.insert(END, '')
            if fcisk==poleck[int(poleidkarty[i])-1]:
                trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkarty[i])-1]+70*' ' +'SUMA'+'  '+poles[i]+'€')
                trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[i]+70*' ' +'DÁTUM'+'  '+ poledate[i])
                trans_list.insert(END, '')
            if fdod!='' and fddo!='':
                x1=datetime.datetime(int(poledatumod[2]),int(poledatumod[1]) , int(poledatumod[0]))
                x2=datetime.datetime(int(poledatumdo[2]),int(poledatumdo[1]) , int(poledatumdo[0]))
                vysl=datetime.datetime(int(rokjoin),int(mesiacjoin) , int(denjoin))
                if x1<=vysl and x2>=vysl:
                    if fsod!=''and fsdo!='':
                        if float(fsod)<=float(poles[i]) and float(fsdo)>=float(poles[i]):
                            trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[i]+70*' ' +'DÁTUM'+'  '+ poledate[i])
                            trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkarty[i])-1]+70*' ' +'SUMA'+'  '+poles[i]+'€')
                            trans_list.insert(END, '')
                    else:
                        trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[i]+70*' ' +'DÁTUM'+'  '+ poledate[i])
                        trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkarty[i])-1]+70*' ' +'SUMA'+'  '+poles[i]+'€')
                        trans_list.insert(END, '')
            else:
                if fsod!=''and fsdo!='':
                    if float(fsod)<=float(poles[i]) and float(fsdo)>=float(poles[i]):
                            trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[i]+70*' ' +'DÁTUM'+'  '+ poledate[i])
                            trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkarty[i])-1]+70*' ' +'SUMA'+'  '+poles[i]+'€')
                            trans_list.insert(END, '')
                    else:
                        print('oooooooooooooooooo')
##                        trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[i]+70*' ' +'DÁTUM'+'  '+ poledate[i])
##                        trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkarty[i])-1]+70*' ' +'SUMA'+'  '+poles[i]+'€')
##                        trans_list.insert(END, '')
        for i in range(len(poleidkartytk)):
            rozdel = list(poledatumtk[i])
            den=rozdel[0:2]
            x=''
            denjoin=x.join(den)
            mesiac=rozdel[2:4]
            mesiacjoin=x.join(mesiac)
            rok=rozdel[4:8]
            rokjoin=x.join(rok)
            k1=datumod.get()
            k2=datumdo.get()
            poledatumod=k1.split('.')
            poledatumdo=k2.split('.')
            poledatumtransakcie.append(denjoin+'.'+mesiacjoin+'.'+rokjoin)
            if fcisu==polecu[int(poleiducetobchodnika[i])-1]:
                trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[int(poleiducetobchodnika[i])-1]+70*' ' +'DÁTUM'+'  '+poledatumtransakcie[i])
                trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkartytk[i])-1]+70*' ' +'SUMA'+'  '+polesumatk[i]+'€')
                trans_list.insert(END, '')
            if fcisk==poleck[int(poleidkartytk[i])-1]:
                trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkartytk[i])-1]+70*' ' +'SUMA'+'  '+polesumatk[i]+'€')
                trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[int(poleiducetobchodnika[i])-1]+70*' ' +'DÁTUM'+'  '+poledatumtransakcie[i])
                trans_list.insert(END, '')
            if fdod!='' and fddo!='':
                x1=datetime.datetime(int(poledatumod[2]),int(poledatumod[1]) , int(poledatumod[0]))
                x2=datetime.datetime(int(poledatumdo[2]),int(poledatumdo[1]) , int(poledatumdo[0]))
                vysl=datetime.datetime(int(rokjoin),int(mesiacjoin) , int(denjoin))
                if x1<=vysl and x2>=vysl:
                    if fsod!=''and fsdo!='':
                        if float(fsod)<=float(polesumatk[i]) and float(fsdo)>=float(polesumatk[i]):
                            trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[int(poleiducetobchodnika[i])-1]+70*' ' +'DÁTUM'+'  '+poledatumtransakcie[i])
                            trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkartytk[i])-1]+70*' ' +'SUMA'+'  '+polesumatk[i]+'€')
                            trans_list.insert(END, '')
                    else:
                        trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[int(poleiducetobchodnika[i])-1]+70*' ' +'DÁTUM'+'  '+poledatumtransakcie[i])
                        trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkartytk[i])-1]+70*' ' +'SUMA'+'  '+polesumatk[i]+'€')
                        trans_list.insert(END, '')
            else:
                if fsod!=''and fsdo!='':
                    if float(fsod)<=float(polesumatk[i]) and float(fsdo)>=float(polesumatk[i]):
                            trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[int(poleiducetobchodnika[i])-1]+70*' ' +'DÁTUM'+'  '+poledatumtransakcie[i])
                            trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkartytk[i])-1]+70*' ' +'SUMA'+'  '+polesumatk[i]+'€')
                            trans_list.insert(END, '')  
                    else:
                        print('oooooooooooooooooofhhdukj')
##                        trans_list.insert(END, 'Číslo Účtu'+'  '+polecu[int(poleidkartytk[i])-1]+70*' ' +'DÁTUM'+'  '+ poledatumtransakcie[i])
##                        trans_list.insert(END, 'Číslo Karty'+'  '+poleck[int(poleidkartytk[i])-1]+70*' ' +'SUMA'+'  '+polesumatk[i]+'€')
##                        trans_list.insert(END, '')
        trans_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=trans_list.yview)
        cislouctu1.close()
        ucty_LockSubor.close()
        os.remove('UCTY_LOCK.txt')
        cislokarty1.close()
        karty_LockSubor.close()
        os.remove('KARTY_LOCK.txt')
def spat():
    global frame, can
    frame.destroy
    can.destroy
    frame=tk.Frame(root,width=sirka, height=vyska)
    frame.place(x=0,y=0)
    can=tk.Canvas(frame,width=sirka, height=vyska, bg='#71CAE7')
    can.pack()
    statistiky()
    vtransakcie()
    button1= tk.Button(text='FILTER',background = 'black', foreground = "#71CAE7",command=filterf)
    button1.pack()
    button1.place(relx=.02, rely=.100, anchor="w")
    button3= tk.Button(text='Odhlásiť sa',background = 'black', foreground = "#71CAE7",command=odhlasit)
    button3.pack()
    button3.place(relx=.9, rely=.05, anchor="w")
def odhlasit():
    global frame, canv
    frame.destroy
    can.destroy
    frame0()
    loginb= tk.Button(text='PRIHLÁSIŤ SA',background = 'black', foreground = "#71CAE7",command=login)
    loginb.pack()
    loginb.place(relx=.85, rely=.470, anchor="w")
    loginb.config( height =5, width = 20 )
global data
loginb= tk.Button( text='PRIHLÁSIŤ SA', background = 'black', foreground = "#71CAE7",command=login)
loginb.pack()
loginb.place(relx=.85, rely=.470, anchor="w")
loginb.config( height =5, width = 20 )

root.mainloop()
