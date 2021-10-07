#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Challenge 03 - how many lines contain our search words?"""


def main():

    # we want to track the number of LINES that contain the users search words
    # the order of these words is NOT importat
    # it is ONLY importat that the words appear within the line
    counter = 0

    words = input("Provide the words you want to look for, within a line. We will search inside of our test file: ")
    words = words.split() # transform words into a list of the words entered by the user
    # Starbucks Sunshine
    # ['Starbucks', 'Sunshine']

    # open our data source (test data)
    with open("datasource.txt") as of:

        for line in of:  # time to examine a SINGLE line
            
            # now that we have a single line, we want to check that line for inclusion of our word(s)
            for word in words: # begin looping across the word(s) the user input as search data
                if word in line:
                    pass # the word is in the line, thats good
                else:
                    break

                if word == words[-1]:
                    counter = counter + 1

    print(f"The number of lines containing your words is... {counter}")

main()
