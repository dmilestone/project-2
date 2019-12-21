
var server = "http://127.0.0.1:5000/"
//Data by City url
var dataByCityURL = `${server}getbycity`

var generateMap = (data) =>{
  console.log(data)
  console.log(L)
  var myMap = L.map("map", {
    
    center: data.mapCenter,
    zoom: 10
  });
  
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets-basic",
    accessToken: API_KEY
  }).addTo(myMap);
  addMarkers(data.accidents, myMap)
}

var addMarkers = (markers, myMap) => {
  markers.forEach(marker => {
    L.circle(marker, {
      fillOpacity: 0.75,
      color: "white",
      fillColor: "purple",
      
    }).bindPopup("<h1>" + marker.name + "</h1> <hr> ").addTo(myMap);
  })
  
}

var getDataByCity = (city) =>{
  var getDataByCity = d3.json(`${dataByCityURL}/${city}`)
  .then(data => generateMap(data));
}
getDataByCity("Atlanta")