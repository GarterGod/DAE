def conversion():
    global Userinput
    Userinput=int(Userinput)


    

print("you are an adventurer walking down a wide woodland path when you suddenly come to a fork you can either go left to the pond or right to the clearing")
Userinput=input("1 for left or 2 for right   ")
conversion()
while Userinput<1 or Userinput>3:
    Userinput=input("please  select 1 for left or 2 for right   ")
conversion()

if Userinput==1:
    print("you turn left bringing you to the pond you and your grandfather used to fish at when you were but a child you see the shed were you he used to keep the fishing eqipment would you like to go see if it is unlocked")
    Userinput=input


elif Userinput==2:
    print("you turn right into the clearing a large open space inviting you to wonder around would you like to wander around")
    Userinput=input("select 1 for yes or 2 for no   ")
conversion()
while  Userinput<1 or Userinput>3:
    print("please select 1 for yes 2 for no")
    conversion


else:
    print("you head straight into the woods looking for adventure and excitment while seeing all the beauty of nature and as your exploring the woods you encounter a snake would you like to fight or flee")
    Userinput=input("1 to fight the snake 2 to run from it    ")
    conversion()
    while Userinput<1 or Userinput>3:
        Userinput=input("please select 1 for fight or 2 for flee   ")
        conversion()
    if Userinput==1:
        print("you jump foward and grab it. it hisses loudly and bites at you as you rip it in half blood spilling to the ground and over you like a water balloon with a hole in it  ")
        print("then you realise it is a garter snake completley harmless  +30xp")
    elif Userinput==2:
        print("you run away from the snake back to the fork")
        print("behind you, you here twigs snapping as something to big to be a snake rapidly aproaches your location")
        print("you can go left, right or straight")
        
        Userinput=input("1 for straight 2 for left 3 for right")
        conversion()



