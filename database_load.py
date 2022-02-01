import json
import psycopg2
import requests

from psycopg2.extras import execute_values

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

    def serialize(self):
        return(json.loads(self.__dict__))

def main():

    astroid_strikes = requests.get("https://data.nasa.gov/resource/y77d-th95.json")

    cur, conn = connect_db()
    
    listthin = []
    for x in astroid_strikes.json():
        new_asteroid = Asteroid(x)
        vals = tuple(new_asteroid.__dict__.values())
        listthin.append(vals)
    
    cur.executemany("INSERT into nasa_data.asteroids (name,nametype,recclass,mass,fall,year,reclat,reclong) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",listthin)
    conn.commit()
    conn.close()


def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="nasa_db",
        user="postgres",
        password="darling")

    cur = conn.cursor()
    return cur, conn    

main()