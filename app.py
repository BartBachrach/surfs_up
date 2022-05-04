import datetime as dt
from venv import create
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask
from flask import jsonify

engine = create_engine("sqlite:///hawaii.sqlite") #allows us to access/query the database

Base = automap_base() # gets us ready to reflect the DB

Base.prepare(engine, reflect=True) # this reflects the DB

Measurement = Base.classes.measurement # creates a variable to reference the table 'Measurement'

Station = Base.classes.station # creates a variable to reference the table 'Station'

session = Session(engine) # establishes a connection with the database

app = Flask(__name__) # creates the flask application 'app'

@app.route('/')
def welcome():
    return(
        '''
        Welcome to the Climate Analysis API!
        Available Routes:
        /api/v1.0/precipitation
        /api/v1.0/stations
        /api/v1.0/tobs
        /api/v1.0/temp/start/end
        ''')

@app.route('/api/v1.0/precipitation')
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365) # defines the time period we're looking for
    # the below queries the measurement table for date and precip, filters it by the above time window, and returns as a list
    precipiation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()     
    precip = {date: prcp for date, prcp in precipiation} # this takes the parameters set in the previous variable and lays them out how we want them
    return jsonify(precip)

@app.route('/api/v1.0/stations')
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route('/api/v1.0/tobs')
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
            filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route('/api/v1.0/temp/<start>')
@app.route('/api/v1.0/temp/<start>/<end>')
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)