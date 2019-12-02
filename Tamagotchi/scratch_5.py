from tkinter import *

okToPressReturn=True

hunger=20
thirst=20
boredom=20
age=0

def start(event):
    global okToPressReturn

    if okToPressReturn==False:
        pass
    else:
        startLabel.config(text="")
        updatehunger()
        updatethirst()
        updateboredom()
        updateage()
        display()
        okToPressReturn = False
def display():
    global thirst
    global hunger
    global boredom
    global age

    if hunger==100 or boredom==100 or thirst==100:
        catPic.config(image=Gameover)
    hungerLabel.config(text="Hunger:  " + str(hunger))
    thirstLabel.config(text="Thirst:  " + str(thirst))
    boredomLabel.config(text="Boredom:   " + str(boredom))
    ageLabel.config(text="Age:" + str(age))
    catPic.after(500,display)
def updatehunger():
    global hunger
    hunger += 1
    if isAlive():
        hungerLabel.after(500,updatehunger)
def updatethirst():
    global thirst
    thirst += 1
    if isAlive():
        thirstLabel.after(500,updatethirst)
def updateboredom():
    global boredom
    boredom += 1
    if isAlive():
        boredomLabel.after(500,updateboredom)
def updateage():
    global age
    if isAlive():
        ageLabel.after(5000,updateage)
        age += 1

def feed():
    global hunger
    if hunger>=100:
        hunger=100
    if hunger<100:
        hunger-=10
    if hunger<=0:
        hunger =0
def water():
    global thirst
    if thirst>=100:
        thirst=100
    if thirst<100:
        thirst-=10
    if thirst<=0:
        thirst =0
def bored():
    global boredom
    if boredom>=100:
        boredom=100
    if boredom<100:
        boredom-=10
    if boredom<=0:
        boredom=0
def isAlive():
    global hunger
    global boredom
    global thirst

    if hunger>=100 or boredom>=100 or thirst>=100:
        startLabel.config(text="""GAME OVER!
                Your Pet Died!!""")
        return False
    else:
        return True
def close_window():
    import sys
    sys.exit()

#-------------------------------------------------------------------

root=Tk()
root.title("Tamagotchi")
root.geometry("400x600")

startLabel = Label(root, text="Press 'Enter' to start!", font=('Arial', 20))
startLabel.pack()
titlephoto = PhotoImage(file = "giphy.gif")
Gameover= PhotoImage(file="gameover.gif")
catPic = Label(root, image=titlephoto)
catPic.pack()
hungerLabel = Label(root, text="Hunger:   " + str(hunger), font=('Helvetica', 12))
hungerLabel.pack()


thirstLabel = Label(root, text="Thirst:   " + str(thirst), font=('Helvetica', 12))
thirstLabel.pack()


boredomLabel = Label(root, text="Boredom:   " + str(boredom), font=('Helvetica', 12))
boredomLabel.pack()



ageLabel = Label(root, text="Age: " + str(age), font=('Helvetica', 12))
ageLabel.pack()

buttonFeed = Button(root, text="Feed Me", font = "Arial", foreground = "black", activebackground="blue",
                            width=20, command=feed)
buttonFeed.pack()

buttonThirst = Button(root, text="Water Me", font = "Arial", foreground = "black", activebackground="blue",
                            width=20, command=water)
buttonThirst.pack()
buttonBoredom = Button(root, text="Play With Me", font = "Arial", foreground = "black", activebackground="blue",
                            width=20, command=bored)
buttonBoredom.pack()


buttonEnd = Button (root, text="Quit", foreground = "black", activebackground="blue",
                            font = "Arial", width=20, command=close_window)
buttonEnd.pack()

root.bind('<Return>', start)

root.mainloop()





