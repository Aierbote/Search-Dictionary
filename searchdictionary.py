"""
This is the exercizeVers-1.1
Feature of matching words like Delhi or Paris

Command Line Interface program to search a word in a data.json dictionary,
made as an exercize during The Python Mega Course
#    https://www.udemy.com/gift/the-python-mega-course/
by Ardit Sulce on Udemy

This version is a bit messy, cause that's how I figured out the exercize

##      INSTRUCTIONS
## Enter any words you need to look for and answer Y or N when
## comfirmation is required.
## To stop it any time enter '\end' (without quotes)
##      almost anytime :think:
##      FIXED: ANYTIME ;-) 😉
##
## It's not case sensitive.
## Unless your word is Capitalized (as a city) or Title Case (New York)

In the future I might be even extending it or tweaking it abit

Later on the course even to make it useful in webapplication or with a
Graphical Interface or work with a database instead of dataset for
optimal execution timing for loads of data.
"""

# since we are going to work with a json file for the data
import json
# difflib is useful to find words even if typos or slightly different
from difflib import get_close_matches  ## a standard library

data = json.load(open("data.json", "r"))

if not isinstance(data, dict):
    print("There might be a problem with opening/loading from data.json")

# Useles, because I need to simply return the thing and check if the returned thing is string or a list element as in the video version of app1.py
# def listing_defin_(word):
#     """To print one or more word definitions"""
#     definition = ""
#     for defin_ in data[word]:
#         # find the index for each definition in the list of definitions
#         i = data[word].index(defin_)
#         i = str(i + 1)
#         definition += i + " : " + defin_ + "\n"
#     return definition


def wordsearch(word):
    """Search a word you're searching and returns vocabulary entry"""

    # first storin the word in lower, in case accidental upper letters
    word = word.lower()
    # then let's check if there are instances of the viable options in the dictionary, like UPPER Title or similar word

    # IN CASE OF WORD MATCHING
    if word in data.keys():   # better to start with simple obvious case, instead of slowing the program with unwanted worse case
        return data[word]
    # Let's check how the word was typed inside first, it it's title/capital (e.g. Paris) or upper (acronym without dots, like USA or NATO) it wont' be searched as lower
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data.keys():
        return data[word.upper()]

    # if difflib have any matches for not clear words
    elif len(get_close_matches(word, data.keys())) > 0 :
        # get_close_matches returns a list of matches with default ratio of diverence cutoff=0.6

        ## LET'S ask if there it's the first match the word user is searching
        matches_ = get_close_matches(word, data.keys())
        for matched_ in matches_:
            yORn_ = input("Mmm, did you mean %s ? Insert Y or N: " % matched_)
            yORn_ = yORn_.lower()   # to avoid case sensitive

            if yORn_ == "y":
                return data(matched_)
            elif yORn_ == "n":
                if matched_ == matches_[-1]:
                    return "I'm out of options, sorry.\n\tMaybe check spelling and retry"
                continue
            elif yORn_ == r"\end":
                exit()
            else:
                return "Sorry, I don't know which word you're searching.\n\tMaybe check spelling and retry"


    # IN CASE OF WORD NOT MATCHING
    else:    # MEMENTO  Unsure if I want the long condition "elif not word in data.keys():" instead
        return f"There is no word like '{word}', double check your word spelling"

if __name__ == "__main__":
    # Keeps running searchdictionary.py unless "\end"
    try:
        while True:
            your_word = str(input("Let me know the word you search: "))

            # To stop the program entering "\end"
            if your_word == r"\end":
                exit()

            # searching query
            output = wordsearch(your_word)

            # let's check if the output is a list of a simple string
            if type(output) == list:
                for item in output:
                    print(output.index(item) +1, ":", item)
            else:
                print(output)

            # Asking if user wants to see another word
            yORn = str(input("Done. Any other word? Enter Y or N: "))
            yORn = yORn.lower()

            if yORn == "y" :
                continue
            elif yORn == "n" or yORn == r"\end":
                exit()
            else:
                print("I guess YES you do")

    except Exception:       # this way ^C (`ctrl + C`) will not raise KeyboardInterrupt
        raise

    finally:
        print("Goodbye! 👋")