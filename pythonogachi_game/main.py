#This is the pythonogachi game 
import random
class Creature:

    def __init__(self,name):

        self.name=name.title()

        #attributes for the creature 
        self.hunger=0
        self.bordem=0
        self.tiredness=0
        self.dirtiness=0

        #food inventory
        self.food=0 #to track food the creature have
        self.is_alive=True # to track whether the creature alive or not
        self.is_sleeping=False# to track whether the creature is sleeping or not
        
    def eat(self):
        #to stimulate the eating of creature 
        if self.food>0:
            self.food-=1
            self.hunger-=random.randint(1,4)
            print("yUMMM.....")
            print(self.name+' GOT A GREAT MEAL')
        else:
            print("OOPSS NO FOOD IS THERE, GO FOR FORAGE") 
        if self.hunger<0:
            self.hunger=0
        

    def sleep(self):
        #THIS METHOD SLEEPING OF CREATURE WHICH WILL REDUCE TIREDNESS AND BORDEM
        self.is_sleeping=True
        self.bordem-=1
        self.tiredness-=3

        print("ZZZZzzzzzz....zzzzZZZZ.....zzzzzZZZZ")
        if self.bordem<0:
            self.bordem=0
        if self.tiredness<0:
            self.tiredness=0

    def forage(self):
        #creature will get random food ..
        food_value=random.randint(0,3)
        self.food+=food_value
        self.dirtiness+=2
        print(self.name+" Got "+str(food_value)+" food....")

    def clean(self):
        #cleaning the creature 
        self.dirtiness=0
        print(self.name+" Got a great bath...")


    def awake(self):
        #stimulating the waking of creature
        value=random.randint(0,2) # 1/3 chance for creature to get wakeup 
        if value==0:
            self.is_sleeping=False
            self.tiredness=0
            print(self.name+" just woke up ......")
        else:
            print(self.name+" is not waking up ....")
            self.sleep()


    def play(self):
        #here the creature is going to play a guessing game
        print("WANT TO PLAY A GAME.....")
        print(self.name+" IS GOING TO THINK OF A NUMBER BTW 0,1,2")
        value=random.randint(0,3)
        guess=int(input("PLEASE ENTER U  GUESS>>"))
        if value==guess:
            print("HURREEYYYY U GOT THE CORRECT Number....")
            self.bordem-=3
        else:
            print("OHH U R WRONG .... "+self.name+"'S NUMBER WAS "+str(value)+".")
            self.bordem-=1
        if self.bordem<0:
            self.bordem=0
        

    def show_values(self):
        #show the current stage of creature
        #print("Creature name : "+self.name)
        print("Hunger[0-10]:    "+str(self.hunger))
        print("Bordem[0-10]:    "+str(self.bordem))
        print("Tiredness[0-10]: "+str(self.tiredness))
        print("Dirtyness[0-10]  "+str(self.dirtiness))
        print("-------------------")
        print("Food inventory:  "+str(self.food))
        print("-------------------")

        if self.is_sleeping:
            print("Sleeping status: Sleeping")
        else:
            print("Sleeping status: Awake")
       
    def increament_values(self,diff):
          #increment the values of creature
          """increamenting hunger and dirtness regardless of sleep or awake"""
          self.hunger+=random.randint(0,diff)
          self.dirtiness+=random.randint(0,diff)
          """increamenting bordem and tiredness if creature is not sleeping """
          if self.is_sleeping==False:
              self.tiredness+=random.randint(0,diff)
              self.bordem+=random.randint(0,diff)
    def kill(self):
        #setting the kill scenario
        if self.hunger>=10:
            self.is_alive=False
            print(self.name+" Died due to starvation ....")
        elif self.dirtiness>=10:
            self.is_alive=False
            print(self.name+" died due to infection...")
        elif self.tiredness>=10:
            self.tiredness=10
            print(self.name+" is tired.. going to sleep..")
            self.is_sleeping=True
        elif self.bordem>=10:
            self.bordem=10
            print(self.name+" is bordem so such .. going to sleep..")
            self.is_sleeping=True
        
def show_menu(creature):

    if creature.is_sleeping==True:
        choice=input("ENTER [6] TO AWAKE THE CREATURE")
        choice='6'
    else:
        print()
        print("Enter [1] to eat:")
        print("Enter [2] to play:")
        print("Enter [3] to forage:")
        print("Enter [4] to sleep")
        print("Enter [5] to take bath")
        choice=input("what is u r choice")
    return choice
def call_actions(creature,choice):
    if choice=='1':
        creature.eat()
    elif choice=='2':
        creature.play()
    elif choice=='3':
        creature.forage()
    elif choice=='4':
        creature.sleep()
    elif choice=='5':
        creature.clean()
    elif choice=='6':
        creature.awake()
    else:
        print("invalid entry..")

#this is the main loop of the game
running=True
while running:
    print("Welcome to Pythonagachi Game...")
    diff=int(input("Please enter the diffulty level [1-5]"))
    if diff<1:
        diff=1
    elif diff>10:
        diff=10
    name=input("Hey please enter u r creature name..")
    creature=Creature(name)
    print(creature.name+" Ready to play ....")
    round=1
    creature.increament_values(diff)
    while creature.is_alive:
        print("Round #"+str(round))
        print("--------------------------------------------------------------")
        creature.show_values()
        choice=show_menu(creature)
        print()
        call_actions(creature,choice)
        print("After effect")
        print("----------------------------------")
        creature.show_values()
        input("press enter to continue..")
        creature.increament_values(diff)
        creature.kill()
        print("----------------------------------------------------------------")

        round+=1
    print("R I P ")   
    print(creature.name+" survived for"+str(round)+" rounds")
    userinput=input("Do u want to continue... this game(y/n)").lower()
    if userinput!='y':
        running=False
        print("Thank u for playing  Pythonagachi game....")

        
    