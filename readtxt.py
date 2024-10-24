def read():
    filetoreadfrom=open("notouch.txt","r")
    line=filetoreadfrom.readline().rstrip("\n")
    while line !="":
        print(line)
        line=filetoreadfrom.readline().rstrip("\n")
def clear():
    filetowriteto=open("notouch.txt", "w")
    filetowriteto.write("")
    print("Cleared")
def write():
    filetowriteto=open("notouch.txt", "a")

    filetowriteto.write(input("input: "))
    filetowriteto.write("\n")

