import random
import time
import sys


class Pet:
    def __init__(self, name, age, happy, hunger, thirst, death, time, timeHours):
        self.name = name
        self.age = age
        self.happy = happy
        self.hunger = hunger
        self.thirst = thirst
        self.death = death
        self.dead = False
        self.time = time
        self.timeHours = timeHours

    def die(self, ouch):
        self.death += ouch
        if(self.death >= 100):
            return True
        if(self.death <= 0):
            self.death=0   
        return False

    def feed(self,food):
        self.hunger -=food
        if(self.hunger>100):
            self.hunger=100
            self.die(10)
        if(self.hunger <0):

            self.die (-10)
            self.hunger=0
    def drink(self, water):
        self.thirst -= water
        if(self.thirst < 0):
            self.thirst = 0   
        if(self.thirst > 100):
            self.thirst = 100
            self.die(10)
    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    def punch(self, hit):
        if(not self.die(hit)):
            if(self.happy <= 0):
                self.happy = 0
                self.die(hit)    
    def ageUp(self, time):
        if(time - self.time > 50):
            self.age += int((time - self.time) / 50)
            self.time = time
            return True
        return False

    def happiness(self, amount):
        if(self.happy <= 0):
            self.happy = 0
            self.die(5)
        else:
            self.happy += amount
    def status(self):
        print("\nName: %s, Age: %d, Hunger: %d, Thirst: %d, Happiness: %d, Death: %d" % (self.name, self.age, self.hunger, self.thirst, self.happy, self.death))

def playGame(thePet):
        choice=1
        while(choice!=0):
                theTime = int(time.time())
                choice = int(input("What would you like to do?\n0 Quit, 1 Feed, 2 Thirst, 3 Punch, 4 Status: "))
                if (choice == 0):
                    sys.exit()
                if (choice == 1):
                    thePet.feed(20)
                if (choice == 2):
                    thePet.drink(20)
                if (choice == 3):
                    thePet.punch(10)
                if (choice == 4):
                    thePet.status()
                if (thePet.die(0)):
                    print(self.name + "suddenly died")
                if (thePet.ageUp(int(time.time()))):
                    print("%s is now a year older!" % (thePet.getName(), thePet.getAge()))
                thePet.happiness(-5)
                thePet.feed(-5)
                thePet.drink(-5)
                print()


def newPet(petName):
        newPet = Pet(petName.replace(' ', '_'), 0, 50, 20, 20, 0, int(time.time()), int(time.time()))
        return newPet

newgame= input("What would you name your new pet?")
playGame(newPet(newgame))
