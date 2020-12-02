##Author:- Rohit Kavitake

#importing modules....
from tkinter import *
from time import sleep
import tkinter
from tkinter.ttk import  *
import tkinter.font as font

amount=0
def simpleInterest(p,n,r):
    try:
        p = int(p.get())
        n = int(n.get())
        r = int(r.get())
        principleAmount = p
        interest = float((p*n*r)/100)
        amount = principleAmount+interest
        interestText.set("Total Interest::{:.2f}".format(float(interest)))
        resultText.set("Total amount::{:.2f}".format(float(amount))+"Rs")
    except:
        resultText.set("Enter correct Values")
        interestText.set("     ")

    

def compoundInterest(p,n,r):
    try:
        p = float(p.get())
        n = float(n.get())
        r = float(r.get())
        principleAmount = p
        rate = float((r/100)+1)
        nyears = rate**n
        amount = principleAmount*nyears
        interest = amount - principleAmount
        interestText.set("Total Interest::{:.2f}".format(float(interest)))
        resultText.set("Total amount::{:.2f}".format(float(amount))+"Rs")
    except:
        resultText.set("Enter correct Values")
        interestText.set("     ")


#print(simpleInterest(100,25,10))
##Gui...
root = tkinter.Tk()
root.title("Interest Calculator")
root.geometry("270x300")

namelbl = Label(root,text="Developed by:- Rohit Kavitake",background="grey", foreground='black')
namelbl.place(x=90,y=275)



myfont = font.Font(size=15)
name = Label(root,text="Interest Calculator",background="cyan", foreground='black',font=myfont)
name.place(x=50,y=30)

prinyentry = Label(root,text="Principal amount:")
prinyentry.place(x=10,y=90)

principal = Entry(root,text="enter amount here")
principal.place(x=130,y=90)


yearslbl = Label(root,text="Time Period(years):")
yearslbl.place(x=10,y=130)

years= Entry(root,text="The time period in years")
years.place(x=130,y=130)

ratelbl = Label(root,text="Rate(%)/anum")
ratelbl.place(x=10,y=170)

rate = Entry(root,text="Rate of interest")
rate.place(x=130,y=170)

si = Button(root,text=" Simple Interest ",command=(lambda p=principal,n=years,r=rate: simpleInterest(p,n,r)))
si.place(x=10,y=200)

ci = Button(root,text=" Compound Interest ",command=(lambda p=principal,n=years,r=rate: compoundInterest(p,n,r)))
ci.place(x=140,y=200)

resultText = StringVar()
resultText.set("                    Go")

interestText = StringVar()
interestText.set("Enter the correct integers")

interestlbl = Label(root,textvariable=interestText)
interestlbl.place(x=50,y=230)
mount = Label(root,textvariable=resultText)
mount.place(x=50,y=250)

root.mainloop()