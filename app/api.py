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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)