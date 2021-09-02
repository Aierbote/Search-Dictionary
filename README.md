# Search-Dictionary

This is exercize (new branch name) version 1.2
Feature: being able to read uppercase names like USA or NATO

This is the exercizeVers-1.1 :
Feature of matching words like Delhi or Paris.

Command Line Interface program to search a word in a data.json dictionary, made as an exercize during [The Python Mega Course](https://www.udemy.com/gift/the-python-mega-course/) by Ardit Sulce on Udemy.

This version is a bit messy, cause that's how I figured out the exercize.

## INSTRUCTIONS

Run `python3 searchdictionary.py` from same folder.

Enter any words you need to look for and answer Y or N when
comfirmation is required.

Query IS ***NOT* case sensitive** (because word are stored in lower and checked with all their possible CASE string methods). Version 1.2 features Title Case Words or Capitals (like Paris, Delhi, also New York) and UPPERCASE WORDS or simple ACRONYMS (like NATO and USA, without dots)

Comfirmation is not case sensitive.

Unless your word is Capitalized (as a city) or Title Case (New York).

To stop it any time enter `\end` (FIXED, it works ANYTIME 👋)\
Now even with `^C` (`Ctrl + C`) interruption, without raising an Exception

## Future

I might be even extending it or tweaking it a bit, cause later on the course it will be useful in webapplication or with a Graphical Interface or work with a database instead of dataset for optimal execution timing for loads of data.
