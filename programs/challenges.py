# These challenges are intended to provide practice in basic python skills such as string manipulation, iteration, use of collection types and conditionals

# Challenge 1: Write a function which:
# - Takes a string as an argument
# - returns the string in all upper case if its' length is even, and all lower case if its' length is odd. Any non-alphabetic characters should not be changed
# - stretch goal: try to implement this both with and without the .upper()/.lower() methods

def func_1_methods(string):
    if(len(string) % 2 == 0):
        return string.upper()
    else:
        return string.lower()
    pass

def func_1_no_methods(string):
    pass

# Challenge 2: write a function which:
# - takes a word and a list of words as input
# - returns a new list containing only the words from the given list which differ from the given word in exactly one position
# You should ignore case

def func_2(string, list):
    pass

# Challenge 3: write a function which:
# - takes two ints and a list of ints as arguments
# - returns a list of bools where the ith element is True if list[i] has the two given ints as factors and false otherwise

def func_3(int1, int2, intlist):
    newlist = []
    for integer in intlist:
        if(integer % int1 == 0 and integer % int2 == 0):
            newlist.append(True)
        else:
            newlist.append(False)
    return newlist

    pass

# Challenge 4: write a function which:
# - takes a string as an argument
# - returns a new string containing only the letters from the original string which
#   are at an even-numbered position in the alphabet (letting a = 1, b = 2, ...)
# - the returned string should only contain letter characters. All chars in the
#   returned string should be lower case

def func_4(string):
    lowerstring = string.lower()
    newstring = ""
    for letter in lowerstring:
        if not(letter.isalpha()):
            newstring = newstring
        elif(ord(letter) % 2 == 0):
            newstring = newstring + letter
    return newstring
    pass

# Challenge 5: write a function which:
# - takes a list of integers as argument
# - for each int, creates a list of the factors of the number, including 1 but excluding the number itself
# - converts these lists to strings and writes them out to a csv file called factors.csv, each on a new line
# - note: this function should be a void (i.e return nothing)

def func_5(list):
    pass 

#the below code works for a single integer

#def func_5(integer):
 #   factors = []
  #  for i in range(1,integer):
   #     if (integer % i == 0):
    #        factors.append(str(i))
    #factorstring = "".join(factors)
    #with open("factors.csv", "w") as file:
     #   file.write(factorstring)
                
    pass

