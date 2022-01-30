import requests
import pprint
import psycopg2
import json

from psycopg2.extras import execute_values
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

# Initialize Flask
app = Flask(__name__)
api = Api(app)

class Asteroid:
    def __init__(self, json_object):
        self.name = json_object.get('name')
        self.nametype = json_object.get('nametype')
        self.recclass = json_object.get('recclass')
        self.mass = json_object.get('mass')
        self.fall = json_object.get('fall')
        self.year = json_object.get('year')
        self.reclat = json_object.get('reclat')
        self.reclong = json_object.get('reclong')
        #self.geolocation = json_object.get('geolocation') #convert off dict

@app.route("/health")
def health_check():
    return {'message': 'Healthy'}  

@app.route("/name/<name>", methods = ['GET'])
def get_name(name):
    cur, conn  = connect_db()
    name_var = f"SELECT * FROM nasa_data.asteroids WHERE name = '{name}'"
    response_get = cur.execute(name_var)
    record = cur.fetchall()

    record_json = json.dumps(record)
    #class_record = Asteroid(record_json)
    conn.commit()
    conn.close()
    return(str(record_json))


def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="nasa_db",
        user="postgres",
        password="darling")

    cur = conn.cursor()
    return cur, conn   


def main():

    astroid_strikes = requests.get("https://data.nasa.gov/resource/y77d-th95.json")
    test = Asteroid(astroid_strikes.json()[0])
    print(test.serialize())


    #Thomas, create a function that utilizes this json and formats the date down to just year. 
    #example: 'year': '1869-01-01T00:00:00.000' to 'year': '1869'
    #Hints: For loop for data, google how to modify json in python, to modify the year look into python slice string

#main()

#if __name__ == "__main__":
#    app.run(debug=True)