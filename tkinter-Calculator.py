from tkinter import *
import math
root = Tk()

# root.title(), like the window name in the close button row
root.title('Cal : )')
# add the window icon
root.iconbitmap(r'C:/Users/4Raisan/Desktop/GitHub/Tkinter-GUI-making-/Part-06-(iconbitmap).ico')

# input
e = Entry(root, width=20,  borderwidth=5, font=('Courier', 12, 'bold'))
e.grid(row=0, column=0, columnspan=4, padx=2, pady=5)
#e.pack() use grids to simply design


# process as defs
box = ''
error = False
def typing(key):  # typed nuimbers display on the input box
  global box
  box = box + key
  disp = box
  if (len(box)>20):
    extra = len(box)-20
    disp = (str(box)[extra:])
  e.delete(0, END)
  e.insert(0, disp)

def equal():
  global eql, box
  try:
    eql = eval(box)
    box = str(eql) # for continue the math with already made answer
    if len(str(box))>20:
      expo = math.floor(math.log10(abs(eql)))  # Find exponent  **(+-X)
      scint = eql / (10**expo)  # Normalize number to scientific notation
      eql = f'{expo}×10^{scint}'
  except (ZeroDivisionError, SyntaxError):  # handle zero division error and syntax errors
    eql = 'Error'
    box = ''
  e.delete(0, END)
  e.insert(0, eql)
  
      
def allclear():  # all clear the input box
  global box
  e.delete(0, END)
  box = ''

def backspace():
  global box
  box = box[:-1]
  typing('')
  
# buttons with positions, use grid()
# numbers
btnnums = [['1',1,0], ['2',1,1], ['3',1,2], ['4',1,3], ['5',2,0], ['6',2,1], ['7',2,2], ['8',2,3], ['9',3,0], ['0',3,1], ['.',5,0]]
for (txt, r, c) in btnnums:
  if txt=='.':
    btn = Button(root, text=txt, command=lambda txt=txt: (typing(txt)), padx=16, pady=1, bg='#FFDE21', font=('Helvetica', 17, 'bold'))
  else:
    btn = Button(root, text=txt, command=lambda txt=txt: (typing(txt)), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
  # lambda: (typing(txt)) - for none iteration places
  # lambda txt=txt: (typing(txt)) - for iterating places, because lambda uses last assigned value, so we need to assign them
  btn.grid(row=r, column=c)

# arithmetic operators and .
btnarm = [['*',4,0], ['/',4,1], ['+',4,2], ['-',4,3]]
for (txt, r, c) in btnarm:
  if txt=='+':
    btn = Button(root, text=txt, command=lambda txt=txt: (typing(txt)), padx=15.4,pady=3, bg='#0060BF', font=('Helvetica', 15, 'bold'))
  elif txt=='/':
    btn = Button(root, text=txt, command=lambda txt=txt: (typing(txt)), padx=17,pady=3, bg='#0060BF', font=('Helvetica', 16, 'bold'))
  else:
    btn = Button(root, text=txt, command=lambda txt=txt: (typing(txt)), padx=17,pady=3, bg='#0060BF', font=('Helvetica', 15, 'bold'))
  btn.grid(row=r, column=c)
  
# results and clears
buttonclr = Button(root, text='AC', command=allclear, padx=16, pady=11, bg="#C40000", font=('Helvetica', 9, 'bold'))
buttonclr.grid(row=3, column=2)

buttondel = Button(root, text='⌫', command=backspace, padx=16, pady=11, bg='#C45924', font=('Helvetica', 9, 'bold'))
buttondel.grid(row=3, column=3)

buttoneql = Button(root, text='=', command=equal, padx=70, pady=1, bg='#1DA80E', font=('Helvetica', 17, 'bold'))
buttoneql.grid(row=5, column=1, columnspan=3)


root.mainloop()
