import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, inspect, func

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

import convert_input

# init app
app = Flask(__name__)

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

    maxlat = lat+1
    maxlong = lng+1
    minlat = lat-1
    minlong = lng-1
    print(maxlong)

    print(session.query(Incidents.Start_Lat > minlat).first())

    inspector = inspect(engine)
    mytables = inspector.get_table_names()
    print(mytables)

    sel = [Incidents.Severity,Incidents.StartDate,Incidents.StartTime,Incidents.Start_Lat,Incidents.Start_Lng,Incidents.Description,Incidents.Weather_Condition]
    
    result = session.query(*sel).\
    filter(Incidents.Start_Lat > minlat).filter(Incidents.Start_Lat < maxlat).\
    filter(Incidents.Start_Lng > minlong).filter(Incidents.Start_Lng < maxlong).all()
    
    print(result)
    result2 = session.query(Incidents.Start_Lng).filter(Incidents.Start_Lng > maxlong).all()
    print(result2)
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
    return render_template("index.html", city_input=city_input)

    # elif: request.method == 'POST':
    #     return render_template('database_error.html')

if __name__ == "__main__":
    app.run()
