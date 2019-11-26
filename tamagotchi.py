import random
import time
import sys


class Pet:
    def __init__(self, name, age, happy, hunger, thirst, death, time, hours):
        self.name = name
        self.age = age
        self.happy = happy
        self.hunger = hunger
        self.thirst = thirst
        self.death = death
        self.dead = False
        self.time = time
        self.hours= hours

    def die(self, ouch):
        self.death += ouch
        if(self.death >= 100):
            return True
        return False

    def feed(self,food):
        self.hunger -=food
        if(self.hunger>100):
            self.hunger=100
            self.die(10)
        if(self.hunger <0):
            self.hunger=0
    def water(self, water):
        self.thirst -= water
        if(self.thirst < 0):
            self.thirst = 0   
        if(self.thirst > 100):
            self.thirst = 100
            self.die(10)

    def game(self):
        rInt = random.randint(0, 10)
        guess = int(input(self.name + " is thinking of a number between 0 and 10. What is it? "))
        if(guess == rInt):
            print("You guessed right!")
            return True
        print("Nope!")
        return False

    def play(self, game, exp):
        print()
        won = False
        won = self.game()
        if(won):
            if(self.happy + game > 100):
                self.happy = 100
            else:
                self.happy += game
            if(self.hunger >= 100 or self.thirst >= 100):
                self.die(5)
            self.feed(-exp)
            self.water(-exp)

    def punch(self, hit):
        if(not self.die(hit)):
            if(self.happy <= 0):
                self.happy = 0
                self.die(hit)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

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

    def randomBehavior(self):
        rInt = random.randint(0, 40)
        if(rInt == 4):
            print(self.name + " played ball by himself! + 5 Happiness" )
            self.happy += 5
        if(rInt == 23):
            print(self.name + " fell down the balcony. " + self.name + " got hurt..... +5 Death ")
            self.die(5)
        if(rInt == 35):
            print(self.name + " woke up and fell ill.... +5 Death") 
        if(rInt == 15):
            print(self.name + " ate your leftover pizza.... -10 Hunger")
            self.feed(2)

    def status(self):
        print("\nName: %s, Age: %d, Hunger: %d, Thirst: %d, Happiness: %d, Death: %d" % (self.name, self.age, self.hunger, self.thirst, self.happy, self.death))

    def whenUserisgone(self,time):
        timegone = int((time - self.timeHours) / 3600)
        self.feed(-timegone)
        self.water(-timegone)
        self.happiness(-timegone)
    def savegame(self,time):
        saveFile = open(self.name + ".pet", 'w')
        saveFile.write(
                self.name + " " + str(self.age) + " " +
                str(self.hunger) + " " + str(self.thirst) + " " +
                str(self.happy) + " " + str(self.death) + " " +
                str(self.time) + " " + str(time))
        saveFile.close

def playGame(thePet):
    choice= 1
    while (choice != 0):
        try:
            theTime = int(time.time())
            choice = int(input("What would you like to do?\n0 Quit, 1 Play, 2 Feed, 3 Water, 4 Punch, 5 Status: "))
            thePet.randomBehavior()
            if (choice == 0):
                sys.exit()
            if (choice == 1):
                thePet.play(25, 10)
            if (choice == 2):
                thePet.feed(20)
            if (choice == 3):
                thePet.water(20)
            if (choice == 4):
                thePet.punch(10)
            if (choice == 5):
                thePet.status()
            if (thePet.die(0)):
                print("You killed" + self.name +"...!!!")
                main()
            if (thePet.ageUp(int(time.time()))):
                print("%s is now a year older! It is %d years old!" % (thePet.getName(), thePet.getAge()))
            thePet.happiness(-5)
            thePet.feed(-5)
            thePet.water(-5)
            thePet.savegame(int(time.time()))
            print()

        except:
            print()

def newPet(petName):
    newPet = Pet(petName.replace(' ', '_'), 0, 50, 20, 20, 0, int(time.time()), int(time.time()))
    return newPet

def loadgame(petName):
    petInfo = open(petName.replace(' ', '_') + ".pet", 'r')
    petList = petInfo.read()
    petList = petList.split(' ')
    newPet = Pet(petList[0], int(petList[1]), int(petList[2]), int(petList[3]), int(petList[4]), int(petList[5]),
                 int(petList[6]), int(petList[7]))
    newPet.whenUserisgone(int(time.time()))
    playGame(newPet)    
def main():
    try:
        choice=int(input("Would you like create a new Pet or load saved pet? (0, 1) "))
        if(choice==1):
            petName = input("What is the name of your saved pet? ")
            loadgame(petName)
        if(choice==0):
            petName = input("What would you name your new pet? ")
            playGame(newPet(petName))
        else:
            main()
    except:
        main()


if __name__ == "__main__":
    main()
