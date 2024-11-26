
##name = input("What is your name?")
##letter = input("What is your favourite letter?")
##letter_count = 0
##vowel_count = 0
##for char in name:
##    if char == letter:
##        # this is short for letter_count = letter_count + 1
##        letter_count += 1
##    if char in "aeiouAEIOU":
##        vowel_count += 1
##print("You have", letter_count,\
##"instances of your favourite letter", letter,"in your name!")
##print("You have", vowel_count, "vowels in your name.")
##print("The total length of your name is", len(name))

##age = 0
##while age < 100: # we will only leave the loop when age >= 100
##    age += 1
##print(age) # this goes AFTER the loop finishes. What is printed?
### we can tell how many times it will repeat (100) by looking
##num = 0
##while num != 2:
##    num += 2
### this loop will only run once!
##number_hippos = 1
##more_hippos = "yes"
##while more_hippos == "yes":
##    number_hippos += 1
##    print("You have", number_hippos, "hippos!")
##    more_hippos = input("Do you want another hippo?")
### how many times will this loop repeat? It depends on the user!
### it will add another hippo anytime they answer "yes"
### it will stop as soon as they answer anything other than "yes"
##name = "Rumplestiltskin"
##guess = "John"
##while guess != name: # stuck in this loop you guess correctly
##    print("I challenge you to guess my name!")
##    guess = input("Enter your guess: ")
##print("Wow! You got it!")
### The only way this print is reached is if you get it right!
### if you always guess wrong, this loop could go forever

##game_completed = True
##while not game_completed: # this is a proper boolean condition
##    print("Keep playing!")

##dollars = 35
##while dollars < 20:
##    print("Insufficient funds.")

##x = 100
##while x != 300:
##    x = x - 5
##guess = "x"
##secret_letter = "b"
##while guess != secret_letter:
##    print("Wrong letter! Guess again!") # read carefully!

##cheer = "yes"
##while cheer == "yes":
##    for i in range(3): # we can put loops inside other loops
##        print("Hip hip hooray!")
##    cheer = input("Would you like us to cheer for you again?")

##for i in range(20): # it seems it will repeat 20 times
##    print(i)
##    if i == 10: # but once i is 10, we break out of the loop
##        break

##name = "Rumplestiltskin"
##guess = "wrong guess"
##while guess != name:
##    guess = input("Enter a guess for my name: ")
##    if guess == "I give up!":
##        break

##print(999999999999999999999999999%4832948395)

##i = int(input("Enter a number"))
##if i % 5 == 0:
##    print("your number is divisible by 5")
##else:
##    print("your number is not divisible by 5")


##a = 0
##while a == 0:
##    print("hi")

##a = 0
##while a != 0:
##    print("hi")

##word = "why"
##guess = input("guess the word")
##while guess != word:
##    while guess == "i dont know": 
##    guess = input("guess the word")

##i = int(input("enter a number"))
##while i % 2 != 0:
##    i = int(input("enter a number"))

##for i in range(2,8):
##    i +=1
##    print(i)

##i = 2
##while i != 8:
##    i +=1
##    print(i)

##the first one is better because it requires less code

##guess = int(input("Guess the number of marbles in the jar: "))
##number_of_marbles = 249
##while guess != number_of_marbles:
##    print("Incorrect guess! Try again!")
##    guess = int(input("Guess the number of marbles in the jar: "))

import random
lst=["rock","paper","scissors"]
p1=random.choice(lst)
p2=random.choice(lst)
print("player 1 chose",p1)
print("player 2 chose",p2)
i = input("do you want to keep playing")
while i == "yes":
    if p1 == "rock" p2 == "scissors":
        print("player 1 won")
    lst=["rock","paper","scissors"]
    p1=random.choice(lst)
    p2=random.choice(lst)
    print("player 1 chose",p1)
    print("player 2 chose",p2)
    i = input("do you want to keep playing")
