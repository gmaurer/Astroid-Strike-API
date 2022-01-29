import requests
import pprint


def main():

    astroid_strikes = requests.get("https://data.nasa.gov/resource/y77d-th95.json")
    pprint.pprint(astroid_strikes.json())

    #Thomas, create a function that utilizes this json and formats the date down to just year. 
    #example: 'year': '1869-01-01T00:00:00.000' to 'year': '1869'
    #Hints: For loop for data, google how to modify json in python, to modify the year look into python slice string

main()