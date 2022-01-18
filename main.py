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

# choose random word
comp_choice = random.choice(words)
# remove it from word bank after it is used
words.remove(comp_choice)
# For debugging: print(comp_choice)
end = False
correct = False
won = False
# reverse lives, if it hits 6, you lose
lives = 0
# holds the blanks and letters guessed if guessed right
display = []
# get length of word for blanks
blanks = len(comp_choice)
# add blanks to display, each representing "_"
for _ in range(blanks):
    display += "_"
# print word length for user
print(f"Word length: {' '.join(display)}")

# continuous until encounters break, could also use "end" variable present
while not end:
    while not won and lives != 6:
        # takes user input
        user_choice = input("What is your letter choice? ").lower()
        # if already guessed letter
        if user_choice in display:
            print("\nYou already guessed that! But good try! \n")
        # check for letters in word and add them to display if applicable
        for position in range(blanks):
            letter = comp_choice[position]
            if letter == user_choice:
                correct = True
                display[position] = letter

        # if user guessed correctly on last guess
        if correct == True:
            print(f"You guessed right!\n {' '.join(display)} \n {HANGMANPICS[lives]}")
        else:
            # if not guessed correctly, will (add) a life and add to hangman art
            lives += 1
            print(f"Incorrect!\n {' '.join(display)} \n {HANGMANPICS[lives]}")
        # if no more blanks left, win game
        if "_" not in display:
            won = True
        # correct set back to false for next guess
        correct = False
        # if user has won
        if won == True:
            print("You won!!!")
        # if not won, lives must be 6, otherwise it will continue through the loop again for another user guess
        elif lives == 6:
            print(f"You lost!!! The word was {comp_choice}")
    # ask to play again
    choice = input("Would you like to play again? (Y/N): ").lower()
    if choice == "y":
        # reset all variable data in order to fully reset game, still removing words from word bank
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
