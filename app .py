import tkinter
from tkinter import *

root = tkinter.Tk()
root.title('Number in Mind')
root.geometry('640x360')
root.config(background =  "light green")
lbl = Label(root, text='Hello Everyone', font = ('BankGothic Md BT',40),bg = "light green")
lbl1 = Label(root, text = "This is my Simple Math Game \nusing Tkinter", font = ('BankGothic Md BT',25),bg = "light green")
lbl.place(x=80,y=50)
lbl1.place(x=40,y=130)
a = []

def homePage():
    nw = tkinter.Toplevel(root)
    nw.geometry('640x360')
    nw.config(background = "yellow")
    l1 = Label(nw, text = "Choose any number \nbetween 1 to 10", bg = "yellow", font = ('BankGothic Md BT',30))
    l2 = Label(nw, text = "\n1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n 10\n", bg = "yellow", font = ('BankGothic Md BT',20))
    b1 = Button(nw, text = "  Okay  ",command=lambda:[exitnw1(), gamePage1()], font = ('BankGothic Md BT',20), bg = '#ecb3ff')

    l1.pack()
    l2.place(x=50,y=50)
    b1.place(x=300,y=250)
    root.withdraw()

    def exitnw1():
        nw.destroy()
        

def gamePage1():
    nw1 = Toplevel(root)
    nw1.geometry('640x360')
    nw1.config(background = "pink")
    l1 = Label(nw1, text = "Click Yes if the number \nis present in the list\n If not Click No", bg = "pink", font = ('BankGothic Md BT',30))
    l2 = Label(nw1, text = "\n1\n 3\n 7\n 8\n 10\n", font = ('BankGothic Md BT',20))
    b1 = Button(nw1, text = "  Yes  ",
                            command=lambda m = "1":[exitnw1(), gamePage2(),res(m)], font = ('BankGothic Md BT',20))
    
    b2 = Button(nw1, text = "  No   ",
                            command=lambda m = "2":[exitnw1(), gamePage2(),res(m)], font = ('BankGothic Md BT',20))

    l1.pack()
    l2.place(x=50,y=150)
    b1.place(x=400,y=190)
    b2.place(x=400,y=250)
    
    def exitnw1():
        nw1.destroy()

def gamePage2():
    
    nw1 = Toplevel(root)
    nw1.geometry('640x360')
    nw1.config(background = "#99ccff")
    l1 = Label(nw1, text = "Click Yes if the number \nis present in the list\n If not Click No", bg = "#99ccff", font = ('BankGothic Md BT',30))
    l2 = Label(nw1, text = "\n1\n 4\n 9\n 10\n", font = ('BankGothic Md BT',20))
    b1 = Button(nw1, text = "  Yes  ",
                            command=lambda m = "3":[exitnw1(), gamePage3(), res(m)], font = ('BankGothic Md BT',20))
    
    b2 = Button(nw1, text = "  No   ",
                            command=lambda m = "4":[exitnw1(), gamePage3(), res(m)], font = ('BankGothic Md BT',20))

    l1.pack()
    l2.place(x=50,y=150)
    b1.place(x=400,y=190)
    b2.place(x=400,y=250)
    def exitnw1():
        nw1.destroy()

def gamePage3():
    
    nw1 = Toplevel(root)
    nw1.geometry('640x360')
    nw1.config(background = "#ff9999")
    l1 = Label(nw1, text = "Click Yes if the number \nis present in the list\n If not Click No", bg = "#ff9999", font = ('BankGothic Md BT',30))
    l2 = Label(nw1, text = "\n1\n 5\n 6\n 8\n 9\n 10\n", font = ('BankGothic Md BT',20))
    b1 = Button(nw1, text = "  Yes  ",
                            command=lambda m = "5":[exitnw1(), gamePage4(), res(m)], font = ('BankGothic Md BT',20))
    
    b2 = Button(nw1, text = "  No   ",
                            command=lambda m = "6":[exitnw1(), gamePage4(), res(m)], font = ('BankGothic Md BT',20))

    l1.pack()
    l2.place(x=50,y=150)
    b1.place(x=400,y=190)
    b2.place(x=400,y=250)
    def exitnw1():
        nw1.destroy()

def gamePage4():
    
    nw1 = Toplevel(root)
    nw1.geometry('640x360')
    nw1.config(background = "#ff9980")
    l1 = Label(nw1, text = "Click Yes if the number \nis present in the list\n If not Click No", bg = "#ff9980", font = ('BankGothic Md BT',30))
    l2 = Label(nw1, text = "\n1\n 2\n 3\n 5\n 8\n 9\n", font = ('BankGothic Md BT',20))
    b1 = Button(nw1, text = "  Yes  ",
                            command=lambda m = "7":[exitnw1(), res(m), resultPage()], font = ('BankGothic Md BT',20))
    
    b2 = Button(nw1, text = "  No   ",
                            command=lambda m = "8":[exitnw1(), res(m), resultPage()], font = ('BankGothic Md BT',20))

    l1.pack()
    l2.place(x=50,y=150)
    b1.place(x=400,y=190)
    b2.place(x=400,y=250)
    def exitnw1():
        nw1.destroy()

def resultPage():
    
    nw1 = Toplevel(root)
    nw1.geometry('640x360')
    nw1.config(background = "sky blue")
    l1 = Label(nw1, text = "Let Me Guess The Answer is....", bg = "sky blue", font = ('BankGothic Md BT',20))
    T = Text(nw1, height = 5, width = 52, font = ('BankGothic Md BT',20))
    #print(a)
    b = [1,3,5,7]
    c = [2,4,6,7]
    d = [1,4,6,7]
    e = [2,3,6,8]
    f = [2,4,5,7]
    g = [2,4,5,8]
    h = [1,4,6,8]
    i = [1,4,5,7]
    j = [2,3,5,7]
    k = [1,3,5,8]
    if a == b:
        num = "1"
    elif a == c:
        num = "2"
    elif a == d:
        num = "3"
    elif a == e:
        num = "4"
    elif a == f:
        num = "5"
    elif a == g:
        num = "6"
    elif a == h:
        num = "7"
    elif a == i:
        num = "8"
    elif a == j:
        num = "9"
    elif a == k:
        num = "10"
    else:
        num = "Invalid Error...\nPlease choose number between 1 to 10"
    b1 = Button(nw1, text = "  Start Again  ",
                            command=lambda:[returnHome(), exitnw1()], font = ('BankGothic Md BT',20))
    
    b2 = Button(nw1, text = "  Exit  ",
                            command=closeWindow, font = ('BankGothic Md BT',20))

    l1.pack()
    T.pack()
    b1.place(x=200,y=190)
    b2.place(x=200,y=250)
    T.insert(tkinter.END, num)
    def exitnw1():
        nw1.destroy()

def res(m):
        s=int(m)
        a.append(s)
        return a


def returnHome():
    #root.iconify()
    a.clear()
    root.deiconify()
def closeWindow():
    root.destroy()

     

btn = Button(root, text = "Start the Game" ,
             fg = "red", command=homePage, font = ('BankGothic Md BT',20))
btn.place(x=200,y=280)
root.mainloop()
    
