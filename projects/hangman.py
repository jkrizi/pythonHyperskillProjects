import random

dictionary = ['python', 'java', 'kotlin', 'javascript']


def menu():
    print('H A N G M A N')
    while True:
        command = input('Type "play" to play the game, "exit" to quit: ')
        if command == 'play':
            run_game()
        else: 
            break


def run_game():
    random_word = random.choice(dictionary)
    guessed_word = '-' * len(random_word)
    hidden_letters = set(random_word)
    guessed_letters = set()
    lives = 8

    while lives > 0 and random_word != guessed_word:
        print()
        print(guessed_word)
        guess = input('Input a letter: ')
        if len(guess) > 1:
            print('You should print a single letter')
        elif not guess.islower() or not guess.isascii():
            print('It is not an ASCII lowercase letter')
        elif guess in guessed_letters:
            print('You already typed this letter')
        elif guess in hidden_letters:
            hidden_letters.discard(guess)
            guessed_letters.add(guess)
            guessed_word = ''
            for letter in random_word:
                if letter in guessed_letters:
                    guessed_word = guessed_word + letter
                else:
                    guessed_word = guessed_word + '-'
        else:
            print('No such letter in the word')
            guessed_letters.add(guess)
            lives -= 1

    if random_word == guessed_word:
        print('You guessed the word!')
        print('You survived!')
    else:
        print('You are hanged!')


menu()
