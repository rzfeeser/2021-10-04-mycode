#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Tuesday Review"""


def main():
    
    astro = {"people": [{"craft": "ISS", "name": "Mark Vande Hei"}, {"craft": "ISS", "name": "Oleg Novitskiy"}, {"craft": "ISS", "name": "Pyotr Dubrov"}, {"craft": "ISS", "name": "Thomas Pesquet"}, {"craft": "ISS", "name": "Megan McArthur"}, {"craft": "ISS", "name": "Shane Kimbrough"}, {"craft": "ISS", "name": "Akihiko Hoshide"}], "number": 7, "message": "success"}

    print(astro.get('people'))

    print(astro.get('number'))

    print(astro.get('message'))

main()
