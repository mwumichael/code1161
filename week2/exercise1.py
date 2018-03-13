"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"


#generates a list of words known as "some_words"
some_words = ['what', 'does', 'this', 'line', 'do', '?']

#for each item in the list, print it out individually
for word in some_words:
    print(word)
#printed each word in some_words as a list

#same as the previous function, the "x" is replacing the "word" but still refers to the same list
for x in some_words:
    print(x)

#prints out the list the exactly as it is entered
print(some_words)
#printed out list with square brackets as entered

# if the length of the list has more than three words, print the message
if len(some_words) > 3:
    print('some_words contains more than 3 words')
# printed the message above

#defines a function with platform.uname, which prints out the platform's underlying data.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()

#printed out uname_result with data regarding processors, versions, etc. 