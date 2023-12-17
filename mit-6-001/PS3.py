#!/usr/bin/env python
# coding: utf-8

# ## Problem Set 3
# 
# ### Introduction
# 
# Note: Do not be intimidated by this problem! It's actually easier than it looks. We will 'scaffold' this problem, guiding you through the creation of helper functions before you implement the actual game.
# 
# For this problem, you will implement a variation of the classic wordgame Hangman. For those of you who are unfamiliar with the rules, you may read all about it here. In this problem, the second player will always be the computer, who will be picking a word at random.
# 
# In this problem, you will implement a function, called hangman, that will start up and carry out an interactive Hangman game between a player and the computer. Before we get to this function, we'll first implement a few helper functions to get you going.
# 
# For this problem, you will need the code files ps3_hangman.py and words.txt. Right-click on each and hit "Save Link As". Be sure to save them in same directory. Open and run the file ps3_hangman.py without making any modifications to it, in order to ensure that everything is set up correctly. By "open and run" we mean do the following:
# 
#     Go to your IDE. From the File menu, choose "Open".
#     Find the file ps3_hangman.py and choose it.
#     The template ps3_hangman.py file should now be open. Run the file.
# 
# The code we have given you loads in a list of words from a file. If everything is working okay, after a small delay, you should see the following printed out:
# 
# 
# Loading word list from file...
# 55909 words loaded.
# 
# If you see an IOError instead (e.g., "No such file or directory"), you should change the value of the WORDLIST_FILENAME constant (defined near the top of the file) to the complete pathname for the file words.txt (This will vary based on where you saved the file). Windows users, change the backslashes to forward slashes, like below.
# 
# For example, if you saved ps3_hangman.py and words.txt in the directory "C:/Users/Ana/" change the line: 
# 
# WORDLIST_FILENAME = "words.txt"  to something like
# 
# WORDLIST_FILENAME = "C:/Users/Ana/words.txt"
# 
# This folder will vary depending on where you saved the files.
# 
# The file ps3_hangman.py has a number of already implemented functions you can use while writing up your solution. You can ignore the code between the following comments, though you should read and understand how to use each helper function by reading the docstrings:
# 
# 
# ```python 
# # -----------------------------------
# # Helper code
# # You don't need to understand this helper code,
# # but you will have to know how to use the functions
# # (so be sure to read the docstrings!)
#     .
#     .
#     .
# # (end of helper code)
# # -----------------------------------
# ```
#    
# 
# You will want to do all of your coding for this problem within this file as well because you will be writing a program that depends on each function you write.
# Requirements
# 
# Here are the requirements for your game:
# 
#     1. The computer must select a word at random from the list of available words that was provided in words.txt. The functions for loading the word list and selecting a random word have already been provided for you in ps3_hangman.py.
# 
#     2. The game must be interactive; the flow of the game should go as follows:
# 
#        - At the start of the game, let the user know how many letters the computer's word contains.
# 
#        - Ask the user to supply one guess (i.e. letter) per round.
# 
#        - The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.
# 
#        - After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.
#     3. Some additional rules of the game:
# 
#         - A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).
# 
#         - A user loses a guess **only** when s/he guesses incorrectly.
# 
#         - If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try again.
# 
#         - The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.
# 
# #### Sample Output
# 
# The output of a winning game should look like this...
# ```
# 
# 	Loading word list from file...
# 	55900 words loaded.
# 	Welcome to the game, Hangman!
# 	I am thinking of a word that is 4 letters long.
# 	-------------
# 	You have 8 guesses left.
# 	Available letters: abcdefghijklmnopqrstuvwxyz
# 	Please guess a letter: a
# 	Good guess: _ a_ _
# 	------------
# 	You have 8 guesses left.
# 	Available letters: bcdefghijklmnopqrstuvwxyz
# 	Please guess a letter: a
# 	Oops! You've already guessed that letter: _ a_ _
# 	------------
# 	You have 8 guesses left.
# 	Available letters: bcdefghijklmnopqrstuvwxyz
# 	Please guess a letter: s
# 	Oops! That letter is not in my word: _ a_ _
# 	------------
# 	You have 7 guesses left.
# 	Available letters: bcdefghijklmnopqrtuvwxyz
# 	Please guess a letter: t
# 	Good guess: ta_ t
# 	------------
# 	You have 7 guesses left.
# 	Available letters: bcdefghijklmnopqruvwxyz
# 	Please guess a letter: r
# 	Oops! That letter is not in my word: ta_ t
# 	------------
# 	You have 6 guesses left.
# 	Available letters: bcdefghijklmnopquvwxyz
# 	Please guess a letter: m
# 	Oops! That letter is not in my word: ta_ t
# 	------------
# 	You have 5 guesses left.
# 	Available letters: bcdefghijklnopquvwxyz
# 	Please guess a letter: c
# 	Good guess: tact
# 	------------
# 	Congratulations, you won!```
# 
#     
# 
# And the output of a losing game should look like this...
# ```
# 
# 	Loading word list from file...
# 	55900 words loaded.
# 	Welcome to the game Hangman!
# 	I am thinking of a word that is 4 letters long
# 	-----------
# 	You have 8 guesses left
# 	Available Letters: abcdefghijklmnopqrstuvwxyz
# 	Please guess a letter: a
# 	Oops! That letter is not in my word: _ _ _ _
# 	-----------
# 	You have 7 guesses left
# 	Available Letters: bcdefghijklmnopqrstuvwxyz
# 	Please guess a letter: b
# 	Oops! That letter is not in my word: _ _ _ _
# 	-----------
# 	You have 6 guesses left
# 	Available Letters: cdefghijklmnopqrstuvwxyz
# 	Please guess a letter: c
# 	Oops! That letter is not in my word: _ _ _ _
# 	-----------
# 	You have 5 guesses left
# 	Available Letters: defghijklmnopqrstuvwxyz
# 	Please guess a letter: d
# 	Oops! That letter is not in my word: _ _ _ _
# 	-----------
# 	You have 4 guesses left
# 	Available Letters: efghijklmnopqrstuvwxyz
# 	Please guess a letter: e
# 	Good guess: e_ _ e
# 	-----------
# 	You have 4 guesses left
# 	Available Letters: fghijklmnopqrstuvwxyz
# 	Please guess a letter: f
# 	Oops! That letter is not in my word: e_ _ e
# 	-----------
# 	You have 3 guesses left
# 	Available Letters: ghijklmnopqrstuvwxyz
# 	Please guess a letter: g
# 	Oops! That letter is not in my word: e_ _ e
# 	-----------
# 	You have 2 guesses left
# 	Available Letters: hijklmnopqrstuvwxyz
# 	Please guess a letter: h
# 	Oops! That letter is not in my word: e_ _ e
# 	-----------
# 	You have 1 guesses left
# 	Available Letters: ijklmnopqrstuvwxyz
# 	Please guess a letter: i
# 	Oops! That letter is not in my word: e_ _ e
# 	-----------
# 	Sorry, you ran out of guesses. The word was else. ```
#     

# In[1]:


import random
import string

WORDLIST_FILENAME = "words.txt" # hosted in same folder


# In[2]:


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


# ### Problem 1 - Is the Word Guessed
# 
# Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.
# 
# Example Usage:
# ```Python 
# secretWord = 'apple' 
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))
# False
# ```

# In[3]:


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    is_guessed = True

    for letter in secretWord:
        if letter not in lettersGuessed:
            is_guessed = False
            break

    return is_guessed
        


# ### Problem 2 - Getting the User's Guess
# 
# 
# Next, implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!
# 
# Example Usage:
# ```python
# secretWord = 'apple' 
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))
# '_ pp_ e'
# ```
# 
# When inserting underscores into your string, it's a good idea to add at least a space after each one, so it's clear to the user how many unguessed letters are left in the string (compare the readability of ____ with _ _ _ _ ). This is called usability - it's very important, when programming, to consider the usability of your program. If users find your program difficult to understand or operate, they won't use it!
# 
# For this problem, you are free to use spacing in any way you wish - our grader will only check that the letters and underscores are in the proper order; it will not look at spacing. We do encourage you to think about usability when designing.
# 
# For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

# In[4]:


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    guessed_str_list = ['_' for x in range(len(secretWord))] 

    for i, letter in enumerate(list(secretWord)):
        if letter in lettersGuessed:
            guessed_str_list[i] = letter
    

    return ''.join(guessed_str_list)
        


# ### Problem 3 - Printing Out all Available Letters
# 
# 
# Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in lettersGuessed.
# 
# Example Usage:
# ```python
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print(getAvailableLetters(lettersGuessed))
# abcdfghjlmnoqtuvwxyz
# ```
# Note that this function should return the letters in alphabetical order, as in the example above.
# 
# For this function, you may assume that all the letters in lettersGuessed are lowercase.
# 
# Hint: You might consider using string.ascii_lowercase, which is a string comprised of all lowercase letters:
# ```python
# import string
# print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
# ```

# In[5]:


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = list(string.ascii_lowercase)

    for letter in lettersGuessed:
        try:
            available.remove(letter)
        except ValueError:
            pass
        
    return ''.join(available)


# ### Problem 4 - The Game
# 
# Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

# In[6]:


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print('Welcome to the game of Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-' * 13)

    guesses_left = 8

    lettersGuessed = []

    while guesses_left != 0:
       print('You have', guesses_left, 'guesses left.')
       #available letters 
       gAL = getAvailableLetters(lettersGuessed)
       
       # letter guesses
       print('Available letters:', gAL)
       guess = input('Please guess a letter:')
              # results
       if guess in lettersGuessed:
           print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
           print('-'*13)
           continue
       else:
          lettersGuessed.append(guess)
       
       if guess in secretWord:
           print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
       else:
           print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
           guesses_left -= 1

       print('-'*13)
           

       x = isWordGuessed(secretWord, lettersGuessed)
       
       if x:
           print('Congratulations, you won!')
           break

       

    if not x and guesses_left == 0:
      print('Sorry, you ran out of guesses. The word was', secretWord + '.')


# In[7]:


hangman(random.choice(wordlist))


# In[8]:


get_ipython().system('jupyter nbconvert PS3.ipynb --to python')

