import tkinter as tk
from tkinter import *
import calendar
import datetime
import sys
sirka=1280
vyska=720
root=tk.Tk()
canvas=tk.Canvas(root,width=sirka, height=vyska, bg='#71CAE7')
canvas.pack()

def frame0():
    global frame, canv,root
    frame=tk.Frame(root,width=sirka, height=vyska)
    frame.place(x=0,y=0)
    canv=tk.Canvas(frame,width=sirka, height=vyska, bg='#71CAE7')
    canv.pack()
    canv.create_text(sirka//2, 50, text='BEZPEČNOSTNÝ AUDIT', font='Arial 30')
    canv.create_text(sirka//2, vyska//2-50, text='MENO:', font='Arial 30', anchor='w')
    canv.create_text(sirka//2, vyska//2, text='HESLO:', font='Arial 30', anchor='w')
    meno=tk.Entry(font="Helvetica 15 ", width=30).place(relx=.62,rely=.410, width=250)
    heslo=tk.Entry(font="Helvetica 15 ", width=30).place(relx=.62,rely=.480, width=250)
    obr = tk.PhotoImage(file='menu.png')
    obr_id = canv.create_image(500, 250, image=obr)
frame0()
def frame1():
    global frame, can,root
    frame=tk.Frame(root,width=sirka, height=vyska)
    frame.place(x=0,y=0)
    can=tk.Canvas(frame,width=sirka, height=vyska, bg='#71CAE7')
    can.pack()
    statistiky()
    vtransakcie()
    button1= tk.Button(text='FILTER',command=filterf)
    button1.pack()
    button1.place(relx=.02, rely=.100, anchor="w")

def vtransakcie():
    can.create_line(sirka//4-200, vyska//10+13,sirka//4+200, vyska//10+13, width=3)
    can.create_text(sirka//4, vyska//10, text='VŠETKY TRANSAKCIE BANKY', font='Arial 20')
    can.create_rectangle(sirka//4-250,vyska//10+35, sirka//4+250, vyska//10+65, fill='forestgreen', width=4)
    can.create_text(sirka//4,vyska//10+50, text='ÚSPEšNé TRANSAKCIE: (pocet)',font='Arial 12', fill='white')
    can.create_rectangle(sirka//4-250,vyska//10+85, sirka//4+250, vyska//10+105, fill='firebrick', outline='firebrick', width=5)
    can.create_text(sirka//4,vyska//10+95, text='NEÚSPEšNé TRANSAKCIE: ',font='Arial 12', fill='white')
    can.create_rectangle(sirka//4-250,vyska//10+102+4,sirka//4+250, vyska-4, outline='firebrick', width=5)
    can.create_rectangle(sirka//4-250+2,vyska//10+102+6,sirka//4+250-2, vyska-6, outline='black', width=4, fill='white')
    can.create_line(sirka//2,0,sirka//2,vyska,width=3)
    
def statistiky():
    can.create_rectangle(sirka//2+200, vyska//10-20,sirka//2+435, vyska//10+13, width=3, fill='white')
    can.create_text(sirka//2+sirka//4, vyska//10, text='ŠTATISTIKY', font='Arial 20')
    can.create_text(sirka//2+15, vyska//10+50, text='Priemerná výška vkladu:', font='Arial 20',anchor='w')
    can.create_text(sirka//2+15, vyska//10+90, text='Priemerný dlh na kreditnej karte:', font='Arial 20',anchor='w')
    can.create_text(sirka//2+15, vyska//10+130, text='Priemerná výška transakcie:', font='Arial 20',anchor='w')
    can.create_text(sirka//2+15, vyska//10+170, text='Priemerný počet denných transakcií:', font='Arial 20',anchor='w')
##    can.create_text(sirka//2+15, vyska//10+110, text='Priemerná výška transakcie:', font='SourceSansPro 20',anchor='w')

def filterf():
    global frame, can, root, datumod
    frame.destroy
    can.destroy
    frame=tk.Frame(root,width=sirka, height=vyska)
    frame.place(x=0,y=0)
    can=tk.Canvas(frame,width=sirka, height=vyska, bg='#71CAE7')
    can.pack()
    can.create_rectangle(0,0,sirka,vyska, outline='skyblue', fill='skyblue')
    can.create_text(sirka//4, vyska//10+15, text='ČÍSLO KARTY:', font='Arial 20',anchor='e')
    cislokarty=tk.Entry(font="Helvetica 15 ", width=15).place(relx=.25,rely=.1, width=250)
    can.create_text(sirka//4, vyska//10+45, text='ČÍSLO ÚČTU:', font='Arial 20',anchor='e')
    cislouctu=tk.Entry(font="Helvetica 15 ", width=15).place(relx=.25,rely=.15, width=250)
    can.create_text(sirka//2+sirka//11, vyska//10+15, text='SUMA OD', font='Arial 20',anchor='e')
    sumaod=tk.Entry(font="Helvetica 15 ", width=10).place(relx=.60,rely=.1)
    can.create_text(sirka//2+sirka//3, vyska//10+15, text='SUMA DO', font='Arial 20',anchor='e')
    sumado=tk.Entry(font="Helvetica 15 ", width=10).place(relx=.85,rely=.1)
    can.create_text(sirka//2+sirka//11, vyska//10+45, text='DÁTUM OD', font='Arial 20',anchor='e')
    datumod=tk.Entry(font="Helvetica 15 ", width=10).place(relx=.60,rely=.15)
    can.create_text(sirka//2+sirka//3, vyska//10+45, text='DÁTUM DO', font='Arial 20',anchor='e')
    datumdo=tk.Entry(font="Helvetica 15 ", width=10).place(relx=.85,rely=.15)
    button2= tk.Button(text='FILTROVAŤ',command=filtrovat)
    button2.pack()
    button2.place(relx=.9, rely=.250, anchor="w")
    button3= tk.Button(text='<==',command=spat)
    button3.pack()
    button3.place(relx=.02, rely=.05, anchor="w")
    def kalendar():
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
                    self.choose_btn = tk.Button(self.parent, text='Choose',command=self.popup)
                    self.show_btn = tk.Button(self.parent, text='Show Selected',command=self.print_selected_date)
                    self.choose_btn.grid()
                    self.show_btn.grid()
                    self.data = {}
             
                def popup(self):
                    child = tk.Toplevel()
                    cal = Calendar(child, self.data)
                def print_selected_date(self):
                    print(self.data)
                    datumod = tk.Entry(root)
                    new_text = "Example text"
                    datumod.delete(0, tk.END)
                    datumod.insert(0, self.data)

            root=tk.Tk()         
            app = Control(root)
    kalendar=tk.Button(text='kalendár', command=kalendar)
    kalendar.pack()
    kalendar.place(relx=.6, rely=.200)

    
def filtrovat():
    global frame, can
    scrollbar = tk.Scrollbar(root)
    scrollbar.place(x=sirka-120,y=200, height=vyska-200, width=20)
    trans_list = tk.Listbox(root, font='Arial 15')
    trans_list.place(x=100,y=200,width=sirka-220,height=vyska-200)
    for x in range(100):    
        trans_list.insert(x*3, 'Číslo Karty'+100*' ' +'SUMA')
        trans_list.insert(x*3+1, 'Číslo Účtu'+100*' ' +'DÁTUM')
        trans_list.insert(x*3+2, '')
    trans_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=trans_list.yview)
    
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
login= tk.Button(text='PRIHLÁSIŤ SA',command=frame1)
login.pack()
login.place(relx=.85, rely=.470, anchor="w")
login.config( height =5, width = 20 )
root.mainloop()








   



