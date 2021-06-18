# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDlist_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the secret_word list, this function may
    take a while to finish.
    """
    print("Loading secret_word list from file...")
    # inFile: file
    inFile = open(WORDlist_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a secret_word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
# secretword = choose_word(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the secret_word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for stuff in letters_guessed:
      if stuff not in secret_word:
        # continue
        return False
      # else:
        
    return True
      
    # return True
# print(is_word_guessed('hello', []))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the secret_word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    returnstring = ''
    for stuff in secret_word:
      if stuff in letters_guessed:
        returnstring += stuff
      else:
        returnstring += '_ '
    return returnstring
# secretword = 'apple'
# lettersguessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secretword, lettersguessed))



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    lowerletters = string.ascii_lowercase
    for letter in lowerletters:
      if letter in letters_guessed:
        lowerletters = lowerletters.replace(letter, '')
    return lowerletters
# print(get_available_letters(lettersguessed))
# secret_word = choose_word(load_words())
def hangman(secret_word):
    '''
    secret_word: string, the secret secret_word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's secret_word.

    * After each guess, you should display to the user the 
      partially guessed secret_word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warning = 3
    guesstimes = 6
    guesslist = []
    
    print('Welcome to the game hangman!!')
    print('I am thinking of a secret_word that is', len(secret_word), "letters long.")
    print('You have', warning, 'warnings left.')
    while guesstimes > 0:
      print('-'*20)
      print('You have', guesstimes, 'guesses left')
      
      print("Available letters: ", get_available_letters(guesslist))
      guess = input('Please guess a letter: ')
      
      if str.isalpha(guess):
        guesslist.append(str.lower(guess))
      else:
        warning -= 1
        if warning <= 0:
          guesstimes -= 1
          continue
        print('Oops that not a valid letter. you have', warning,'warnings left!')
        continue
      if guess in secret_word:
        print('Good guess:', get_guessed_word(secret_word, guesslist))
        if not is_word_guessed(secret_word, guesslist):
          print('Congrats you won the game')
        else:
          print('Sorry you ran out of guesses. Try again')
        continue
      else:
        print('Oops! That letter is not in my secret_word:',get_guessed_word(secret_word, guesslist))
        if guess in 'aeiou':
          guesstimes -= 2
        else:
          guesstimes -= 1
      if is_word_guessed(secret_word, guesslist):
        print('Congrats you won the game')
      else:
        print('Sorry you ran out of guesses. Try again')







# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret secret_word
    other_word: string, regular English secret_word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) == len(other_word):
      for i in range(len(my_word)):
        if my_word[i] == other_word[i]:
          continue
        if my_word[i] == '_' and other_word[i] not in my_word:
          continue
        else:
          return False
      return True
    else:
      return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret secret_word
    returns: nothing, but should print out every secret_word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret secret_word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the secret_word
            that has already been revealed.

    '''
    words = ""
    # count =0
    for word in wordlist:
        # if count % 5 == 0:
            # words += '\n'
        if match_with_gaps(my_word,word):
            words += word +" "
            # count += 1
        else:
            continue
    if words == '':
        return("No match found!")
    else:
        return (words)


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret secret_word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's secret_word.

    * After each guess, you should display to the user the 
      partially guessed secret_word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed secret_word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warning = 3
    guesstimes = 6
    guesslist = []
    
    print('Welcome to the game hangman!!')
    print('I am thinking of a secret_word that is', len(secret_word), "letters long.")
    print('You have', warning, 'warnings left.')
    while guesstimes > 0:
      if not guesstimes > 0:
        print('Oops you ran out of guesses')
        quit()
      print('-'*20)
      print('You have', guesstimes, 'guesses left')
      
      print("Available letters: ", get_available_letters(guesslist))
      guess = input('Please guess a letter: ')
      print(guess)
      if str.isalpha(guess):
        guesslist.append(str.lower(guess))
      elif guess == '*':
        print("Possible words are: ")
        print(show_possible_matches(get_guessed_word(secret_word, guesslist)))
        continue
      else:
        warning -= 1
        if warning <= 0:
          guesstimes -= 1
          continue
        print('Oops that not a valid letter. you have', warning,'warnings left!')
        continue
      if guess in secret_word:
        guess_so_far = get_guessed_word(secret_word, guesslist)
        print('Good guess:', guess_so_far)
        if is_word_guessed(secret_word, guess_so_far) == True:
          print('Congrats you won the game')
          quit()
        else:
          continue
        continue
      else:
        print('Oops! That letter is not in my secret_word:',get_guessed_word(secret_word, guesslist))
        if guess in 'aeiou':
          guesstimes -= 2
        else:
          guesstimes -= 1
      




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # print(secret_word)
    # hangman(secret_word)
    
# ###############
    
#     # To test part 3 re-comment out the above lines and 
#     # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    print(secret_word)
    hangman_with_hints(secret_word)
