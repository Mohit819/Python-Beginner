##for i in range (1,12):
##    print("-------------------------------------------------------------------------------------------------------------------------------")
##    if i != 11:
##        for j in range(1,12):
##            print("|",end="\t")
##            if j != 11:
##                print(i*j,end="")
##        print()

i = input("do you want a triangle")
w = 1


while i == "y":
    for j in range(1,w+1):
        print("*"* j)
    w +=1
    i = input("do you want a triangle")
