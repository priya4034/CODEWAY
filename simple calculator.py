# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:20:41 2024

@author: Priyatharsini
"""
from tkinter import *
expression = ""

def press(num):

  global expression
  expression = expression + str(num)
  equation.set(expression)

def equalpress():

  try:

    global expression
    expression = expression.replace("%", "/100*")
    total = str(eval(expression))
    equation.set(total)
    expression = ""

  except:

    equation.set(" error ")
    expression = ""

def clear():
    
  global expression
  expression = ""
  equation.set("")
  
def doublezero():
    
  global expression
  if expression and expression[-1] in ['+', '-', '*', '/']:
     expression += '0'
  expression = expression + '00'
  equation.set(expression)

def editpress():
    
    global expression
    expression = expression[:-1]  
    equation.set(expression)
    
    
if __name__ == "__main__":
  
  gui = Tk()

  gui.configure(background="powder blue")

  gui.title("Simple Calculator")
 
  gui.geometry("370x315")
  
  gui.resizable(0, 0)
  
  frame = Frame(gui)
  frame.grid(row=0, column=0)

  equation = StringVar()

  expression_field = Label(gui, textvariable=equation,font = ('Helvetica',12) )
  expression_field.grid(columnspan=4 ,ipadx=70, padx=10, pady=10)

  equation.set('Expression to be Evaluated')

  button_font = ('Helvetica', 10) 
  

  button1 = Button(gui, text=' 1 ', fg='black', bg='white',
          command=lambda: press(1), height=2, width=9, font=button_font)
  button1.grid(row=5, column=0, padx=5, pady=5)

  button2 = Button(gui, text=' 2 ', fg='black', bg='white',
          command=lambda: press(2), height=2, width=9, font=button_font)
  button2.grid(row=5, column=1,  padx=5, pady=5)

  button3 = Button(gui, text=' 3 ', fg='black', bg='white',
          command=lambda: press(3), height=2, width=9,font=button_font)
  button3.grid(row=5, column=2,  padx=5, pady=5)

  button4 = Button(gui, text=' 4 ', fg='black', bg='white',
          command=lambda: press(4), height=2, width=9,font=button_font)
  button4.grid(row=4, column=0,  padx=5, pady=5)

  button5 = Button(gui, text=' 5 ', fg='black', bg='white',
          command=lambda: press(5), height=2, width=9,font=button_font)
  button5.grid(row=4, column=1,  padx=5, pady=5)

  button6 = Button(gui, text=' 6 ', fg='black', bg='white',
          command=lambda: press(6), height=2, width=9,font=button_font)
  button6.grid(row=4, column=2,  padx=5, pady=5)

  button7 = Button(gui, text=' 7 ', fg='black', bg='white',
          command=lambda: press(7), height=2, width=9,font=button_font)
  button7.grid(row=3, column=0,  padx=5, pady=5)

  button8 = Button(gui, text=' 8 ', fg='black', bg='white',
          command=lambda: press(8), height=2, width=9,font=button_font)
  button8.grid(row=3, column=1,  padx=5, pady=5)

  button9 = Button(gui, text=' 9 ', fg='black', bg='white',
          command=lambda: press(9), height=2, width=9, font=button_font)
  button9.grid(row=3, column=2, padx=5, pady=5)

  button0 = Button(gui, text=' 0 ', fg='black', bg='white',
          command=lambda: press(0), height=2, width=9, font=button_font)
  button0.grid(row=6, column=0,  padx=5, pady=5)
  
  button00 = Button(gui, text=' 00 ', fg='black', bg='white',
          command=doublezero, height=2, width=9, font=button_font)
  button00.grid(row=6, column=1,  padx=5, pady=5)

  plus = Button(gui, text=' + ', fg='black', bg='white',
        command=lambda: press("+"), height=2, width=9, font=button_font)
  plus.grid(row=5, column=3, padx=5, pady=5)

  minus = Button(gui, text=' - ', fg='black', bg='white',
        command=lambda: press("-"), height=2, width=9, font=button_font)
  minus.grid(row=4, column=3,  padx=5, pady=5)

  multiply = Button(gui, text=' * ', fg='black', bg='white',
          command=lambda: press("*"), height=2, width=9, font=button_font)
  multiply.grid(row=3, column=3,  padx=5, pady=5)

  divide = Button(gui, text=' / ', fg='black', bg='white',
          command=lambda: press("/"), height=2, width=9, font=button_font)
  divide.grid(row=2, column=3,  padx=5, pady=5)

  equal = Button(gui, text=' = ', fg='white', bg='black',
        command=equalpress, height=2, width=9, font=button_font)
  equal.grid(row=6, column=3,  padx=5, pady=5)

  allclear = Button(gui, text='Clear', fg='white', bg='black',
        command=clear, height=2, width=9, font=button_font)
  allclear.grid(row=2, column=0,  padx=5, pady=5)
  
  edit = Button(gui, text='<--', fg='white', bg='black',
        command=editpress, height=2, width=9, font=button_font)
  edit.grid(row=2, column=1,  padx=5, pady=5)

  percent = Button(gui, text=' % ', fg='black', bg='white', 
        command=lambda: press("%"), height=2, width=9, font=button_font)
  percent.grid(row=2, column=2, padx=5, pady=5)
  
  dot = Button(gui, text=' . ', fg='black', bg='white', 
        command=lambda: press('.'), height=2, width=9, font=button_font)
  dot.grid(row=6, column=2, padx=5, pady=5)
  
  gui.mainloop()