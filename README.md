# Search-Dictionary

Command Line Interface programs to search a word in a `data.json` **dataset** or a **remote MySQL database**, made as an exercize during [The Python Mega Course](https://www.udemy.com/gift/the-python-mega-course/) by Ardit Sulce on Udemy.

## scripts

- `searchdictionary.py` reads from `data.json`
- `sourcevar1.py` reads from a MySQL database using a Python module version of the app

## Instructions

To stop it any time enter `\end` (FIXED, it works ANYTIME 👋)\
Now even with `^C` (`Ctrl + C`) interruption, without raising an Exception

Enter any words you need to look for and answer Y or N when
comfirmation is required.

**To run it, navigate to the folder location:**

#### Search in `data.json` dataset

- Run `python3 searchdictionary.py`

Query IS ***NOT* case sensitive** (because word are stored in lower and checked with all their possible CASE string methods). Version 1.2 features Title Case Words or Capitals (like Paris, Delhi, also New York) and UPPERCASE WORDS or simple ACRONYMS (like NATO and USA, without dots)

Comfirmation is not case sensitive.

#### Search in remote database

- Run `python3 sourcevar1.py`

In my *variation* I added the features for:
- simple typos (e.g. `rainn`, `rain`) to be found.
    - comparing among different suggestions, but within 1 character of difference
- while loop, to search as many words as you like
    - stops with keyword `\end`
- a warm "Goodbye! 👋"


Since this mysql query is **case INsensitive** it can by itself search any UPPER CASE or Title Case (in order to find words like NATO and Delhi)

##### Note: MySQL

With a simple query it loads less data into a file, UNLESS of a typo, then you will "Hold a sec" in order to let it checks all Definitions

## Future

I might be even extending it or tweaking it a bit, cause later on the course it will be useful in webapplication or with a Graphical Interface.
