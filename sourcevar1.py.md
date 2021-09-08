# `sourcevar1.py` - Search Dictionary with mysql

It's the second given material for real exercize during [The Python Mega Course](https://www.udemy.com/gift/the-python-mega-course/) by Ardit Sulce on Udemy.

Using mysql to search a word in database.

## Features

I added the features for:
- simple typos (e.g. `rainn`, `rain`) to be found.
    - comparing among different suggestions, but within 1 character of difference
- while loop, to search as many words as you like
    - stops with keyword `\end`
- a warm "Goodbye! 👋"


Since this mysql query is **case INsensitive** it can by itself search any UPPER CASE or Title Case (in order to find words like NATO and Delhi)

### MySQL

With a simple query it loads less data into a file, UNLESS of a typo, then you will "Hold a sec" in order to let it checks all Definitions