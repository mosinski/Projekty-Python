path="dane.txt"
import sys
from Tkinter import *
from tkMessageBox import *

def pathcheck():
    checkfile=open(path)
    pierwsza = checkfile.readline()
    druga = checkfile.readline()
    trzecia = checkfile.readline()
    checkfile.close
    cena = float(pierwsza)
    obj = int(druga)
    ilzbr = int(trzecia)
    root = Tk()
    root.title('Program Stacji Gazu')
    top = Frame(root)
    top.pack(side='top') 
    hwframe = Frame(top)
    hwframe.pack(side='top')
    font = 'times 18 bold'
    hwtext = Label(hwframe, text='>Program Stacji Gazu<',bg='black',fg='green', font=font)
    hwtext.pack(side='top', pady=20)
    def sprzedaz(event=None):
        checkfile=open(path)
        pierwsza = checkfile.readline()
        cena = float(pierwsza)
        root = Tk()
        root.title('Sprzedaż')
        top = Frame(root)
        top.pack(side='top') 
        hwframe = Frame(top)
        hwframe.pack(side='top')
        font = 'times 18 bold'
        rachunek = 'arial 15'
        hwtext = Label(hwframe, text='Wybierz opcje', font=font)
        hwtext.pack(side='top', pady=20)
        rframe = Frame(top)
        rframe.pack(side='top', padx=10, pady=20)
        r_label = Label(rframe, text='Podaj w zł: ', fg='blue', font='13')
        s_label = Label(rframe, width=30)
        s_label.pack(side='bottom')
        r_label.pack(side='left')
        r_entry = Entry(rframe, width=6)
        r_entry.pack(side='left')
        r_entry.insert('end', '')
        t_label = Label(rframe, text=("Podaj w dm'3"), fg= 'blue', font='13')
        t_label.pack(side='right')
        t_entry = Entry(rframe, width=6)
        t_entry.pack(side='right')
        t_entry.insert('end', '')
        t_entry.delete('0', END)
        def comp_s(event=None):
            r = float(r_entry.get())
            gaz=r/cena
            s_label.configure(text=("-------------------"
                                   "\nZatanokowano: %g dm'3"
                                   "\nRachunek wynosi: %g zł"
                                   "\n-------------------") % (round(gaz,2),r),font=rachunek)
            r_entry.delete('0', END)
        def comp_t(event=None):
            t = float(t_entry.get())
            money=t*cena
            s_label.configure(text=("--------------------"
                                   "\nZatanokowano: %g dm'3"
                                   "\nRachunek wynosi: %g zł"
                                   "\n-------------------") % (t,round(money,2)),font=rachunek)

        r_entry.bind('<Return>', comp_s)

        def quit(event=None):
            root.destroy()

        pieniadze = Button(top, text="Potwierdź", command=comp_s, relief='solid',bg='green')
        pieniadze.pack(side='left')
        objetosc = Button(top, text="Potwierdź",command=comp_t, relief='solid',bg='green')
        objetosc.pack(side='right')
        quit_button = Button(top, text='Wróć do głównego menu', command=quit,
                             background='yellow', foreground='blue')
        quit_button.pack(side='top', pady=5, fill='x')
        root.bind('<q>', quit)
        root.mainloop() 
        
    def ustawienia(event=None):
        checkfile=open(path)
        pierwsza = checkfile.readline()
        cena = float(pierwsza)
        druga = checkfile.readline()
        obj = int(druga)
        root = Tk()
        root.title('Ustawienia')
        top = Frame(root)
        top.pack(side='top') 

        napisframe = Frame(top)
        napisframe.pack(side='top')
        font = 'times 18 bold'
        napis='arial 12'
        napistext = Label(napisframe, text='Dostępne Ustawienia', font=font)
        napistext.pack(side='top', pady=10)
        rframe = Frame(top)
        rframe.pack(side='top', padx=10, pady=5)
        napistext = Label(rframe, text='Aktualna cena: %szł/1L' % cena, fg='red',font='arial 13 italic')
        napistext.pack(side='top', pady=20)
        r_label = Label(rframe, text='                      Zmiana ceny: ')
        r_label.pack(side='left')
        s_label = Label(rframe, width=30)
        s_label.pack(side='right')
        r_entry = Entry(rframe, width=6)
        r_entry.pack(side='left')
        r_entry.insert('end', '')
        sframe = Frame(top)
        sframe.pack(side='top', padx=10, pady=5)
        napistext = Label(sframe, text=("Aktualna wielkość zbiorników: %s dm'3") % obj, fg='red',font='arial 13 italic')
        napistext.pack(side='top', pady=20)
        t_label = Label(sframe, text='Zmiana wilekości zbiorników: ')
        t_label.pack(side='left')
        w_label = Label(sframe, width=30)
        w_label.pack(side='right')
        t_entry = Entry(sframe, width=6)
        t_entry.pack(side='left')
        wframe = Frame(top)
        wframe.pack(side='top', padx=10, pady=5)
        napistext = Label(wframe, text=("Aktualna ilość zbiorników: %s ") % ilzbr, fg='red',font='arial 13 italic')
        napistext.pack(side='top', pady=20)
        k_label = Label(wframe, text='     Zmiana ilości zbiorników: ')
        k_label.pack(side='left')
        m_label = Label(wframe, width=30)
        m_label.pack(side='right')
        k_entry = Entry(wframe, width=6)
        k_entry.pack(side='left')
        def comp_s(event=None):
            checkfile=open(path)
            nowacena = float(r_entry.get())
            cena=nowacena
            pierwsza = str(cena)
            druga = str(obj)
            trzecia = str(ilzbr)
            checkfile = open(path, "w")
            checkfile.write(pierwsza+"\n"+druga+"\n"+trzecia)
            checkfile.close()
            s_label.configure(text='Zmieniono cene na: %gzł/1L' % cena,font=napis)
            r_entry.delete('0', END)
        def comp_t(event=None):
            checkfile=open(path)
            noweobj = int(t_entry.get())
            obj=noweobj
            pierwsza = str(cena)
            druga = str(obj)
            trzecia = str(ilzbr)
            checkfile = open(path, "w")
            checkfile.write(pierwsza+"\n"+druga+"\n"+trzecia)
            checkfile.close()
            w_label.configure(text=("Zmieniono objętość na: %gdm'3!!") % obj,font=napis)
            t_entry.delete('0', END)
        def comp_w(event=None):
            checkfile=open(path)
            noweilzbr = int(k_entry.get())
            ilzbr=noweilzbr
            pierwsza = str(cena)
            druga = str(obj)
            trzecia = str(ilzbr)
            checkfile = open(path, "w")
            checkfile.write(pierwsza+"\n"+druga+"\n"+trzecia)
            checkfile.close()
            m_label.configure(text=("Zmieniono ilość zbiorników na: %g") % ilzbr,font=napis)
            k_entry.delete('0', END)
        def quit(event=None):
            root.destroy()

        pieniadze = Button(rframe, text="Potwierdź", command=comp_s, relief='solid',bg='green')
        pieniadze.pack(side='left')
        objetosc = Button(sframe, text="Potwierdź", command=comp_t, relief='solid',bg='green')
        objetosc.pack(side='right')
        zbiorniki = Button(wframe, text="Potwierdź", command=comp_w, relief='solid',bg='green')
        zbiorniki.pack(side='right')
        quit_button = Button(top, text='Wróć do głównego menu', command=quit,
                             background='yellow', foreground='blue')
        quit_button.pack(side='top', pady=5, fill='x')
        root.bind('<q>', quit)
        root.mainloop() 
    def dodatkowe_opcje (event=None) :
        root = Tk()
        root.title('Dodatkowe opcje')
        top = Frame(root)
        top.pack(side='top') 

        hwframe = Frame(top)
        hwframe.pack(side='top')
        napisframe = Frame(top)
        napisframe.pack(side='top')
        font = 'times 18 bold'
        rachunek = 'arial 15'
        hwtext = Label(hwframe, text='Wybierz opcje', font=font)
        hwtext.pack(side='top', pady=20)
        napistext = Label(hwframe, text='Ile jest aktualnie gazu w zbiornikach stacji', fg='red',font='arial 13 italic')
        napistext.pack(side='top', pady=20)

        rframe = Frame(top)
        rframe.pack(side='top', padx=10, pady=20)

        r_label = Label(rframe, text='Podaj sume procentów: ')
        s_label = Label(rframe, width=30)
        s_label.pack(side='bottom')
        r_label.pack(side='left')
        r_entry = Entry(rframe, width=6)
        r_entry.pack(side='left')
        r_entry.insert('end', '')

        napisyframe = Frame(top)
        napisyframe.pack (side='top', padx=10, pady=30)
        napiframe = Frame (top)
        napiframe.pack (side='top')
        napisytext = Label(napisyframe,text = 'Maksymalna ilość gazu przy dostawie',fg='red',font='arial 13 italic')
        napisytext.pack(side='top')
        t_label = Label(napiframe, text='Podaj sume procentów: ')
        p_label = Label(napiframe, width=30)
        p_label.pack(side='bottom')
        t_label.pack(side='left')
        t_entry = Entry(napiframe, width=6)
        t_entry.pack(side='left')
        t_entry.insert('end', '')
        napframe = Frame (top)
        napframe.pack (side='top',padx=10, pady=30)
        napisytext = Label(napframe,text = '*Wynik uwzględnia fakt iż w zbiorniku nie może znajdować się więcej niż 85% gazu.',font='arial 11 underline')
        napisytext.pack(side='bottom')


        def comp_s(event=None):
            r = float(r_entry.get())
            gaz=r*obj/100
            s_label.configure(text=("-------------------"
                                    "\nW zbiornikach aktualnie znajduje się"
                                    "\n%g dm'3 gazu *"
                                    "\n-------------------") % (gaz),font=rachunek)
            r_entry.delete('0', END)
        def comp_t(event=None):
            t = float(t_entry.get())
            gaz=(((85*ilzbr)-t)*obj)/100
            p_label.configure(text=("--------------------"
                                    "\nPodczas dostawy gazu maksymalnie"
                                    "\nzmieści się: %g dm'3 *"
                                    "\n-------------------") % (gaz),font=rachunek)
            t_entry.delete('0', END)

        r_entry.bind('<Return>', comp_s)

        def quit(event=None):
            root.destroy()
        
        pieniadze = Button(rframe, text="Potwierdź", command=comp_s, relief='solid',bg='green')
        pieniadze.pack(side='right')
        
        objetosc = Button(napiframe, text="Potwierdź",command=comp_t, relief='solid',bg='green')
        objetosc.pack(side='right')
        quit_button = Button(top, text='Wróć do głównego menu', command=quit,
                             background='yellow', foreground='blue')
        quit_button.pack(side='top', pady=5, fill='x')
        root.bind('<q>', quit)

        root.mainloop() 
        r_entry.bind('<Return>', comp_s)
    def quit(event=None):
        sys.exit()
    sprzedaz = Button( text='Sprzedaż',fg='red',font=font,command=sprzedaz, relief='flat')
    sprzedaz.pack(side='top')
    d_opcje = Button( text='Dodatkowe Opcje',fg='red',font=font, command=dodatkowe_opcje, relief='flat')
    d_opcje.pack(side='top')
    ustawienia = Button( text='Ustawienia',fg='red',font=font, command=ustawienia, relief='flat')
    ustawienia.pack(side='top')
    wyjscie = Button( text='Wyjście',fg='red',font=font, command=quit, relief='flat')
    wyjscie.pack(side='top')
    root.mainloop()
    pierwsza = str(cena)
    druga = str(obj)
    trzecia = str(ilzbr)
    checkfile = open(path, "w")
    checkfile.write(pierwsza+"\n"+druga+"\n"+trzecia)
    checkfile.close()
pathcheck()
