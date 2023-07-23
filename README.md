# Hawaii Climate Analysis

Hawaii Climate Analysis is a Python-based climate study tool that provides users with a range of information about Hawaii's weather patterns. Leveraging on a SQLite database, the application comprises an exploratory analysis notebook climate_starter.ipynb for detailed climate study, and an API server app.py that serves key climate data endpoints.

## Usage

### Exploratory Climate Analysis - Jupyter Notebook (climate_starter.ipynb)

This Jupyter notebook contains an exploratory analysis of the climate in Hawaii. It includes:

The most recent 12 months of precipitation data, plotted as a function of time.

![Screenshot 2023-07-22 152749](https://github.com/ehsanshahrabi/sqlalchemy-challenge/assets/124327258/9810fde5-8011-4a9d-9be7-b48759b6bf32)

Summary statistics for precipitation data.

The total number of stations in the dataset.

The most active weather stations, and the respective number of observations.

Temperature observations for the most active station, over the last 12 months, presented as a histogram.

![Screenshot 2023-07-22 152807](https://github.com/ehsanshahrabi/sqlalchemy-challenge/assets/124327258/2bc335af-ea15-44d0-b872-060a930edbd9)


### Climate API - Flask Application (app.py)
The Flask application serves as a climate data API with various endpoints:

Home (/): This route gives an overview of all the available routes.

Precipitation (/api/v1.0/precipitation): This route returns a JSON object with the date and precipitation from the last year.

Stations (/api/v1.0/stations): This route returns a JSON list of the stations.

Temperature Observations (/api/v1.0/tobs): This route returns a JSON list of Temperature Observations (TOBS) for the previous year from the most active station.

Start Date Analysis (/api/v1.0/<start>): Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start date. Replace <start> with a date in YYYY-MM-DD format.

Date Range Analysis (/api/v1.0/<start>/<end>): Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start-end date range. Replace <start> and <end> with dates in YYYY-MM-DD format.

## Installation & Usage

Clone the repo: git clone <repo_url>

Change directory to the local repo: cd <repo_directory>

Run the Flask application: python app.py

Open a web browser and go to http://localhost:5000/ to see the available routes. To use a specific route, append it to the base URL. For example, for precipitation data use http://localhost:5000/api/v1.0/precipitation.

### Example

To get temperature stats starting from 2017-01-01, use the URL http://localhost:5000/api/v1.0/2017-01-01

To get temperature stats from 2017-01-01 to 2017-12-31, use the URL http://localhost:5000/api/v1.0/2017-01-01/2017-12-31

Please note that the Flask application runs on port 5000 by default. If your application runs on a different port, replace 5000 with the appropriate port number.
