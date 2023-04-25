#!/usr/bin/env python
#Functions written by Mazerant Adam https://github.com/amazerant

from tkinter import *
import csv
import requests

def internet_on():
    try:
        requests.get('https://www.google.pl/', timeout=1)
        return True
    except:
        return False

def create_main_window():

    root = Tk()
    root.title('Currency exchange calculator')
    root.geometry('450x200')
    root.resizable(0,0)

    frame = Frame(root)
    frame.pack()
    
    currency1 = StringVar()
    currency1.set('"złoty" "PLN"')

    currency2 = StringVar()
    currency2.set('"złoty" "PLN"')


    exchange_rate = StringVar()
    exchange_rate.set('1.0')

    def mulchange(*args):
        exchange_rate.set(round(currencies[currency1.get()]/currencies[currency2.get()],4))
    
    currency1.trace('w', mulchange)
    currency2.trace('w', mulchange)

    Label(frame, text='Starting currency:').grid(row=0, column=0, pady=3, padx=3)
    Label(frame, text="Ending currency:").grid(row=0, column=1, pady=3, padx=3)

    menu_button1 = Menubutton(frame, textvariable=currency1)
    menu_button2 = Menubutton(frame, textvariable=currency2)

    menu1 = Menu(menu_button1, tearoff=0)
    menu2 = Menu(menu_button2, tearoff=0)

    for key in currencies.keys():
        menu1.add_radiobutton(label=f"{key}", value=f"{key}", variable = currency1)
        menu2.add_radiobutton(label=f"{key}", value=f"{key}", variable = currency2)

    menu_button1['menu'] = menu1
    menu_button1.grid(row=1, column=0, pady=3, padx=3)

    menu_button2['menu'] = menu2
    menu_button2.grid(row=1, column=1, pady=3, padx=3)
    
    label_p = Label(frame,textvariable=exchange_rate)
    label_p.grid(row=2, column=0, columnspan=2, pady=2)
    
    kwota = Entry(frame, width=20)
    kwota.insert(END, '0')
    kwota.grid(row=3, column=0, columnspan=2, pady=3)

    def calculate():
        try:
            inp = float(kwota.get())
        except:
            label_k.config(text='Result: wrong input')
        else:
            inp = float(kwota.get())*float(exchange_rate.get())
            label_k.config(text=f'Result: {str(inp)}')

    Przelicz = Button(frame, text='Calculate', command=calculate, width=15)
    Przelicz.grid(row=4, column=0, columnspan=2, pady=3)

    label_k = Label(frame, text='Result: ')
    label_k.grid(row=5, column=0, columnspan=2, pady=3)
    
    koniec = Button(frame, text='Close', command=root.destroy, width=15)
    koniec.grid(row=6,column=0,  columnspan=2, pady=3)
    
    root.mainloop()

if __name__ == "__main__":
    if internet_on() == True:
        import api
    else:
        try:
            open('exchange.csv','r')
            print("Saved table of exchange rates was loaded")
        except:    
            print("Couldn't load saved table of exchange rates")

    currencies = {'"złoty" "PLN"':1.000}

    with open('exchange.csv') as plik:
        plik_reader = csv.reader(plik, delimiter=',')

        for row in plik_reader:
            if len(row) > 0:
                currencies[f"{row[1]} {row[0]}"] = float(f"{row[2]}")
                
    create_main_window()
    
