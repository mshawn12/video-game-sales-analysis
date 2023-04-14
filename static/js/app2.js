
// Create chart generator function
function generateCharts(sample){
    d3.json("https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json").then((data) => {
        let samples = data.samples;
        let resultsArray = samples.filter((sampleDictionary) => sampleDictionary.id == sample);
        let result = resultsArray[0];

        // set values
        let sampleValues = result.sample_values;
        let otuIDs = result.otu_ids;
        let otuLabels = result.otu_labels;

        // Bubblechart setup
        let bubbleLayout = {
            title: "Bacteria Cultures Per Sample",
            margin: {t: 0},
            hovermode: "closest",
            xaxis: {title: "OTU ID"},
            margin: {t: 30}
        };

        let bubbleData = [
            {
                x: otuIDs,
                y: sampleValues,
                text: otuLabels,
                mode: "markers",
                marker: {
                    size: sampleValues,
                    color: otuIDs,
                    colorscale: "Earth"        
                }
            }

        ]
        // Generate bubble chart
        Plotly.newPlot("bubble", bubbleData, bubbleLayout);

        // Bar chart setup
        let yticks = otuIDs.slice(0,10).map(otuID => `OTU ${otuID}`).reverse();
        let barData = [
            {
                x: sampleValues.slice(0,10).reverse(),
                y: yticks,
                text: otuLabels.slice(0,10).reverse(),
                type: "bar",
                orientation: "h"

            }
        ]

        let barLayout = {
            title: "Top 10 Bacteria Cultures Found",
            margin: {t: 30, l: 150}
        }

        // Generate bar chart
        Plotly.newPlot("bar", barData, barLayout);
    });
}

// Create metadata function
function generateMetadata(sample){
    d3.json("https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json").then((data) => {
        let metadata = data.metadata;

        let resultsArray = metadata.filter(sampleDictionary => sampleDictionary.id == sample);

        let result = resultsArray[0];

        let PANEL = d3.select("#sample-metadata");

        // clear results
        PANEL.html("");

        for(key in result) {
            PANEL.append("h6").text(`${key.toUpperCase()}: ${result[key]}`)
        }


        // Generate Gauge chart -- via bonus.js
        generateGauge(result.wfreq);

    })

}


// Create initialize function
function init(){
    let selector = d3.select("#selDataset");

    // call API
    d3.json("https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.1/14-Interactive-Web-Visualizations/02-Homework/samples.json").then((data) =>{
        // console.log(data.names);
        let sampleNames = data.names;

        // loop through and generate option links from dataset
        for(let index = 0; index < sampleNames.length; index++){
            selector.append("option").text(sampleNames[index]).property("value", sampleNames[index]);
            
        }
        let sampleOne = sampleNames[0];
        generateCharts(sampleOne);
        generateMetadata(sampleOne);

    })

}

// Create function to change options / data via dropdown

function optionChanged(newSample){
    generateCharts(newSample);
    generateMetadata(newSample);
}


// Call intialize function
init();