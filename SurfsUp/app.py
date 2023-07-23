# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt
import numpy as np
from datetime import datetime, timedelta


#################################################
# Database Setup
#################################################

# Create an engine to connect to hawaii.sqlite database.
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
# Create an instance of Flask
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
# Home page
# List all routes that are available
@app.route("/")
def home():
    return (
        f"<h1>Welcome to the Hawaii Climate Analysis API!</h1>"
        f"<h2>You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. "
        f"To help with your trip planning, we provide climate analysis about the area. </h2>"
        f"<h3>Available Routes:</h3>"
        f"<ul>"
        f"<li><a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a>: Get the date and precipitation data for the last year.</li>"
        f"<li><a href='/api/v1.0/stations'>/api/v1.0/stations</a>: Get the list of all the weather stations.</li>"
        f"<li><a href='/api/v1.0/tobs'>/api/v1.0/tobs</a>: Get the date and temperature observations of the most active station for the last year.</li>"
        f"<li>/api/v1.0/&lt;start&gt; (in the format YYYY-MM-DD): Get the minimum temperature, the average temperature, and the maximum temperature for a specified start date.</li>"
        f"<li>/api/v1.0/&lt;start&gt;/&lt;end&gt; (in the format YYYY-MM-DD/YYYY-MM-DD): Get the minimum temperature, the average temperature, and the maximum temperature for a specified date range.</li>"
        f"</ul>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date one year from the last date in data set.
    latest_date = session.query(Measurement.date).order_by(
        Measurement.date.desc()).first()
    latest_date = datetime.strptime(latest_date[0], '%Y-%m-%d')
    year_ago = latest_date - timedelta(days=365)

    # Query all precipitation data within the last year.
    prcp_data = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_ago).all()

    # Close the session
    session.close()

    # Convert the query results to a dictionary with date as the key and prcp as the value.
    prcp_data_list = {date: prcp for date, prcp in prcp_data}

    # Return the JSON representation of the dictionary.
    return jsonify(prcp_data_list)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    station_data = session.query(Station.station, Station.name).all()

    # Convert query results to a list of dictionaries
    station_list = [{"station": station, "name": name}
                    for station, name in station_data]

    # Close the session
    session.close()

    # Return the JSON representation of the list of station dictionaries.
    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date one year from the last date in data set.
    latest_date = session.query(Measurement.date).order_by(
        Measurement.date.desc()).first()
    latest_date = datetime.strptime(latest_date[0], '%Y-%m-%d')
    year_ago = latest_date - timedelta(days=365)

    # Query the last 12 months of temperature observation data for this station
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= year_ago).all()

    # Convert query results to a list of dictionaries
    tobs_list = [{"date": date, "tobs": tobs} for date, tobs in tobs_data]

    # Close the session
    session.close()

    # Return the JSON representation of the list of station dictionaries.
    return jsonify(tobs_list)

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start


@app.route("/api/v1.0/<start>")
def start(start):

    # Create a new session (link) from Python to the database.
    session = Session(engine)

    # Query the minimum temperature, average temperature, and maximum temperature from the given start date onwards.
    temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    # Close the session
    session.close()

    # Ensure data is in a serializable format
    temp_list = [{"TMIN": result[0], "TAVG": result[1],
                  "TMAX": result[2]} for result in temp_data]
    # Return the JSON representation of the list of station dictionaries.
    return jsonify(temp_list)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):

    # Create a new session
    session = Session(engine)

    # Query the minimum temperature, average temperature, and maximum temperature within the given date range.
    temp_data = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    session.close()

    # Ensure data is in a serializable format
    temp_list = [{"TMIN": result[0], "TAVG": result[1],
                  "TMAX": result[2]} for result in temp_data]
    # Return the JSON representation of the list of station dictionaries.
    return jsonify(temp_list)


# Main driver function
if __name__ == "__main__":
    app.run(debug=True)
