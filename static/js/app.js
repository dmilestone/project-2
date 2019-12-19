console.log(target_city)
console.log("xxxxxxxxxxxxxxxxx")
console.log(raw_city)
console.log("xxxxxxxxxxxxxxxxx")
console.log(city_input)


optionChanged(city_input) {
	const data = await d3.json(`/create/${city_input}`);
	console.log(city_input)
	console.log("xxxxxxxxxxxxxxxxx")
	console.log("raw_city")

}

async function buildCharts(sample) {

	// @TODO: Use `d3.json` to fetch the sample data for the plots
	  const data = await d3.json(`/create/${city}`);
	  console.log(city)
	//   buildBubbleChart(data);
  
	//   buildPieChart(data);
	  // @TODO: Build a Pie Chart
	  // HINT: You will need to use slice() to grab the top 10 sample_values,
	  // otu_ids, and labels (10 each).
	  


// function optionChanged(newSample) {
//   // Fetch new data each time a new sample is selected
//   buildCharts(newSample);
//   buildMetadata(newSample);
// }

// Initialize the dashboard
