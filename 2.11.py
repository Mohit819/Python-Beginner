##for i in range (100):
##    i +=1
##    if i % 3 == 0 and i % 5 == 0:
##        print("fizzbuzz")
##    elif i % 3 == 0:
##        print("fizz")
##    elif i % 5 == 0:
##        print("buzz")
##    else:
##        print(i)

##for w in range(5):
##    for i in range (10):
##        for j in range(i):
##            print(" "*j,end="")
##        print("*")
##    for i in range (10,0,-1):
##        for j in range(i):
##            print(" "*j,end="")
##        print("*")

##i = float(input("enter cash"))
##cash = i
##toonie = 2
##loonie = 1
##quarter = 0.25
##dime = 0.10
##nickel = 0.05
##numtoonies = 0
##numloonies = 0
##numquarters  = 0
##numdimes = 0
##numnickels = 0
##while cash > 0:
##    while cash > 1.99:
##        if cash > 1.99:
##            numtoonies +=1
##            cash = cash - numtoonies * toonie
##    while cash > 0.99:
##        if cash > 0.99:
##            numloonies +=1
##            cash = cash - numloonies*loonie
##    while cash > 0.24:
##        if cash > 0.24:
##            numquarters +=1
##            cash = cash - numquarters*quarter
##    while cash > 0.09:
##        if cash > 0.09:
##            numdimes +=1
##            cash = cash - numdimes*dime
##    while cash > 0.04:
##        if cash > 0.04:
##            numnickels +=1
##            cash = cash - numnickels*nickel
##print("the least amount of change results in ",numtoonies, "toonies ",numloonies, "loonies ",numquarters, "quarters "\
##          ,numdimes, "dimes ",numnickels, "nickels")

cash = int(input("How much cash do you have?"))
toonies = cash // 2
cash = cash - 2 * toonies
loonies = cash //1
cash = cash - 1 * loonies
quarters = cash // 0.25
cash = cash - 0.25 * quarters
dimes = cash // 0.10
cash = cash - 0.10 * dimes
nickels = cash // 0.05
cash = cash - 0.05 * nickels
print("the least amount of change is ",toonies,"toonies ",loonies,"loonies ",quarters,"quarters ",dimes,"dimes and ",nickels,"nickels.")
