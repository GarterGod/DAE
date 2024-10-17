

"input the length, height, and or hypotenuse of your right triangle and set the one you do not know to 0"
length=3
height=0
hypotenuse=5

print()


import math
length=length*length
height=height*height
hyponuse=hypotenuse*hypotenuse

if length==0:
    length=hypotenuse-height
    length=math.sqrt(length)
    print (f"The length is {length} unit(s).")

elif height==0:
    height=hypotenuse-length
    height=math.sqrt(height)
    print(f"The height is {height} unit(s).")
else:
    hypotenuse=length+height
    hypotenuse=math.sqrt(hypotenuse)
    print(f"The hypotenuse is {hypotenuse} unit(s).")

    print()