# Hawaii Climate Analysis API

Welcome to the Hawaii Climate Analysis API! This API provides climate analysis data for the beautiful vacation destination of Honolulu, Hawaii, to assist you in planning your trip. The data is based on historical weather measurements, enabling you to make informed decisions about your vacation activities.

## Available Routes

The Hawaii Climate Analysis API offers the following routes:

/api/v1.0/precipitation : Returns the date and precipitation data for the last year. Output format: JSON

/api/v1.0/stations : Returns a list of all the weather stations. Output format: JSON

/api/v1.0/tobs : Returns the date and temperature observations of the most active weather station for the last year. Output format: JSON

/api/v1.0/<start> : Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start date (in the format YYYY-MM-DD). Output format: JSON

/api/v1.0/<start>/<end> : Returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified date range (in the format YYYY-MM-DD/YYYY-MM-DD). Output format: JSON

## Usage
Once the API is up and running, you can access the available routes using a web browser or any API client (e.g., Postman).

To retrieve the last year's precipitation data, visit /api/v1.0/precipitation.

To obtain the list of weather stations, go to /api/v1.0/stations.

To get the temperature observations for the last year from the most active station, visit /api/v1.0/tobs.

To retrieve temperature statistics for a specific start date, use /api/v1.0/<start> and replace <start> with the desired date (e.g., /api/v1.0/2017-01-01).

To retrieve temperature statistics for a date range, use /api/v1.0/<start>/<end> and replace <start> and <end> with the desired date range (e.g., /api/v1.0/2017-01-01/2017-01-15).

