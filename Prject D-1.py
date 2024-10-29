import random
import time
#Math Pong
def Roll():
    global Maximum
    global Minumum
    global NumberRolled
    import random
    random_number=random.randint(Minumum, Maximum) 
    NumberRolled = random_number
    #Creates a random number within set boundries(minumum and Maximum)
Repetions=0
def Subtracting():
    global Net
    global Ball
    global NumberRolled
    if NumberRolled<0:
        Ball=Ball-NumberRolled
        NumberRolled=NumberRolled*-1
        print(f"Adding {NumberRolled}")
        print()
        print(Ball)
        print()
    else:
        print(f"Subtracting {NumberRolled}")
        Ball=Ball-NumberRolled
        print()
        print(Ball)
        print()
def Adding():
    global Net
    global Ball
    global NumberRolled
    Roll()
    if NumberRolled<0:
        Ball=Ball+NumberRolled
        NumberRolled=NumberRolled*-1
        print(f"Subtracting {NumberRolled}")
        print()
        print(Ball)
        print() 
    else:
        print(f"Adding {NumberRolled}")
        Ball=Ball+NumberRolled
        print()
        print(Ball)
        print()    
Maximum=0
Minumum=0
while Maximum-Minumum<1:
    print()
    Maximum=int(input("Maximum   "))#this has the user set the maximum boundry
    print()
    Minumum=int(input("Minumum   ")) #this has the user set the minumum boundry
print()  
Net=int(input("What Number Do You Wish The Net To Be  "))
print()
print()
def BallFinder (): 
    global Ball
    Ballmin=0
    Ballmax=0
    while Ballmin==Ballmax:
        Roll()
        Ballmin=NumberRolled
        Roll()
        Ballmax=NumberRolled
    Ball=Net
    while Ball==Net:
        if Ballmin>Ballmax: 
            random_numbers = random.randint(Ballmax,Ballmin) 
            Ball=random_numbers
        elif Ballmax>Ballmin:
            random_numbers = random.randint(Ballmin,Ballmax) 
            Ball=random_numbers
    #this sets the ball within randomly selected boundreis (ballmax and ballmin) which are found through the Roll function
BallFinder() 
print(Ball)
print()
StartTime = time.time()#sets the start time for the timer to reference
CurrentTime=time.time()#this sets the current time
DURATION=10#makes it so the timer only the time only runs for 10 seconds
while CurrentTime < StartTime + DURATION: #this works as a timer
    CurrentTime=time.time()  #makes sure CurrentTime remains accurate
    Roll()
    if Ball>Net:# if the ball is bigger than the net it subtracts
        Subtracting()
        Repetions=Repetions+1       
    elif Ball<Net:#if the ball is smaller than the net it adds
        Adding()
        Repetions=Repetions+1 
    else:
        CurrentTime=time.time()+DURATION      #if the ball=net it imediatly ends  
print(f"It Looped {Repetions} Times") #tells the user how many times it looped
