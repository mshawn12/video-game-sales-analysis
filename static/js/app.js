
// Create chart generator function
// function generateCharts(sample){
//     d3.json("http://127.0.0.1:5000/api/v1.0/completedata").then((data) => {
//         let salesdata = data;
//         for(let index = 0; index < salesdata.length; index++){
//             console.log(salesdata[index].globalsales)
        // let resultsArray = genres.filter((genreDictionary) => genreDictionary.uniqueid == sample);
        // let result = resultsArray[0];

        // // set values
        // let sampleValues = result.globalsales;
        // let otuIDs = result.uniqueid;
        // let otuLabels = result.name;

        // set values
        // let sampleValues = data.globalsales;
        // let otuIDs = data.uniqueid;
        // let otuLabels = data.name;



        // // Bubblechart setup
        // let bubbleLayout = {
        //     title: "Bubble Chart",
        //     margin: {t: 0},
        //     hovermode: "closest",
        //     xaxis: {title: "OTU ID"},
        //     margin: {t: 30}
        // };

        // let bubbleData = [
        //     {
        //         x: otuIDs,
        //         y: sampleValues,
        //         text: otuLabels,
        //         mode: "markers",
        //         marker: {
        //             size: sampleValues,
        //             color: otuIDs,
        //             colorscale: "Earth"        
        //         }
        //     }

        // ]
        // // Generate bubble chart
        // Plotly.newPlot("bubble", bubbleData, bubbleLayout);

//         // Bar chart setup
//         let yticks = otuIDs.slice(0,10).map(otuID => `OTU ${otuID}`).reverse();
//         let barData = [
//             {
//                 x: sampleValues.slice(0,10).reverse(),
//                 y: yticks,
//                 text: otuLabels.slice(0,10).reverse(),
//                 type: "bar",
//                 orientation: "h"

//             }
//         ]

//         let barLayout = {
//             title: "Top 10 Video Games",
//             margin: {t: 30, l: 150}
//         }

//         // Generate bar chart
//         Plotly.newPlot("bar", barData, barLayout);
//     });
// }

// // Create metadata function
// function generateMetadata(sample){
//     d3.json("http://127.0.0.1:5000/api/v1.0/completedata").then((data) => {
//         let metadata = data.genre;

//         let resultsArray = metadata.filter(sampleDictionary => sampleDictionary.id == sample);

//         let result = resultsArray[0];

//         let PANEL = d3.select("#sample-metadata");

//         // clear results
//         PANEL.html("");

//         for(key in result) {
//             PANEL.append("h6").text(`${key.toUpperCase()}: ${result[key]}`)
//         }


// //         // Generate Gauge chart -- via bonus.js
// //         generateGauge(result.wfreq);

//     })

// }


// Create initialize function
// function init(){
//     let selector = d3.select("#selDataset");


    // call API
//     d3.json("http://127.0.0.1:5000/api/v1.0/completedata").then((data) =>{
//         // console.log(data.names);
//         let sampleGenres = data.genre;

//         // loop through and generate option links from dataset
//         for(let index = 0; index < sampleGenres.length; index++){
//             selector.append("option").text(sampleGenres[index]).property("value", sampleGenres[index]);
            
//         }
//         let sampleOne = sampleNames[0];
//         generateCharts(sampleOne);
//         generateMetadata(sampleOne);

//     })

// }

// Create function to change options / data via dropdown

function optionChanged(newGenre){
    // generateCharts(newSample);
    // generateMetadata(newSample);
    alert(newGenre)
}


// Call intialize function
init();