hangman0 = '''
  +---+
  |   |
      |
      |
      |
      |
========='''

hangman1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
hangman2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
hangman3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
hangman4 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
hangman5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
hangman6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
player1_name=input("what is ur name")
player2_name=input("what is ur name")
full_answer=input("whats ur word")
wrong_letters=""
correct_letters=""
lives=5
won = False
while lives != -1 and won == False:
    won=True
    for i in full_answer:
        if i in correct_letters:
            print(i,end="")
        else:
            print("_",end="")
    if lives == 5:
        print(hangman0)
    elif lives == 4:
        print(hangman1)
    elif lives == 3:
        print(hangman2)
    elif lives == 2:
        print(hangman3)
    elif lives == 1:
        print(hangman4)
    elif lives == 0:
        print(hangman5)
    guessed_letter =input("enter a letter")
    if guessed_letter in correct_letters or guessed_letter in wrong_letters:
        print("u already tried that letter")
    if guessed_letter in full_answer:
        correct_letters =correct_letters + guessed_letter
    elif guessed_letter not in full_answer:
        wrong_letters =wrong_letters+guessed_letter
        lives = lives-1
    for j in full_answer:
        if j not in correct_letters:
            won = False
            break

    
if won == True:
    print("Congratulations", player1_name,"you have won!")
    print("Nice try", player2_name)
elif won == False:
    print(hangman6)
    print("Congratulations", player2_name,"you have won!")
    print("Nice try", player1_name)
