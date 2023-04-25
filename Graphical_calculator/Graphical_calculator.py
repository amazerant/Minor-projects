#!/usr/bin/env python
#functions written by Mazerant Adam https://github.com/amazerant

from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

def graph(functions,xlim,ylim,xlabel,ylabel,title,box):
    """Takes all inputs and draws plots"""
    
    x = np.linspace(xlim[0],xlim[1],int(np.ceil(xlim[1]-xlim[0]))*100, endpoint=True)
    legend = []

    for function in functions:
        if ('x' in function) == True:
            if ('x' in function.replace('exp','')) == False:
                try:
                    y = eval(function+'*x**0')
                except:
                    error_window(error="Wrong formulas were given")
                finally:
                    y = eval(function+'*x**0')
            else:
                try:
                    y = eval(function)
                except:
                    error_window(error="Wrong formulas were given")
                finally:
                    y = eval(function)
        else:
            try:
                y = eval(function+'*x**0')
            except:
                error_window(error="Wrong formulas - functions must depend on variable x")
            finally:
                y = eval(function+'*x**0')

        plt.plot(x,y)
        plt.axis([xlim[0],xlim[1],ylim[0],ylim[1]])
        legend.append(f"y = {function.replace('np.','').replace('**','^').replace('3.1415926536','pi').replace('2.7182818285','e')}")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if box ==1: plt.legend(legend)
    plt.show()

def convert(wzor):
    """Converts given functions into functions that can be evaluated using eval()"""

    funkcje = []

    wzory = wzor.split(';')

    for wzor in wzory:
        
        wzor = wzor.replace(' ','')
        wzor = wzor.lower()
        wzor = wzor.replace('pi', 'np.pi')
        wzor = wzor.replace('exp', 'EXP')
        wzor = wzor.replace('e', 'np.e')
        wzor = wzor.replace('EXP', 'np.exp')
        wzor = wzor.replace('x**0', '1')
        wzor = wzor.replace('x^0', '1') 
        wzor = wzor.replace('sqrt', 'np.sqrt')
        wzor = wzor.replace('^', '**')
        wzor = wzor.replace('sin', 'np.sin')
        wzor = wzor.replace('cos', 'np.cos')
        wzor = wzor.replace('tan', 'np.tan')
        wzor = wzor.replace('log', 'np.log')        

        funkcje.append(wzor)

    return funkcje

root = Tk()
root.geometry('845x245')
root.resizable(0,0)
root.title('Graphic calculator')

def error_window(error):
    error_root = Tk()
    error_root.geometry('400x50')
    error_root.resizable(0,0)
    error_root.title('Error')
    error_lbl = Label(error_root,text=error)
    error_lbl.pack()
    exitButton = Button(error_root, text='Close', command=error_root.destroy, width=15)
    exitButton.pack()
    error_root.mainloop()

xleft_V = IntVar()
xright_V = IntVar()
yleft_V = IntVar()
yright_V = IntVar()

wzor = StringVar()
title = StringVar()
legendBox = IntVar()
xlabel = StringVar()
ylabel = StringVar()

frame = Frame(root)
frame.pack(side=TOP)

plotframe = Frame(frame)
plotframe.grid(row=0, column=0)
    
text = Entry(plotframe, width=50)
text.insert(END,'x')
text.grid(row=0,column=0,padx=5,pady=5,columnspan=4)

xleftlbl = Label(plotframe, text='Beginning\n of the x interval')
xleftlbl.grid(row=1,column=0,padx=5,pady=5)
xleft = Entry(plotframe, width=10)
xleft.insert(END,'-1')
xleft.grid(row=1,column=1,padx=5,pady=5)

xrightlbl = Label(plotframe, text='End\n of the x interval')
xrightlbl.grid(row=1,column=2,padx=5,pady=5)
xright = Entry(plotframe, width=10)
xright.insert(END,'1')
xright.grid(row=1,column=3,padx=5,pady=5)
    
yleftlbl = Label(plotframe, text='Beginning\n of the y interval')
yleftlbl.grid(row=2,column=0,padx=5,pady=5)
yleft = Entry(plotframe, width=10)
yleft.insert(END,'-1')
yleft.grid(row=2,column=1,padx=5,pady=5)

yrightlbl = Label(plotframe, text='End\n of the y interval')
yrightlbl.grid(row=2,column=2,padx=5,pady=5)
yright = Entry(plotframe, width=10)
yright.insert(END,'1')
yright.grid(row=2,column=3,padx=5,pady=5)

xlbl = Label(plotframe, text='x axis label')
xlbl.grid(row=3,column=0,padx=5,pady=5)

xEntry = Entry(plotframe, width=10)
xEntry.grid(row=3,column=1,padx=5,pady=5)
xEntry.insert(END,'x label')
    
ylbl = Label(plotframe, text='y axis label')
ylbl.grid(row=3,column=2,padx=5,pady=5)

yEntry = Entry(plotframe, width=10)
yEntry.grid(row=3,column=3,padx=5,pady=5)
yEntry.insert(END,'y label')
    
tlbl = Label(plotframe, text='Plot title')
tlbl.grid(row=4,column=0,padx=5,pady=5)

tEntry = Entry(plotframe, width=40)
tEntry.grid(row=4,column=1,padx=5,pady=5,columnspan=2)
tEntry.insert(END,'Plot of y(x)')
    
checkbox = Checkbutton(plotframe, text='Show\nlegend?', variable=legendBox, onvalue=1, offvalue=0)
checkbox.grid(row=4,column=3,padx=5,pady=5)

def draw():
    """Initializes graph() function"""

    is_error = False
    
    try:
        xleft_V.set(eval(xleft.get().lower().replace('exp','EXP').replace('pi','np.pi').replace('e', 'np.e').replace('EXP', 'np.exp').replace('^','**')))
    except:
        is_error = True
        error_window(error="Wrong value for: beginning of x interval")
    finally:
        xleft_V.set(eval(xleft.get().lower().replace('exp','EXP').replace('pi','np.pi').replace('e', 'np.e').replace('EXP', 'np.exp').replace('^','**')))

    try:
        xright_V.set(eval(xright.get().lower().replace('exp','EXP').replace('pi','np.pi').replace('e', 'np.e').replace('EXP', 'np.exp').replace('^','**')))
    except:
        is_error = True
        error_window(error="Wrong value for: end of x interval")
    finally:
        xright_V.set(eval(xright.get().lower().replace('exp','EXP').replace('pi','np.pi').replace('e', 'np.e').replace('EXP', 'np.exp').replace('^','**')))

    try:
        yleft_V.set(eval(yleft.get().lower().replace('exp','EXP').replace('pi','np.pi').replace('e', 'np.e').replace('EXP', 'np.exp').replace('^','**')))
    except:
        is_error = True
        error_window(error="Wrong value for: beginning of y interval")
    finally:
        yleft_V.set(eval(yleft.get().lower().replace('exp','EXP').replace('pi','np.pi').replace('e', 'np.e').replace('EXP', 'np.exp').replace('^','**')))

    try: 
        yright_V.set(eval(yright.get().lower().replace('exp','EXP').replace('pi','np.pi').replace('e', 'np.e').replace('EXP', 'np.exp').replace('^','**')))
    except:
        error_window(error="Wrong value for: end of y interval")
    finally:
        yright_V.set(eval(yright.get().lower().replace('exp','EXP').replace('pi','np.pi').replace('e', 'np.e').replace('EXP', 'np.exp').replace('^','**')))

    wzor.set(text.get())
    xlabel.set(xEntry.get())
    ylabel.set(yEntry.get())
    title.set(tEntry.get())

    if xleft_V.get() >= xright_V.get():

        error_window(error="Left limit of x interval is bigger than right limit")

    elif yleft_V.get() >= yright_V.get():

        error_window(error="Left limit of y interval is bigger than right limit")

    else:
        if is_error == False:
            graph(functions=convert(wzor.get()),
                                xlim=(xleft_V.get(),xright_V.get()),
                                ylim=(yleft_V.get(),(yright_V.get())),
                                xlabel=xlabel.get(),
                                ylabel=ylabel.get(),
                                title=title.get(),
                                box=legendBox.get())
        
    
drawB = Button(plotframe, text='Show plots', command=draw, width=15)
drawB.grid(row=5,column=0,padx=5,pady=5,columnspan=2)
    
ttk.Separator(frame, orient=VERTICAL).grid(column=1,row=0, rowspan=7, sticky='ns', pady=5)

btnframe = Frame(frame)
btnframe.grid(row=0,column=2)

plus = Button(btnframe, text='+', command=lambda: text.insert(text.index(INSERT),'+'), width=6, height=1)
plus.grid(row=0,column=0,padx=5,pady=5)

minus = Button(btnframe, text='-', command=lambda: text.insert(text.index(INSERT),'-'), width=6, height=1)
minus.grid(row=0,column=1,padx=5,pady=5)

times = Button(btnframe, text='*', command=lambda: text.insert(text.index(INSERT),'*'), width=6, height=1)
times.grid(row=0,column=2,padx=5,pady=5)

div = Button(btnframe, text='/', command=lambda: text.insert(text.index(INSERT),'/'), width=6, height=1)
div.grid(row=1,column=0,padx=5,pady=5)

power = Button(btnframe, text='^', command=lambda: text.insert(text.index(INSERT),'^'), width=6, height=1)
power.grid(row=1,column=1,padx=5,pady=5)

sqrt = Button(btnframe, text='sqrt(x)', command=lambda: text.insert(text.index(INSERT),'sqrt(x)'), width=6, height=1)
sqrt.grid(row=1,column=2,padx=5,pady=5)

sin = Button(btnframe, text='sin(x)', command=lambda: text.insert(text.index(INSERT),'sin(x)'), width=6, height=1)
sin.grid(row=2,column=0,padx=5,pady=5)

cos = Button(btnframe, text='cos(x)', command=lambda: text.insert(text.index(INSERT),'cos(x)'), width=6, height=1)
cos.grid(row=2,column=1,padx=5,pady=5)

tan = Button(btnframe, text='tan(x)', command=lambda: text.insert(text.index(INSERT),'tan(x)'), width=6, height=1)
tan.grid(row=2,column=2,padx=5,pady=5)

exp = Button(btnframe, text='exp(x)', command=lambda: text.insert(text.index(INSERT),'exp(x)'), width=6, height=1)
exp.grid(row=3,column=0,padx=5,pady=5)

log = Button(btnframe, text='log(x)', command=lambda: text.insert(text.index(INSERT),'log(x)'), width=6, height=1)
log.grid(row=3,column=1,padx=5,pady=5)

log10 = Button(btnframe, text='log10(x)', command=lambda: text.insert(text.index(INSERT),'log10(x)'), width=6, height=1)
log10.grid(row=3,column=2,padx=5,pady=5)

b7 = Button(btnframe, text='7', command=lambda: text.insert(text.index(INSERT), '7'), width=6, height=1)
b7.grid(row=0,column=3,padx=5,pady=5)

b8 = Button(btnframe, text='8', command=lambda: text.insert(text.index(INSERT), '8'), width=6, height=1)
b8.grid(row=0,column=4,padx=5,pady=5)

b9 = Button(btnframe, text='9', command=lambda: text.insert(text.index(INSERT), '9'), width=6, height=1)
b9.grid(row=0,column=5,padx=5,pady=5)

b4 = Button(btnframe, text='4', command=lambda: text.insert(text.index(INSERT), '4'), width=6, height=1)
b4.grid(row=1,column=3,padx=5,pady=5)

b5 = Button(btnframe, text='5', command=lambda: text.insert(text.index(INSERT), '5'), width=6, height=1)
b5.grid(row=1,column=4,padx=5,pady=5)

b6 = Button(btnframe, text='6', command=lambda: text.insert(text.index(INSERT), '6'), width=6, height=1)
b6.grid(row=1,column=5,padx=5,pady=5)

b1 = Button(btnframe, text='1', command=lambda: text.insert(text.index(INSERT), '1'), width=6, height=1)
b1.grid(row=2,column=3,padx=5,pady=5)

b2 = Button(btnframe, text='2', command=lambda: text.insert(text.index(INSERT), '2'), width=6, height=1)
b2.grid(row=2,column=4,padx=5,pady=5)

b3 = Button(btnframe, text='3', command=lambda: text.insert(text.index(INSERT), '3'), width=6, height=1)
b3.grid(row=2,column=5,padx=5,pady=5)

b0 = Button(btnframe, text='0', command=lambda: text.insert(text.index(INSERT), '0'), width=6, height=1)
b0.grid(row=3,column=3,padx=5,pady=5)

x = Button(btnframe, text='x', command=lambda: text.insert(text.index(INSERT), 'x'), width=6, height=1)
x.grid(row=3,column=4,padx=5,pady=5)

semi = Button(btnframe, text=';', command=lambda: text.insert(text.index(INSERT), ';'), width=6, height=1)
semi.grid(row=3,column=5,padx=5,pady=5)

exitButton = Button(plotframe, text='Close', command=root.destroy, width=15)
exitButton.grid(row=5,column=2,columnspan=2)
    
root.mainloop()

if __name__ == "__main__":
    pass
