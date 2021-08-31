"""
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
##
## It's not case sensitive.

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


def listing_defin_(word):
    """To print one or more word definitions"""
    definition = ""
    for defin_ in data[word]:
        # find the index for each definition in the list of definitions
        i = data[word].index(defin_)
        i = str(i + 1)
        definition += i + " : " + defin_ + "\n"
    return definition

def wordsearch(word):
    """Search a word you're searching and returns vocabulary entry"""

    # IN CASE OF WORD MATCHING
    if word in data.keys():   # better to start with simple obvious case, instead of slowing the program with unwanted worse case
        return listing_defin_(word)

    # if difflib have any matches for not clear words
    elif len(get_close_matches(word, data.keys())) > 0 :
        # get_close_matches returns a list of matches with default ratio of diverence cutoff=0.6

        ## LET'S ask if there it's the first match the word user is searching
        matches_ = get_close_matches(word, data.keys())
        for matched_ in matches_:
            yORn_ = input("Mmm, did you mean %s ? Insert Y or N: " % matched_)
            yORn_ = yORn_.lower()   # to avoid case sensitive

            if yORn_ == "y":
                return listing_defin_(matched_)
                break
            elif yORn_ == "n":
                if matched_ == matches_[-1]:
                    return "I'm out of options, sorry.\n\tMaybe check spelling and retry"
                continue
            elif yORn_ == r"\end":
                exit()  ## TODO for this to be good enough, I would like a Goobye statement in a Finally codeblock
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
            if your_word.istitle():
                query = your_word
            else:
                query = your_word.lower()   # to avoid case sensitive

            # To stop the program entering "\end"
            if query == r"\end":
                print("Goodbye!")
                break

            # searching query
            print(wordsearch(query))

            # Asking if user wants to see another word
            yORn = str(input("Done. Any other word? Enter Y or N: "))
            yORn = yORn.lower()

            if yORn == "y" :
                continue
            elif yORn == "n" or yORn == r"\end":
                print("Goodbye!")
                break
            else:
                print("I guess YES you do")

    except:
        raise

    finally:
        print("Goodbye! 👋")