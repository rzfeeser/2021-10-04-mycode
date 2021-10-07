import requests
import pandas

resp = requests.get("https://api.magicthegathering.io/v1/sets")

cards = resp.content # create the string

df = pandas.read_json(cards)
