path="kurs_walut.txt"
from Tkinter import *
import sys
def program():
    checkfile=open(path)
    dolar = checkfile.readline()
    euro = checkfile.readline()
    frank = checkfile.readline()
    checkfile.close
    dolar = float(dolar)
    euro = float(euro)
    frank = float(frank)
    root = Tk()
    root.title('Program Wymiany Walut')
    top = Frame(root)
    top.pack(side='top') 
    hwframe = Frame(top)
    hwframe.pack(side='top')
    font = 'times 18 bold'
    hwtext = Label(hwframe, text='>Program Wymiany Walut<',bg='black',fg='green', font=font)
    hwtext.pack(side='top', pady=20,fill='x')
    kurstext = Label(hwframe, text='  $=%g  €=%g CHF=%g  '% (dolar,euro,frank), font='Thoma 15')
    kurstext.pack(side='top', pady=20)   
    def wymiana(event=None):
        checkfile=open(path)
        dolar = checkfile.readline()
        dolar = float(dolar)
        euro = checkfile.readline()
        euro = float(euro)
        frank = checkfile.readline()
        frank = float(frank)
        root = Tk()
        root.title('Wymiana')
        top = Frame(root)
        top.pack(side='top')
        bottom = Frame(root)
        bottom.pack(side='bottom')
        hwframe = Frame(top)
        hwframe.pack(side='top')
        font = 'times 18 bold'
        rachunek = 'arial 15'
        hwtext = Label(hwframe, text='Wybierz która walute chcesz wymienić', font=font)
        hwtext.pack(side='top', pady=20)
        rframe = Frame(top)
        rframe.pack(side='top', padx=100, pady=20)
        s_label = Label(rframe, width=30)
        s_label.pack(side='bottom')
        r_entry = Entry(top, width=15,bg='gray',bd=5,fg='red',font='Times 15')
        r_entry.pack(side='top')
        r_entry.insert('end', '')
        def zlnadolar(event=None):
            kasa = float(r_entry.get())
            wynik=kasa/dolar
            s_label.configure(text=("-------------------"
                                   "\nNależy wypłacić: %g$"
                                   "\n-------------------") % (round(wynik,2)),font=rachunek)
        def dolarnazl(event=None):
            kasa = float(r_entry.get())
            wynik=kasa*dolar
            s_label.configure(text=("-------------------"
                                   "\nNależy wypłacić: %gzł"
                                   "\n-------------------") % (round(wynik,2)),font=rachunek)
        def zlnaeuro(event=None):
            kasa = float(r_entry.get())
            wynik=kasa/euro
            s_label.configure(text=("-------------------"
                                   "\nNależy wypłacić: %g €"
                                   "\n-------------------") % (round(wynik,2)),font=rachunek)
        def euronazl(event=None):
            kasa = float(r_entry.get())
            wynik=kasa*euro
            s_label.configure(text=("-------------------"
                                   "\nNależy wypłacić: %gzł"
                                   "\n-------------------") % (round(wynik,2)),font=rachunek)
        def franknazl(event=None):
            kasa = float(r_entry.get())
            wynik=kasa*frank
            s_label.configure(text=("-------------------"
                                   "\nNależy wypłacić: %gzł"
                                   "\n-------------------") % (round(wynik,2)),font=rachunek)
        def zlnafrank(event=None):
            kasa = float(r_entry.get())
            wynik=kasa/frank
            s_label.configure(text=("-------------------"
                                   "\nNależy wypłacić: %gF"
                                   "\n-------------------") % (round(wynik,2)),font=rachunek)
        def kasuj(event=None):
            r_entry.delete('0', END)
        def quit(event=None):
            root.destroy()
        zlotenadolar = Button(hwframe, text="Zł na $", command=zlnadolar, relief='solid',bg='green',font='Arial 15 bold')
        zlotenadolar.pack(side='left')
        dolarnazlote = Button(hwframe, text="$ na Zł",command=dolarnazl, relief='solid',bg='green',font='Arial 15 bold')
        dolarnazlote.pack(side='left')
        zlotenaeuro = Button(hwframe, text="Zł na €",command=zlnaeuro, relief='solid',bg='yellow',font='Arial 15 bold')
        zlotenaeuro.pack(side='right')
        euronazlote = Button(hwframe, text="€ na Zł",command=euronazl, relief='solid',bg='yellow',font='Arial 15 bold')
        euronazlote.pack(side='right')
        zlotenafrank = Button(rframe, text="Fr. na Zł",command=franknazl, relief='solid',bg='blue',fg='yellow',font='Arial 15 bold')
        zlotenafrank.pack(side='left')
        franknazlote = Button(rframe, text="Zł na Fr.",command=euronazl, relief='solid',bg='blue',fg='yellow',font='Arial 15 bold')
        franknazlote.pack(side='left')
        kasuj = Button(top, text='Kasuj', command=kasuj,bg='red', fg='yellow',font='Thoma 12')
        kasuj.pack(side='top', pady=10)
        quit_button = Button(top, text='Wróć do głównego menu', command=quit,bg='yellow', fg='blue')
        quit_button.pack(side='bottom', pady=5, fill='x')
        root.bind('<q>', quit)
        root.mainloop() 
    def ustawienia(event=None):
        checkfile=open(path)
        dolar = checkfile.readline()
        euro = checkfile.readline()
        frank = checkfile.readline()
        checkfile.close
        dolar = float(dolar)
        euro = float(euro)
        frank = float(frank)
        root = Tk()
        root.title('Ustawienia')
        top = Frame(root)
        top.pack(side='top') 
        napisframe = Frame(top)
        napisframe.pack(side='top')
        font = 'times 18 bold'
        napis='arial 12'
        napistext = Label(napisframe, text='Zmiana stawek walut', font=font)
        napistext.pack(side='top', pady=10)
        rframe = Frame(top)
        rframe.pack(side='top', padx=10, pady=5)
        r_label = Label(rframe, text='Zmiana kursu $: ',font='Courier 12 bold')
        r_label.pack(side='left')
        s_label = Label(rframe, width=30)
        s_label.pack(side='right')
        r_entry = Entry(rframe, width=6,font='thoma 12 bold',bd=4,bg='gray',fg='red')
        r_entry.pack(side='left')
        r_entry.insert('end', '')
        sframe = Frame(top)
        sframe.pack(side='top', padx=10, pady=5)
        t_label = Label(sframe, text='Zmiana kursu €: ',font='Courier 12 bold')
        t_label.pack(side='left')
        w_label = Label(sframe, width=30)
        w_label.pack(side='right')
        t_entry = Entry(sframe, width=6,font='thoma 12 bold',bd=4,bg='gray',fg='red')
        t_entry.pack(side='left')
        wframe = Frame(top)
        wframe.pack(side='top', padx=10, pady=5)
        k_label = Label(wframe, text='Zmiana kursu CHF: ',font='Courier 12 bold')
        k_label.pack(side='left')
        m_label = Label(wframe, width=30)
        m_label.pack(side='right')
        k_entry = Entry(wframe, width=6,font='thoma 12 bold',bd=4,bg='gray',fg='red')
        k_entry.pack(side='left')
        def dolar(event=None):
            checkfile=open(path)
            nowacena = float(r_entry.get())
            dolar=nowacena
            pierwsza = str(dolar)
            druga = str(euro)
            trzecia = str(frank)
            checkfile = open(path, "w")
            checkfile.write(pierwsza+"\n"+druga+"\n"+trzecia)
            checkfile.close()
            s_label.configure(text='Zmieniono kurs $ na: %gzł' % dolar,font=napis)
            r_entry.delete('0', END)
        def euro(event=None):
            checkfile=open(path)
            noweobj = int(t_entry.get())
            obj=noweobj
            pierwsza = str(cena)
            druga = str(obj)
            trzecia = str(ilzbr)
            checkfile = open(path, "w")
            checkfile.write(pierwsza+"\n"+druga+"\n"+trzecia)
            checkfile.close()
            w_label.configure(text=("Zmieniono kurs Euro na : %gzł") % obj,font=napis)
            t_entry.delete('0', END)
        def frank(event=None):
            checkfile=open(path)
            noweilzbr = int(k_entry.get())
            ilzbr=noweilzbr
            pierwsza = str(cena)
            druga = str(obj)
            trzecia = str(ilzbr)
            checkfile = open(path, "w")
            checkfile.write(pierwsza+"\n"+druga+"\n"+trzecia)
            checkfile.close()
            m_label.configure(text=("Zmieniono kurs franka na: %gzł") % ilzbr,font=napis)
            k_entry.delete('0', END)
        def quit(event=None):
            root.destroy()

        dola = Button(rframe, text="Potwierdź", command=dolar, relief='solid',bg='green')
        dola.pack(side='left')
        objetosc = Button(sframe, text="Potwierdź", command=euro, relief='solid',bg='green')
        objetosc.pack(side='right')
        zbiorniki = Button(wframe, text="Potwierdź", command=frank, relief='solid',bg='green')
        zbiorniki.pack(side='right')
        quit_button = Button(top, text='Wróć do głównego menu', command=quit,
                             background='yellow', foreground='blue')
        quit_button.pack(side='top', pady=5, fill='x')
        root.bind('<q>', quit)
        root.mainloop() 
    def quit(event=None):
        sys.exit()
    wymiana = Button( text='Wymiana Walut',fg='red',font='Arial 18 bold',command=wymiana, relief='groove')
    wymiana.pack(side='top')
    zmiana = Button( text='Zmiana kursów',fg='red',font='Arial 18 bold', command=ustawienia, relief='groove')
    zmiana.pack(side='top',pady=20)
    wyjscie = Button( text='Zamknij program',bg='black',fg='green',font='Courier 12 bold', command=quit, relief='flat')
    wyjscie.pack(side='bottom',fill='x')
    root.mainloop()
program()
