##my_birth_year = 2000
##user_birth_year = int(input("What year were you born?"))
##print("If I print True, you are older than me!")
##print(my_birth_year > user_birth_year)
##
##my_favourite_word = "haberdashery"
##your_favourite_word = input("What is your favourite word?")
##print("If I print True, your word is longer!")
##print(len(your_favourite_word) > len(my_favourite_word))
##
##num1 = float(input("Enter a decimal number: "))
##num2 = float(input("Enter a decimal number: "))
##print("If I print True, both your numbers round to 4!")
##print(round(num1) == round(num2))

##if user_birth_year > 2000: # our first branch (pink)
##    print("I am older than you!")
##elif user_birth_year == 2000: # our second branch (blue)
##    print("We are the same age!")
##else:
##    print("You are older than me!") # the last branch (yellow)
##
##if len(my_favourite_word) > len(your_favourite_word):
##    print("My word is longer!")
##elif len(my_favourite_word) < len(your_favourite_word):
##    print("Your word is longer!")
##else:
##    print("Our words have the same length!")
##    print("They have", \
##len(my_favourite_word),"letters")

##user_pet = input("What kind of pet do you have?")
##if user_pet == "dog":
##    print("Me too!")
##elif user_pet == "cat":
##    print("I wish I could have a cat!")
##elif user_pet == "bird":
##    print("It would be so cool to have a bird.")
##elif user_pet == "hamster" or user_pet == "fish":
##    print("I used to have a pet like that.")
##elif user_pet == "I dont have a pet":
##    print("Thats sad")
##else: # this branch is for when the user didn’t answer
##    print("That's a unique pet!") # any of the above

##num = 3
##if num < 10:
##    print("That's a single digit number!")
##elif num == 16:
##    print("That's my favourite number,")
##elif num < 13:
##    print("My age is greater than that number.")
##elif num == 10:
##    print("There are 10 years in a decade.")
##elif num < 100:
##    print("That's a 2 digit number.")

##user_age = int(input("How old are you"))
##if user_age < 12:
##    print("You are very young")
##elif user_age < 20:
##    print("You are a teenager")
##elif user_age > 19:
##    print("You are an adult")
##elif user_age > 100:
##    print("You are an adult")

num = (81)
user_num = int(input("Guess the number"))
if user_num > num:
    print("Your guess is too high")
elif user_num == num:
    print("You got it")
elif user_num < num:
    print("Your guess is too low")
