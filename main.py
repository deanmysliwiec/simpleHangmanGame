# Hangman Game by Dean Mysliwiec

import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Word bank of animals
words = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar',
         'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat',
         'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt',
         'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven',
         'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider',
         'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf',
         'wombat', 'zebra']

# highest it can go is 6 : print(HANGMANPICS[6])

comp_choice = random.choice(words)
words.remove(comp_choice)
# print(comp_choice)
end = False
correct = False
won = False
lives = 0
display = []
blanks = len(comp_choice)
for _ in range(blanks):
    display += "_"

print(f"Word length: {' '.join(display)}")

while not end:
    while not won and lives != 6:

        user_choice = input("What is your letter choice? ").lower()
        if user_choice in display:
            print("\nYou already guessed that! But good try! \n")
        for position in range(blanks):
            letter = comp_choice[position]
            if letter == user_choice:
                correct = True
                display[position] = letter


        if correct == True:
            print(f"You guessed right!\n {' '.join(display)} \n {HANGMANPICS[lives]}")
        else:
            lives += 1
            print(f"Incorrect!\n {' '.join(display)} \n {HANGMANPICS[lives]}")
        if "_" not in display:
            won = True
        correct = False
        if won == True:
            print("You won!!!")
        elif lives == 6:
            print(f"You lost!!! The word was {comp_choice}")

    choice = input("Would you like to play again? (Y/N): ").lower()
    if choice == "y":
        lives = 0
        won = False
        display = []
        comp_choice = random.choice(words)
        words.remove(comp_choice)
        blanks = len(comp_choice)
        for _ in range(blanks):
            display += "_"
        print(f"Word length: {' '.join(display)}\n")
    elif choice == "n":
        print("\nThanks for playing! Good bye!")
        break
    else:
        print("\nPlease enter a correct choice!\n")