// An array containing all of the information needed to create city and date markers
var locations = [
    {
        "type": "Feature",
        "features": [
          {
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [
                33.546177,
                -84.577347
              ]
            }
          },
          {
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [
                33.766376,
                -84.527321
              ]
            }
          },
          {
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [
                33.786896,
                -84.493134
              ]
            }
          },
          {
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [
                33.697849,
                -84.418266
              ]
            }
          },
          {
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [
                33.696915000000004,
                -84.404984
              ]
            }
          }
        ]
      }
];

// Define arrays to hold created city and date markers
var cityMarkers = [];
var dateMarkers = [];

// Loop through locations and create city and date markers
for (var i = 0; i < locations.length; i++) {
  // Setting the marker radius for the date 
  dateMarkers.push(
    L.circle(locations[i].coordinates, {
      stroke: false,
      fillOpacity: 0.75,
      color: "red",
      fillColor: "red",
      
    })
  );

// Setting the marker radius for the city by passing population into the markerSize function
   cityMarkers.push(
     L.circle(locations[i].coordinates, {
       stroke: false,
       fillOpacity: 0.75,
       color: "purple",
       fillColor: "purple",
       
     })
   );
 }

// Define variables for our base layers
 var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
   attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
   maxZoom: 18,
   id: "mapbox.streets",
   accessToken: API_KEY
 });

 var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>", 
   maxZoom: 18, 
   id: "mapbox.dark",
   accessToken: API_KEY
 });

// Create two separate layer groups: one for cities and one for states
 var date = L.layerGroup(stateMarkers);
 var cities = L.layerGroup(cityMarkers);

// Create a baseMaps object
 var baseMaps = {
   "Street Map": streetmap,
   "Dark Map": darkmap
 };

// Create an overlay object
 var overlayMaps = {
   "Date Accident": date,
   "City Accident": cities
 };

// Define a map object
 var myMap = L.map("map", {
   center: [33.753746, -84.386330],
   zoom: 5,
   layers: [streetmap, states, cities]
 });

// Pass our map layers into our layer control
// Add the layer control to the map
 L.control.layers(baseMaps, overlayMaps, {
   collapsed: false
 }).addTo(myMap);
