import random
import math
def Roll():
    global numberlist
    random_numbers = {random.randint(1, 20) for _ in range(1)}  
    numberlist = list(random_numbers)
    print(f"roll {numberlist[0]}")

Roll()
"7704"
length=30
length=math.sqrt(length)

print(length)
Roll()