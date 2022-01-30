import requests
import pprint
import datetime

def main():

    astroid_strikes = requests.get("https://data.nasa.gov/resource/y77d-th95.json")
    
    for strike in astroid_strikes.json():
        if "year" in strike:
            only_year = datetime.datetime.strptime(strike["year"], '%Y-%m-%dT%H:%M:%S.%f')
            # print(only_year.year)
            strike["year"]=only_year.year
            #print(strike)
        elif "years" in strike:
            print("abcd")
        else:
            print("no year")
    print("end")
    astroid_strikes.json()[0]["year"]="1980"
    print(astroid_strikes.json()[0])
    

    #Thomas, create a function that utilizes this json and formats the date down to just year. 
    #example: 'year': '1869-01-01T00:00:00.000' to 'year': '1869'
    #Hints: For loop for data, google how to modify json in python, to modify the year look into python slice string

main()