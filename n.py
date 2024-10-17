import random
def Roll():
    global waw
    global numberlist
   
    random_numbers = {random.randint(1,10) for _ in range(1)}  
    numberlist = list(random_numbers)
    waw=numberlist[0]
Roll()
print(waw)