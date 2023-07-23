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

Home Endpoint (/): Displays the home page with the list of all available routes.

Precipitation Data (/api/v1.0/precipitation): Returns a JSON list of the date and precipitation from the last year.

Stations (/api/v1.0/stations): Returns a JSON list of all weather stations.

Temperature Observations (/api/v1.0/tobs): Returns a JSON list of the date and temperature observations from the most active station over the last year.

Start Date Analysis (/api/v1.0/<start>): Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.

Date Range Analysis (/api/v1.0/<start>/<end>): Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start-end range.

To run the API, simply navigate to the application's root directory and execute python app.py in the terminal. You can then access the API endpoints through http://localhost:5000/.
