## Requirements
python

## Description
CLI based hangman game, which randomly selects a word and we are asked to fill the letters.

User starts with 6 guesses, every wrong guess results in deduction of guess. Right guess doesn't result in decrease of guesses.

You can ask for hint using '*'.

### Good luck!!

## Example Usage:
```
python hangman.py

Loading word list from file...
55900 words loaded.
Welcome to the game Hangman!
I am thinking of a word that is 5 letters long.
--------
You have 6 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Good guess: a_ _ _ _
--------
You have 6 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: l
Good guess: a_ _ l_
--------
You have 6 guesses left.
Available letters: bcdefghijkmnopqrstuvwxyz
Please guess a letter: *
Possible word matches are:
addle adult agile aisle amble ample amply amyls angle ankle apple
apply aptly arils atilt
```