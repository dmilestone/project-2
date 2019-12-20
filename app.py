import os
import json
import pandas as pd
import numpy as np
from flask_cors import CORS

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, inspect, func

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

import convert_input

# init app
app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/accident_data_GA.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()

engine = db.engine
Base.prepare(engine, reflect=True)

# reflect the tables
# engine = create_engine("sqlite:///db/accident_data_GA.sqlite")

# Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples
Incidents = Base.classes.ga_accident


@app.route("/")
def index():

    """Return the homepage."""
    return render_template("index.html")

@app.route('/get/<city>', methods=['GET', 'POST'])
def get_accident_by_city(city):
    session = Session(engine)

    city_input = city
    print(city_input)
    # if request.method == 'GET':
    # raw_city = request.form['city_input']
    target_city = city_input + ', GA'
    
    loc_coords = convert_input.scrape(target_city)
    print(loc_coords)
    lat = loc_coords['lat']
    lng = loc_coords['long']

    maxlat = lat+0.5
    maxlong = lng+0.5
    minlat = lat-0.5
    minlong = lng-0.5

    # inspector = inspect(engine)
    # mytables = inspector.get_table_names()
    # print(mytables)

    sel = [Incidents.Severity,Incidents.StartDate,Incidents.StartTime,Incidents.Start_Lat,Incidents.Start_Lng,Incidents.Description,Incidents.Weather_Condition]
    
    result = session.query(*sel).\
    filter(Incidents.Start_Lat > minlat).filter(Incidents.Start_Lat < maxlat).\
    filter(Incidents.Start_Lng > minlong).filter(Incidents.Start_Lng < maxlong).\
    limit(10).\
    all()
    
    features = []
    for accident in result:
        point = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [accident[3], accident[4]]
            }
        }
        features.append(point)

    response = {
        "type": "Feature",
        "features": features
    }

    response_JSON = json.dumps(response)

    # # Create a dictionary entry for each row of metadata information
    # sample_metadata = {}
    # for result in results:
    #     sample_metadata["Severity"] = result[3]
    #     sample_metadata["StartDate"] = result[4]
    #     sample_metadata["StartTime"] = result[5]
    #     sample_metadata["Start_Lat"] = result[8]
    #     sample_metadata["Start_Lng"] = result[9]
    #     sample_metadata["Description"] = result[10]
    #     sample_metadata["Weather_Condition"] = result[18]
    
    # print(sample_metadata)
    session.close()
    return response_JSON

    # elif: request.method == 'POST':
    #     return render_template('database_error.html')

@app.route('/getdate/<date>', methods=['GET', 'POST'])
def get_accident_by_date(date):
	session = Session(engine)

	newdate = date.split('-')

	month = newdate[0]
	day = newdate[1]
	year = newdate[2]
	full_date = month+"/"+day+"/"+year

	sel = [Incidents.Severity,Incidents.StartDate,Incidents.StartTime,Incidents.Start_Lat,Incidents.Start_Lng,Incidents.Description,Incidents.Weather_Condition]

	results2 = session.query(*sel).\
    filter(Incidents.StartDate == full_date).\
    limit(10).\
    all()

	print(date)
	print(full_date)
	print(results2)
	
	response_JSON2 = json.dumps(results2)

	session.close()
	return response_JSON2

# @app.route('/gettime/<time>', methods=['GET', 'POST'])
# def get_accident_by_time(time):
# 	session = Session(engine)

# 	sel = [Incidents.Severity,Incidents.StartDate,Incidents.StartTime,Incidents.Start_Lat,Incidents.Start_Lng,Incidents.Description,Incidents.Weather_Condition]

# 	results3 = session.query(*sel).\
# 	filter(or_(Incidents.StartTime.like("17%"),Incidents.StartTime.like("16%")).\
# 		limit(10).\
# 		all()

# 	myresponse= json.dumps(results3)
# 	session.close()
# 	return myresponse

if __name__ == "__main__":
	app.run()
