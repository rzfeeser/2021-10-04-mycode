#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
A script to demonstrate the power of Regular Expression (regex) and
the requests library."""

# standard library imports go above 3rd party imports (best practice)
import re

# python3 -m pip install requests
import requests

def main():
    """Search a website's content"""

    searchFor = '' # this is the users input

    print("Where should we search?")
    url = input("> ")  # collect user input

    print(f"Great! So we'll try to open this URL {url}")
    
    while searchFor != 'q':
        print("Enter the search phrase, or 'q' to quit.")
        searchFor = input("> ").lower().replace(" ", "|")

        resp = requests.get(url)  # Send HTTP GET
        searchMe = resp.text      # strip everything off the response as a string (text)

        # use the re.search() to determine if our website has the pattern we are looking for
        # it works by taking arguments, the first is the regex search pattern, and the second
        # is the string to search within

        search_result = re.search(searchFor, searchMe)
        numMatch = len(re.findall(searchFor, searchMe))

        if search_result:
            print("Found a match!")
            print(f"There were a total of {numMatch} matches.")
        else:
            print("No match!")

    print("Thanks for searching.")

if __name__ == "__main__":
    main()

