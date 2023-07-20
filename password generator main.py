from tkinter import *
import string
import random
from PIL import ImageTk, Image
import pyperclip 
import tkinter.font as font
mainwindow= Tk()
mainwindow.title('Welcome to password generator')
mainwindow.geometry('620x620')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='purple')
passwordLabel=Label(mainwindow,text='Welcome to password generator',font=('algerian',20,'bold'))
passwordLabel.pack(ipadx=0.5,ipady=1.5)


def start():
 root=Toplevel(mainwindow)
 root.config(bg='purple')
 root.geometry("600x600")
 root.resizable(0,0)
 choice=IntVar()
 Font=('algerian',23,'bold')
 



 def generator():
  small_alphabets=string.ascii_lowercase
  capital_alphabets=string.ascii_uppercase
  numbers=string.digits
  special_charecters=string.punctuation
  all=small_alphabets+capital_alphabets+numbers+special_charecters
  password_length=int(length_Box.get())


  if choice.get()==1:
    passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

  if choice.get()==2:
    passwordField.insert(0,random.sample(small_alphabets+capital_alphabets+numbers,password_length))

  if choice.get()==3:
    passwordField.insert(0,random.sample(small_alphabets+capital_alphabets+numbers+special_charecters,password_length))

 #password=random.sample(all,password_length)
 #passwordField,insert(0,password)
 def copy():
   random_password=passwordField.get()
   pyperclip.copy(random_password)





 passwordLabel=Label(root,text='password generator',font=('algerian',35,'bold'),bg='gray20',fg='white')
 passwordLabel.grid(padx=0.5,pady=1.5)
 weakradioButton=Radiobutton(root,text='weak',value=1,variable=choice,font=Font)
 weakradioButton.grid(pady=5)

 mediumradioButton=Radiobutton(root,text='medium',value=2,variable=choice,font=Font)
 mediumradioButton.grid(pady=5)

 strongradioButton=Radiobutton(root,text='strong',value=3,variable=choice,font=Font)
 strongradioButton.grid(pady=5)

 lengthLabel=Label(root,text='password length',font=Font,bg='gray20',fg='white')
 lengthLabel.grid(pady=5)

 length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
 length_Box.grid(pady=5)
 generateButton=Button(root,text='generate',font=Font,command=generator)
 generateButton.grid(pady=5)


 passwordField=Entry(root,width=25,bd=2,font=Font)
 passwordField.grid()

 copyButton=Button(root,text='copy',font=Font, command=copy)
 copyButton.grid(pady=5)


myFont = font.Font(size=30,family='algerian')

clickmebutton=Button(mainwindow,text="click here",activebackground="pink",command=start)
clickmebutton['font']= myFont

clickmebutton.pack(ipadx=20,ipady=20,expand=TRUE)





mainwindow.mainloop()