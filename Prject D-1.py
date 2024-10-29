import random
import time
#"random number selection"
#def Roll():
    #global NumberRolled
    #global numberlist
  # global Maximum
 #   global Minumum
# import random

#def Roll():
    #global numberlist
    #random_numbers = {random.randint(Minumum,Maximum) for _ in range(1)}  
   # NumberRolled =random_numbers[0]


def Roll():
    global Maximum
    global Minumum
    global NumberRolled
    import random
    random_number=random.randint(Minumum, Maximum) 
    NumberRolled = random_number
   
    #random_numbers = {random.randint(Minumum,Maximum) for _ in range(1)}  
    #numberlist = list(random_numbers)
    #NumberRolled=numberlist[0]

Repetions=0

#Math PONG

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
    Maximum=int(input("Maximum   "))
    print()
    Minumum=int(input("Minumum   "))
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
    
    

BallFinder() 



print(Ball)
print()

StartTime = time.time()
CurrentTime=time.time()
DURATION=10
while CurrentTime < StartTime + DURATION: 
    CurrentTime=time.time()  
    Roll()

    if Ball>Net:
        Subtracting()
        Repetions=Repetions+1 

           
    elif Ball<Net:
        Adding()
        Repetions=Repetions+1 

    else:
        CurrentTime=time.time()+DURATION

        
print(f"It Looped {Repetions} Times")
