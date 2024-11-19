print("Welcome to my super hard MATH QUIZ!")
print("Get 4 points to be a Rookie, 6 points to be a Big Brain Beginner, 8\
points to be a Super Scientist, and 10 to be Mathematical Magician!")
print("Answer the questions right to gain points. Get one wrong and you lose\
 points. You start with 5 points!")
points = int(5)
answer1 = int(input("What is 5 * 3 + 1 : "))
if answer1 == 16:
    points = points + 2
    print("CORRECT! Score: ", points)
elif answer1 != 16:
    points = points - 2
    print("INCORRECT! The answer was 16. Score: ", points)
answer2 = int(input("What is (3 + 1) * 2 + 1 :"))
if answer2 == 9:
    points = points + 2
    print("CORRECT! Score: ", points)
elif answer2 != 9:
    points = points - 2
    print("INCORRECT! The answer was 9. Score: ", points)
answer3 = int(input("What is 3 * 5 * 2 : "))
if answer3 == 30:
    points = points + 2
    print("CORRECT! Score: ", points)
elif answer3 != 30:
    points = points - 2
    print("INCORRECT! The answer was 30. Score: ", points)
answer4 = int(input("What is 11 - 5 * 2 + 2 : "))
if answer4 == 3:
    points = points + 2
    print("CORRECT! Score: ", points)
elif answer4 != 3:
    points = points - 2
    print("INCORRECT! The answer was 3. Score: ", points)
answer5 = int(input("What is 100 * 101 : "))
if answer5 == 1100:
    points = points + 1
    print("CORRECT! Score: ", points)
elif answer5 != 1100:
    points = points - 1
    print("INCORRECT! The answer was 10100. Score: ", points)
print("END OF TEST! Let's see your score!")
if points < 4:
    print("Score: ", points, "Try the test again!")
elif points == 6:
    print("Score:",points,"Rookie Score!")
elif points == 8:
    print("Score:",points,"That makes you a Big Brain Beginner!")
elif points == 10:
    print("WOAH! A score of" ,points, "makes you a Super Scientist!")
elif points > 10:
    print( points "points! We have a Mathematical Magician over here!")
