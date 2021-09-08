import mysql.connector
from difflib import get_close_matches

conn = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)



def search_query(execute_str = "SELECT * FROM Dictionary"):    # NOTE check later for the correct args
    """ Search with an execute_str in given connector, unless not specified otherwise

        BY DEFAULT execute_str = "SELECT * FROM Dictionary"

    give a different string for a more Selective Query

    Example: if you want to find variable `word` then
        user_execute_str = "SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word
    """

    cursor = conn.cursor()
    query = cursor.execute(execute_str)
    results = cursor.fetchall()

    return results


def close_matches(wrong_word):
    """ Suggest alternative words in case a typo similar words in database """
    # Designed search_query() query/read all words, unless specific execute_str
    all_expressions = [x[0] for x in search_query()]

    if len(get_close_matches(wrong_word, all_expressions)) > 0:
        suggest_matches = get_close_matches(wrong_word, all_expressions)
        for suggested_word in suggest_matches:
            yORn = input("Searching for '%s' ? Enter Y or N: " % suggested_word)

            if yORn.lower() == "y":
                sugg_execute_str = "SELECT * FROM Dictionary WHERE Expression = '%s' " % suggested_word
                results = search_query(sugg_execute_str)
                return results
            elif yORn.lower() == "n":
                if suggested_word == suggest_matches[-1]:
                    return "I'm out of options, sorry.\n\tMaybe check spelling and retry"
                continue
            elif yORn == r"\end":
                break
            else:
                return "No word found!"



if __name__ == "__main__":
    try:
        while True:
            word = input("Enter the word: ")

            if word == r"\end":
                break

            user_execute_str = "SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word

            store_results = search_query(user_execute_str)

            # gets the results out of the tuple/list if found
            if store_results:
                for result in store_results:
                    print(result[0])
            else:
                print("No match for '%s' found..." % word , "Hold a sec..., let me think...", sep="\n")

                # let's see if there is anything similar to word in case it's a wrong_word
                sugges_results = close_matches(word)

                # gets results out of a list, else outputs string during the process
                # # in case of `\end` "exit()" (no idea why it doesn't work) a.k.a. None, ending the whileloop
                if type(sugges_results) == list:
                    for result in sugges_results:
                        print(sugges_results.index(result) +1, ":", result[1] )
                elif sugges_results == None:
                    break
                else:
                    print(sugges_results)

            # Asking if user wants to see another word
            yORn = str(input("Done. Any other word? Enter Y or N: "))

            if yORn.lower() == "y" :
                continue
            elif yORn.lower() == "n" or yORn == r"\end":
                break
            else:
                print("I guess YES you do")
    except Exception:
        raise
    finally:
        print("Goodbye! 👋")




# MEMENTO DETOUR NOTE:
# this line should work to get lower or upper
#       "SELECT * FROM NameOfTable WHERE ValueName = LOWER(%s)" % string_you_search
# as read from
#       https://stackoverflow.com/questions/3936967/mysql-is-a-select-statement-case-sensitive


        # # Debbugging
        # print(f"{all_expressions = }")
