# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 01:40:53 2023

@author: p
"""

from tkinter import *
expression=''
def press_on(user_input):
    global expression
    expression=expression+ str(user_input)
    equation.set(expression)
def resultPress():
    global expression
    result=str(eval(expression))
    equation.set(result)
def clearPress():
    global expression
    expression=" "
    equation.set(expression)
    
window=Tk()
window.title("Alaa Calculator")
window.geometry("340x320")
window.configure(bg='#272A29')
label=Label(window,text='Simple Calculator',bg='#111518',fg='#F27614',font=('century 16 bold'),borderwidth=10)
label.grid(columnspan=4,pady=5)

equation=StringVar()
expressionField=Entry(window,textvariable=equation,bg='#D7D7D7',width=50,borderwidth=10)
expressionField.grid(columnspan=4,pady=10)
btn1=Button(window,text='1',command=lambda: press_on(1),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btn1.grid(row=3,column=0)
btn2=Button(window,text='2',command=lambda: press_on(2),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btn2.grid(row=3,column=1)
btn3=Button(window,text='3',command=lambda: press_on(3),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btn3.grid(row=3,column=2)
btnPlus=Button(window,text='+',command=lambda: press_on('+'),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btnPlus.grid(row=3,column=3)

btn4=Button(window,text='4',command=lambda: press_on(4),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btn4.grid(row=4,column=0)
btn5=Button(window,text='5',command=lambda: press_on(5),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btn5.grid(row=4,column=1)
btn6=Button(window,text='6',command=lambda: press_on(6),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btn6.grid(row=4,column=2)
btnMinus=Button(window,text='-',command=lambda: press_on('-'),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btnMinus.grid(row=4,column=3)

btn7=Button(window,text='7',command=lambda: press_on(7),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btn7.grid(row=5,column=0)
btn8=Button(window,text='8',command=lambda: press_on(8),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btn8.grid(row=5,column=1)
btn9=Button(window,text='9',command=lambda: press_on(9),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btn9.grid(row=5,column=2)
btnMultiply=Button(window,text='*',command=lambda: press_on('*'),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btnMultiply.grid(row=5,column=3)

btn0=Button(window,text='0',command=lambda: press_on(0),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btn0.grid(row=6,column=0)
btnDot=Button(window,text='.',command=lambda: press_on('.'),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btnDot.grid(row=6,column=1)
btnEqual=Button(window,text='=',command=resultPress,width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btnEqual.grid(row=6,column=2)
btnDivide=Button(window,text='/',command=lambda: press_on('/'),width=9,height=2,padx=2,bg='#D7D7D7',font=('century 8 bold'))
btnDivide.grid(row=6,column=3)
btnClear=Button(window,text='Clear',command=clearPress,width=42,height=2,bg='#F97109',font=('century 8 bold'))
btnClear.grid(row=7,columnspan=4)


window.mainloop()

