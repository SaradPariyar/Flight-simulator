import json

import requests
from flask import Flask
from gm import Database
from flask_cors import CORS
import random
import mysql.connector

db = Database()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight',
    user='root',
    password='Ratgai#1!',
    autocommit=True
)


@app.route('/continents')
def continents():
    sql = f'''SELECT DISTINCT continent
              FROM country'''
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return json.dumps(result)


@app.route('/countries/<continent>')
def countries_by_continent(continent):
    sql = f'''SELECT iso_country, name
              FROM country
              WHERE continent = %s'''
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute(sql, (continent,))
    result = cursor.fetchall()
    return json.dumps(result)


@app.route('/airports/<country>')
def airports_by_country(country):
    sql = f'''SELECT ident, name, latitude_deg, longitude_deg
              FROM airport WHERE iso_country = %s'''
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute(sql, (country,))
    result = cursor.fetchall()
    return json.dumps(random.sample(result, 3))


@app.route('/airport/<icao>')
def airport(icao):
    sql = f'''SELECT name, latitude_deg, longitude_deg
              FROM airport
              WHERE ident=%s'''
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return json.dumps(result)


@app.route('/weather/<name>')
def weather(name):
    sql = '''select municipality from airport where name=%s'''
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute(sql, (name,))
    result = cursor.fetchone()
    municipal = result["municipality"]
    key = "8614c7f206c8dabab99a14d0736a39d2"
    request = "https://api.openweathermap.org/data/2.5/weather?q=" + municipal + "&appid=" + key

    try:
        response = requests.get(request)
        if response.status_code == 200:
            json_response = response.json()
            main = json_response['main']

    except requests.exceptions.RequestException as e:
        print("Request could not be completed.")
    return json.dumps(main)




@app.route('/treasure/<attempt>')
def treasure(attempt):
    result = random.randint(1, 2)
    final_score = 0
    if result == 1:
        final_score += 500

    else:
        final_score += 0
    return json.dumps(final_score)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)