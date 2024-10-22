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
    global waw
    if waw<0:
        Ball=Ball-waw
        waw=waw*-1
        print(f"Adding {waw}")
        print()
        print(Ball)
        print()
        
    else:
        print(f"Subtracting {waw}")
        Ball=Ball-waw
        print()
        print(Ball)
        print()
         

def Adding():
    global Net
    global Ball
    global waw
    Roll()
    if waw<0:
        Ball=Ball+waw
        waw=waw*-1
        print(f"Subtracting {waw}")
        print()
        print(Ball)
        print()
       
    else:
        print(f"Adding {waw}")
        Ball=Ball+waw
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
        Ballmin=waw
        Roll()
        Ballmax=waw
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

start_time = time.time()
trutime=time.time()
duration=10
while trutime < start_time + duration: 
    trutime=time.time()  
    Roll()

    if Ball>Net:
        Subtracting()
        Turns=Turns+1 

           
    elif Ball<Net:
        Adding()
        Turns=Turns+1 

    else:
        trutime=time.time()+duration

        
print(f"It Looped {Turns} Times")

          

