//d3.select(window).on("load", fetchData);
fetchData();
function init() {
    var selector = d3.select("#selDataset");
  
    d3.json("samples.json").then((data) => {
      console.log(data);
      var sampleNames = data.names; // Name ids
      sampleNames.forEach((sample) => {
        selector
          .append("option")
          .text(sample)
          .property("value", sample);
  
        });

  })}
  
  init();

function fetchData() {
    buildMetadata(940);
    build_Barchart(940);
    build_Bubblechart(940);
    // d3.json("samples.json").then((data) => {
    //   var metadata = data.metadata;

    //   var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
    //   var result = resultArray[0];
    //   console.log(result);
    // });

}  

  function optionChanged(newSample) {
    buildMetadata(newSample);
    build_Barchart(newSample);
    build_Bubblechart(newSample);
  }


  function buildMetadata(sample) {
    d3.json("samples.json").then((data) => {
      var metadata = data.metadata;


      var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
      var result = resultArray[0];


      var PANEL = d3.select("#sample-metadata");
      PANEL.html("");
      PANEL.append("h6").text("id: " + result.id);
      PANEL.append("h6").text("ethnicity: " + result.ethnicity);
      PANEL.append("h6").text("gender: " + result.gender);
      PANEL.append("h6").text("age: " + result.age);
      PANEL.append("h6").text("location: " + result.location);
      PANEL.append("h6").text("bbtype: " + result.bbtype);
      PANEL.append("h6").text("wfreq: " + result.wfreq);
    });
  }


  function change_label(id) {
    return "otu" + id;
  }

  function build_Barchart(sample) {
    d3.json("samples.json").then((data) => {
      var samples = data.samples; // data samples
      var resultArray = samples.filter(sampleObj => sampleObj.id == sample); // User selection
      var result = resultArray[0];
      var sample_values = result.sample_values; // x      
      var otu_ids = result.otu_ids; // y
      var y_label = otu_ids.slice(0,10).map(change_label).reverse();
      var bar_data = [{
        x: sample_values.slice(0,10).reverse(),
        y: y_label,
        type: "bar", orientation: "h"
      }]
    Plotly.newPlot("bar", bar_data);
  });
}


  function build_Bubblechart(sample) {
    d3.json("samples.json").then((data) => {
      var samples = data.samples; // data samples
      var resultArray = samples.filter(sampleObj => sampleObj.id == sample); // User selection
      var result = resultArray[0];
      var sample_values = result.sample_values; // y
      var otu_ids = result.otu_ids; // x
      var x_label = otu_ids;
      var bubble_data = [{
        x: x_label,
        y: sample_values,
        mode: "markers",
        marker: {
          color: x_label,
          size: sample_values,
          sizeref: 10.0 * sample_values,
          sizemode: 'area'
        }
      }]
    Plotly.newPlot("bubble", bubble_data);
  });
}
