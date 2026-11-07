import random

with open('words.txt') as f:
    words = f.read().splitlines()

hangmanword = random.choice(words) #randomly choosing the word from words.txt
lives = 8
guesses = []
to_print = ""
is_puzzle_solved = False

def consume_life(lives): #Function to make the player lose lives when they guess wrong
    lives -= 1
    print('Incorrect guess, you lost a life')
    print('Lives left:', lives)
    return lives

print(hangmanword) #Word debug
while is_puzzle_solved == False and lives > 0: #checking to see if the program should be run
    guess = input('Enter a guess (Can be letters or words):').lower()
    guesses.append(guess) #Getting the guess and adding it to the list
    to_print = "" #Reseting the print to nothing

    if len(guess) != len(hangmanword) and len(guess) != 1:
        print('Error, this isnt a single letter or the correct word length.') #Checking if its the right length

    if guess == hangmanword:
            is_puzzle_solved = True #Checking if it's the exact word

    elif guess not in hangmanword:
        lives = consume_life(lives) #checking if the letter is in the word

    elif len(guess) == len(hangmanword) and guess != hangmanword:
        is_puzzle_solved = False
        to_print += "_"
        lives = consume_life(lives) #Checking if it is the right length but the wrong word
        
    else:
        is_puzzle_solved = True
        for letter in hangmanword:
            if letter in guesses:
                to_print += letter
            else:
                to_print += "_"
                is_puzzle_solved = False
        print(to_print) #Writing out the letters the user has gotten so far

if lives == 0:
    print('Game over! You ran out of lives') #Game over message

if is_puzzle_solved == True:
    print('Well done! You completed the hangman with', lives, 'lives left. The word was:', hangmanword) #Winning message
