import random
import time
#"random number selection"
#def Roll():
    #global waw
    #global numberlist
  # global Maximum
 #   global Minumum
# import random

#def Roll():
    #global numberlist
    #random_numbers = {random.randint(Minumum,Maximum) for _ in range(1)}  
   # waw =random_numbers[0]


def Roll():
    global Maximum
    global Minumum
    global waw
    import random
    random_number=random.randint(Minumum, Maximum) 
    waw = random_number
   
    #random_numbers = {random.randint(Minumum,Maximum) for _ in range(1)}  
    #numberlist = list(random_numbers)
    #waw=numberlist[0]

Turns=0

#Math PONG

def Subtracting():
    global Net
    global Ball
    global Turns
    global waw
    if waw<0:
        Ball=Ball-waw
        waw=waw*-1
        print(f"Adding {waw}")
    else:
        print(f"Subtracting {waw}")
        Ball=Ball-waw
    Turns=Turns+1
    print(Ball)
    print()
    
   

def Adding():
    global Net
    global Ball
    global Turns
    global waw
    Roll()
    if waw<0:
        Ball=Ball+waw
        waw=waw*-1
        print(f"Subtracting {waw}")
    else:
        print(f"Adding {waw}")
        Ball=Ball+waw


        Turns=Turns+1
        print(Ball)
        print()



print()
Maximum=int(input("Maximum   "))


Minumum=int(input("Minumum   "))
if Minumum>Maximum:
     while Minumum>Maximum:
          print("The Minumum can not be more than the Maximum   ")
          Minumum=int(input("What is the minumum change you wish applied"))
elif Maximum-Minumum<1:
    print("You Need To Create A Bigger Diferrfence Or Else This Will Go On Forever")
    Minumum=int(input("What is the minumum change you wish aplied    "))
else:
     print()
          
Net=int(input("What Number Do You Wish The Net To Be  "))
     
 
         




def BallFinder (): 

    Ballmin=0
    Ballmax=0
    while Ballmin==Ballmax:
        global Ball
        Roll()
        Ballmin=waw
        Roll()
        Ballmax=waw
    if Ballmin>Ballmax: 
        random_numbers = random.randint(Ballmax,Ballmin) 
        Ball=random_numbers
    elif Ballmax>Ballmin:
        random_numbers = random.randint(Ballmin,Ballmax) 
        Ball=random_numbers

BallFinder() 

#DDFFFFF
Roll()

if Ball==Net:
    Ball=Ball+waw
    print(Ball)
else:
    print(Ball)

start_time = time.time()
trutime=time.time()
duration=10
while trutime < start_time + duration: 
    trutime=time.time()  
    Turns=Turns+1 
    if Ball>Net:
        Subtracting()
           
    elif Ball<Net:
        Adding()
    else:
        trutime=time.time()+duration
        
print(f"It Looped {Turns} Times")

          

