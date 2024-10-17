import random

#"random number selection"
#def Roll():
    #global waw
    #global numberlist
  # global Maximum
 #   global Minumum
# import random

def Roll():
    global Maximum
    global Minumum
    global waw
    import random
    waw=random.randint(Minumum, Maximum)
   
    #random_numbers = {random.randint(Minumum,Maximum) for _ in range(1)}  
    #numberlist = list(random_numbers)
    #waw=numberlist[0]

Turns=0

#Math PONG

def Subtracting():
    global Center
    global Ball
    global Turns
    while Ball>Center:
        Roll()
        print("subtracting")
        Ball=Ball-waw
        Turns=Turns+1
    print(Ball)
   

def Adding():
    global Center
    global Ball
    global Turns
    while Ball<Center:
        Roll()
        print("adding")
        Ball=Ball+waw
        Turns=Turns+1
    print(Ball)

def notSubtracting():
    global Center
    global Ball
    global Turns
    while Ball>Center:
        Roll()
        print("Adding")
        Ball=Ball+waw
        Turns=Turns+1
    print(Ball)

def notAdding():
    global Center
    global Ball
    global Turns
    while Ball<Center:
        Roll()
        print("Subtracting")
        Ball=Ball-waw
        Turns=Turns+1
    print(Ball)


print()
Maximum=int(input("What is the maximum change you wish applied    "))


Minumum=int(input("What is the minumum change you wish applied   "))
if Minumum>Maximum:
     while Minumum>Maximum:
          print("The Minumum can not be more than the Maximum   ")
          Minumum=int(input("What is the minumum change you wish applied"))
elif Maximum-Minumum<1:
    print("You Need To Create A Bigger Diferrfence Or Else This Will Go On Forever")
    Minumum=int(input("What is the minumum change you wish aplied    "))
else:
     print()
          
Center=int(input("What Number Do You Wish The Center To Be  "))
     
 
         

Guess=int(input("How Times Do You Think It Will Loop  - "))
while Guess<0:
    print("Please Input 0 Or Greater")
    Guess=int(input("How Times Do You Think It Will Loop   "))


def Run():
    global Ball
    global numberlist
    random_numbers = {random.randint(-100,100) for _ in range(1)}  
    numberlist = list(random_numbers)
    Ball=numberlist[0]
 

#DDFFFFF
Roll()
Run()
if Ball==Center:
    Ball=Ball+waw
    print(Ball)
else:
    print(Ball)



if Maximum<1:
     if Ball>Center:
        while Ball!=Center:
            notSubtracting()
            notAdding()
          
                 
     elif Ball<Center:
            while Center!=Ball:
                notAdding()
                notSubtracting()
            
                
               

     else:
         print("Eror 404 Number Not Found")
     
elif Maximum>=1:
     if Ball>=Center:
        while Ball!=Center:
            Subtracting()
            Adding()
           

     elif Ball<Center:
        while Ball!=Center:
            Adding()
            Subtracting()
          

     else:
          
        print("Eror 404 Number Not Found")

else:
     print("eror 405")


if Guess==Turns:
    print("You Win")
else:
    print("You Lose")
    print(f"It Looped {Turns} Times")