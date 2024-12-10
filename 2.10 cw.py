##i = 10
##while i > 2:
##    print(i)
##    i = i - 3
### what does the code above print?
##for i in range(10,2,-3):
##    print(i)
### what does the code above print?

##print("Any string you like", end="") # end string with nothing!
##print("Any string you like", end="\t") # end string with \t

##print("Hello", end="")
##print("World!", end="")
##for i in range(10):
##    print(i, end="\t")
##for i in range(5):
##    print(i, end="0\n")

##user_name = "Gurleen"
##user_age = 13
##name = "Kyle"
##print("%s is your name, and %s is mine."%(user_name,name))
##print("Username:%s, age:%d years old."%(user_name, user_age))

##for counter in range(1,11):
##    print(counter)
##    for i in range(3):
### actions here will happen 3 times
##        for i in range(3):
##            for counter in range(1,11):
##                print(counter)

##for i in range(10): # 10 rows
##    for j in range(5): # 5 columns
##        print("*", end="\t")
##    print() # this will JUST print a newline character
##for x in range(8): # 8 rows
##    for char in "abcd": # 4 columns
##        print(char, end=" ")
##    print("----")
### Can you print out 6 rows of "3 3 3 3" using thze method above?
##for a in range(1,6):
##    for b in range(a): # using the iterator variable here!
##        print("#", end="") # no extra characters added
##    print()
### what shape does the code above print out?
### Let’s print a multiplication table
##for i in range(5):
##    for j in range(5):
##        print(i * j, end="\t")
##    print()

##a = "more stars"
##while a == "more stars":
##    for i in range(1,5):
##        for w in range(i):
##            print("*",end="")
##        print()
##    a = input("type more stars for more stars")

##name=input("what is your name")
##for w in range(3):
##    for z in range(5):
##        print(name,end=" ")
##    print()

##for i in range(1,11):
##    for j in range(1,11):
##        print(i*j,end="\t")
##    print()
##    print()

for i in range (4):
    print("------------------------------------")
    if i != 3:
        for j in range(4):
            print("|",end="")
            if j != 3:
                print("\t",end=" ")
        print()
