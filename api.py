import requests
import pprint


def main():

    astroid_strikes = requests.get("https://data.nasa.gov/resource/y77d-th95.json")
    pprint.pprint(astroid_strikes.json())
main()