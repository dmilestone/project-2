# project-2

As this was a group project, front end portion can be found at:
https://github.com/rfpoulos/project-front-end

The goal of this project was to tell a story through interactive means and data visualizations. 

Visualizations must include:
-Python Flask- powered RESTful API
-HTML/CSS
-JaaScript
-At least one database (we chose SQLite)

Additional Requirments:
-Data set with at least 100 records (ours had over 1 million)
-Combination of web scraping and Leaflet or Plotly (we use Leaflet)
-Final Visualization must include at least 3 views
-Some level of user-driven interaction

Our project:
- Analyzes car accident data from 2016-2019 across the US sourced from Kaggle.com
- Created a website that takes either a date or city in Georgia as input and maps the data using Leaflet
- A third clickable view portrays same data in table form
- Includes API that calls json data from opencage.com to convert input city to lattitude and longitude to create radius of accidents to show on graph
-Uses Flask, HTML, SQLAlchemy, JavaScript, Python, Pandas
