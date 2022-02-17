import requests
import logging
import pprint
import psycopg2
import json

from psycopg2.extras import execute_values
from connection import Database
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields

# Initialize Flask
app = Flask(__name__)
api = Api(app)

class Asteroid:
    def __init__(self, json_object):
        logging.error(json_object)
        json_object = list(json_object)
        logging.error(json_object)
        logging.error(type(json_object))
        self.name = json_object[0]
        self.nametype = json_object[1]
        self.recclass = json_object[2]
        self.mass = json_object[3]
        self.fall = json_object[4]
        self.year = json_object[5]
        self.reclat = json_object[6]
        self.reclong = json_object[7]
        #self.geolocation = json_object.get('geolocation') #convert off dict


@app.route("/health")
def health_check():
    return {'message': 'Healthy'}  

@app.route("/name/<name>", methods = ['GET'])
def get_name(name):
    database_connection = Database()
    cur, conn  = database_connection.connect_db()
    name_var = f"SELECT name, nametype, recclass, mass, fall, year, reclat, reclong FROM nasa_data.asteroids WHERE name = '{name}'"
    response_get = cur.execute(name_var)
    record = cur.fetchall()
    record_json = json.dumps(record)
    #list_of_records = []
    #for record in record_json:
    #    class_record = Asteroid(record_json)
    conn.commit()
    conn.close()
    return(record_json)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)