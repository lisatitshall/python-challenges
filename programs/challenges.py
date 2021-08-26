# These challenges are intended to provide practice in basic python skills such as string manipulation, iteration, use of collection types and conditionals

# Challenge 1: Write a function which:
# - Takes a string as an argument
# - returns the string in all upper case if its' length is even, and all lower case if its' length is odd. Any non-alphabetic characters should not be changed
# - stretch goal: try to implement this both with and without the .upper()/.lower() methods

def func_1_methods(string):
    if len(string) % 2 == 0:
        return string.upper()
    else:
        return string.lower()

def char_swap(string, dictionary):
    outstring = ""
    for char in string:
            newChar = dictionary.get(char, char)
            outstring += newChar
    return outstring

def func_1_no_methods(string):
    upper_case_dict = {
        "A":"a",
        "B":"b",
        "C":"c",
        "D":"d",
        "E":"e",
        "F":"f",
        "G":"g",
        "H":"h",
        "I":"i",
        "J":"j",
        "K":"k",
        "L":"l",
        "M":"m",
        "N":"n",
        "O":"o",
        "P":"p",
        "Q":"q",
        "R":"r",
        "S":"s",
        "T":"t",
        "U":"u",
        "V":"v",
        "W":"w",
        "X":"x",
        "Y":"y",
        "Z":"z"
    }
    lower_case_dict = {
        "a":"A",
        "b":"B",
        "c":"C",
        "d":"D",
        "e":"E",
        "f":"F",
        "g":"G",
        "h":"H",
        "i":"I",
        "j":"J",
        "k":"K",
        "l":"L",
        "m":"M",
        "n":"N",
        "o":"O",
        "p":"P",
        "q":"Q",
        "r":"R",
        "s":"S",
        "t":"T",
        "u":"U",
        "v":"V",
        "w":"W",
        "x":"X",
        "y":"Y",
        "z":"Z"
    }
    if len(string) % 2 == 0:
        return char_swap(string, lower_case_dict)
    else:
        return char_swap(string, upper_case_dict)

# Challenge 2: write a function which:
# - takes a word and a list of words as input
# - returns a new list containing only the words from the given list which differ from the given word in exactly one position
# You should ignore case

def func_2(string, list):
    newlist = []
    for word in list:
        if len(word) != len(string):
            continue
        else:
            diffs = 0
            for i in range(len(word)):
                if word.lower()[i] == string.lower()[i]:
                    continue
                else:
                    diffs += 1
            if diffs == 1:
                newlist.append(word)
            else:
                continue
    return newlist
