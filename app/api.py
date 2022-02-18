import requests
import logging
import pprint
import psycopg2
import json

from psycopg2.extras import execute_values
from connection import Database
from flask import Flask, request
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
    database_connection = Database()
    cur, conn  = database_connection.connect_db()
    name_var = f"SELECT name, nametype, recclass, mass, fall, year, reclat, reclong FROM nasa_data.asteroids WHERE name = '{name}'"
    response_get = cur.execute(name_var)
    record = cur.fetchone()
    record_json = json.dumps(record)
    #list_of_records = []
    #for record in record_json:
    #    class_record = Asteroid(record_json)
    conn.commit()
    conn.close()
    response = app.response_class(
        response=record_json,
        status=200,
        mimetype='application/json'
    )
    return(response)

@app.route("/asteroid/", methods = ['POST'])
def create_new_asteroid():
    content_type = request.headers.get('Content-Type')
    data = request.get_json()
    database_connection = Database()
    cur, conn  = database_connection.connect_db()
    
    new_asteroid_obj = Asteroid(data)
    new_asteroid = tuple(new_asteroid_obj.__dict__.values())
    logging.warning("ASTER")
    logging.warning(new_asteroid)

    try:
        cur.execute("INSERT into nasa_data.asteroids (name,nametype,recclass,mass,fall,year,reclat,reclong) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",new_asteroid)
    except:
       logging.warning("NO GO") 
    conn.commit()
    conn.close()
    response = app.response_class(
        response=json.dumps(data),
        status=201,
        mimetype='application/json'
    )
    return(response)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)