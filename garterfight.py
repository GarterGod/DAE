
#untitlded.jam
#"turns the userinput into an integer"
def conversion():
    global Userinput
    Userinput=int(Userinput)

import random
#"random event selection"
def Roll():
    global numberlist
    random_numbers = {random.randint(1,20) for _ in range(1)}  
    numberlist = list(random_numbers)
    print(f"you rolled a {numberlist[0]}")
    
#"Garter fight"
print("input Username")
UserName=input("   :")
print("welcome to Garter fight")
print("you are an adventerer in snake woods looking for Super Serpint the lord of snakes ")
print("you have come because the snakes are spareading far and wide taking over what was once human lands")
print("As you wonder into a clearing you come across the GARTER SNAKE OF BEGININGS") 
print()
Userinput=int(input("challenge the GARTER SNAKE OF BEGININGS 1 for yes 2 for no    "))
print() 
while Userinput<1 or Userinput>1:
    while Userinput<1 or Userinput>2:
         Userinput=input("please  select 1 for yes or 2 for no   ")
         print()
    print("IT'S A SNAKE KILL IT")
    Userinput=int(input("please  select 1 for yes or 2 for no     "))
    print()

if Userinput==1:
    Roll()
 
   #natural 1  you trip
    if numberlist[0]==1:
        print("you run foward but you get ambushed by a rock luckily your foot was already oh a path to handle it but the rock did manage to knock you prone in the proccess")
        print("the GARTER SNAKE OF BEGININGS laughs at you for your stupidity") 
        Userinput=int(input("would you like to continue fighting 1 for yes 2 or no    "))
        print() 
        while Userinput<1 or Userinput>2:
            Userinput=int(input("please  select 1 for yes or 2 for no   "))
            print()
        #you crush the snake r1
        if Userinput==1:
            print("you get back up on your feet and charge towards the beast")
            print("your body fills with energy")
            print("you leap foward shooting your fist out with great force crushing the body of the still uprigght snake")
            print("good job")
            print("you killed a gartter snake")
            Roll()
            Userinput=int(input("would you like to loot it 1 for yes 2 for no   "))
            print() 
            while Userinput<1 or Userinput>2:
                Userinput=input("please  select 1 for yes or 2 for no   ")
                print()
            # you loot it  r1
            if Userinput==1:
                print("you grab its bag and walk away you won")
                print("you wonder into another clearing about a mmile from the first")
                print("sunlight is disapearing rapidly so you decide to set up camp on a hill with a veiw")
                print("you wake up you here hissing all around you")
            #run from corpse r1
            else:
                print("you run awway not trusting that the GARTER SNAKE OF BEGININGS was truly so weak")
                print("you find yourself deep in the woods inside of a deer den which is suprisingly comfy ")
                print("as the sun flickers out you doze off")
                print("you wake up you could set up base here or you can wander deeper")
        #trip and stay still r1
        else:
            print("you lie motionles the GARTER SNAKE OF BEGININGS slithers over ")
            print("it begins examining you to see if your dead")
            print("now is the perfect moment to stike")
            Userinput=int(input("attck 1 for yes 2 for no   "))
            print() 
            while Userinput<1 or Userinput>2:
                Userinput=int(input("please  select 1 to attack 2 lay still   "))
                print()



 
 #this is less 11  yoted         
    elif numberlist[0]<11:
        print("You grin runing foward and plunging your blade in to the GARTER SNAKE OF BEGININGS body")
        print("It looks down disapointed only to pick you up and launch you deep into the surrounding woods")
        print("you dont have your sword there are only trees and grass around you ")
        print("what do you do")
        Userinput=int(input("1 for wander 2 for sit still   "))
        print()
        
        while Userinput<1 or Userinput>2:
            Userinput=int(input("please  select 1 for wander or 2 for stay   "))
            print()
        #wander and find mirror r<11
        if Userinput==1:
            print("you get up on you feet and begin to walk you look around to see everything aroound you and iit is breathtakingly beutiful ")
            print("you realise that nature is more than just plants it is everything around you")
            print("once you reach this conclusion you come across a club it may not be your sword but it will do for now")
            print("you come across another wandering adventurer who is mimicking you with a club almost exactly like yours")
            Userinput=int(input("1 attack this brute, 2 talk to this person, or 3 run "))
           
            while Userinput<1 or Userinput>2:
                Userinput=int(input("please  select 1 for fight 2 for talk or 3 for flee   "))
                
            #remain seated hear noise r<11
        else:
            print("you decide to sit still"     )
            print()
            print("after a minute you here the faint sound of air moving even though there is no wind")
            Userinput=int(input("would you like to 1 look for the source of the noise or 2 sit still    "))
            while Userinput<1 or Userinput>2:
                Userinput=int(input("please  select 1 for search 2 to remain where you are   "))
                print()
   
    #natural 20 kill it
    elif numberlist[0]==20:
       print()
       print("You jump upwards far above the GARTER SNAKE OF BEGININGS head ")
       print("launch you blade straight at it in pure shock the GARTER SNAKE OF BEGININGS can do nothing but stare as it's imapaled upon your sword")
       print("you grab you sword and stare down at its pitiful body")
       print("+20 EXP")

       Userinput=int(input("1 to bury it 2 to loot it     "))
       print()
       while Userinput<2 or Userinput>2:
        Userinput=int(input("input 2 to loot the GARTER SNAKE OF BEGININGS      "))
        print()
        print()
       print("you grab its bag and leave no point in wasting your time")

    


    #more than 10 slash the bag
    else:
        
        print("you leap at the GARTER SNAKE OF BEGININGS weaving between it's attacks and slicing at its body but you miss and accidently hit the GARTER SNAKE OF BEGININGS bag ")
        print("tens of maps spill out along with a few compasses ")
        print()
        Userinput=int(input("1 to keep attacking 2 to run away "     ))
       
        print() 
        while Userinput<1 or Userinput>2:
            Userinput=input("please select 1 to continue 2 to run   ")
            print()
        if Userinput==1:
            #you kill it r>10
            print("as the GARTER SNAKE OF BEGININGS is distracted as stuff falls from it's bag ")
            print("you jump at the chance and stab the blasted creature in the neck  ")
        #you run fom cops r>10
        else:
            print("you sprint away realising this was a ploy to convict you just because you protected yourself from a snake")


print()
print()
print("You have finished the Demo Good Job but you only got 1 of many endings and remember this game is")
print("10% luck 20% skill 15% concentrated power of will 5% pleasure 50% pain 100% reason to remember your name")
print(f"Good job {UserName}")
print()
print()