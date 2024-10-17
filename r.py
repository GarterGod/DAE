
"input name and age and height in feet"


age=2

name="John Doe"

height=6.5



AGE=age

TimeUntilAdult=21
print(f"{name} you are {AGE}")

if age>21:
       age=age-21
       if age<1.0001:
              print("you were 21 last year.")
       else:
              print(f"You were 21 {age} years ago.")   
elif age<21:
       TimeUntilAdult=TimeUntilAdult-age
       if TimeUntilAdult<1.001:
              print("You will be 21 next year.")
       else:
               print(f"You will be 21 in {TimeUntilAdult} years.")   
else:
       print(f"{name} You are 21.")


age=AGE
TimeUntilAdult=30

if age>30:
       age=age-30
       if age<1.0001:
              print("you were 30 last year.")
       else:
              print(f"{name} you are {AGE} and you were 30 {age} years ago.")   
elif age<30:
       TimeUntilAdult=TimeUntilAdult-age
       if TimeUntilAdult<1.001:
              print("you will be 30 next year.")
       else:
               print(f"You will be 30 in {TimeUntilAdult} years.")   
else:
       print(f"{name} You are 30.")


age=AGE
TimeUntilAdult=50

if age>50:
       age=age-50
       if age<1.0001:
              print("You were 50 last year.")
       else:
              print(f"You were 50 {age} years ago.")   
elif age<50:
       TimeUntilAdult=TimeUntilAdult-age
       if TimeUntilAdult<1.001:
              print("You will be 50 next year.")
       else:
               print(f"You will be 50 in {TimeUntilAdult} years.")   
else:
       print(f"{name} You are 50.")


age=AGE
TimeUntilAdult=100

if age>100:
       age=age-100
       if age<1.0001:
              print("You were 100 last year.")
       else:
              print(f"You were 100 {age} years ago.")   
elif age<100:
       TimeUntilAdult=TimeUntilAdult-age
       if TimeUntilAdult<1.001:
              print("You will be 100 next year.")
       else:
               print(f"You will be 100 in {TimeUntilAdult} years.")   
else:
       print(f"{name} You are 100.") 



print(f"your currently about {height} feet tall")
