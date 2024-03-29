'use strict';

const plotWidth = 500;
const plotHeight = 500;
const paddingLeft = 50;
const paddingRight = 50;
const paddingTop = 50;
const paddingBottom = 50;

let keys = ['top_sp_ranks', 'second_sp_ranks', 'third_sp_ranks'];

let keysOriginal = ['top_original_pos', 'second_original_pos', 'third_original_pos']

let keyToLabel = {
    top_sp_ranks: "Rank of the supporting fact closest to question.",
    second_sp_ranks: "Rank of the supporting fact second closest to question.",
    third_sp_ranks: "Rank of the supporting fact third closest to question.",
    top_original_pos: "The supporting fact closest to the question in the original text.",
    second_original_pos: "The supporting fact second closest to the question in the original text.",
    third_original_pos: "The supporting fact third closest to the question in the original text.",
}

function makePlot(key, data, aggregate) {
    let d = data[key];

    let size = d.length

    console.log(d);

    let svg = d3.select("body").append("svg").attr('width', plotWidth).attr('height', plotHeight);

    let rankExtent = d3.extent(d);

    let xScale = d3.scaleLinear().domain([0, 50]).nice().range([paddingLeft, plotWidth - paddingRight]);

    let bins = d3.histogram()
        .thresholds(xScale.ticks(40))
        .domain(xScale.domain())(d);

    for (let i = 0; i < bins.length; i++) {
        if (i == 0) {
            bins[i]['aggregate'] = bins[i].length
        } else {
            bins[i]['aggregate'] = bins[i].length + bins[i - 1].aggregate
        }
    }

    console.log(bins);

    let yScale = d3.scaleLinear()
        .domain([0, 1])
        .range([plotHeight - paddingTop, paddingBottom]);

    if (!aggregate) {
        svg.append("g")
            .attr("fill", "steelblue")
            .selectAll("rect")
            .data(bins)
            .join("rect")
            .attr("x", d => xScale(d.x0) + 1)
            .attr("width", d => Math.max(0, xScale(d.x1) - xScale(d.x0) - 1))
            .attr("y", d => yScale(d.length / size))
            .attr("height", d => yScale(0) - yScale(d.length / size));
    } else {
        svg.append("g")
            .attr("fill", "steelblue")
            .selectAll("rect")
            .data(bins)
            .join("rect")
            .attr("x", d => xScale(d.x0) + 1)
            .attr("width", d => Math.max(0, xScale(d.x1) - xScale(d.x0) - 1))
            .attr("y", d => yScale(d.aggregate / size))
            .attr("height", d => yScale(0) - yScale(d.aggregate / size));
    }

    const xAxisTicks = xScale.ticks()
        .filter(tick => Number.isInteger(tick));
    const xAxis = d3.axisBottom(xScale)
        .tickValues(xAxisTicks)
        .tickFormat(d3.format('d'));
    // const yAxisTicks = yScale.ticks()
    //     .filter(tick => Number.isInteger(tick));
    const yAxis = d3.axisLeft(yScale)
        // .tickValues(yAxisTicks)
        .tickFormat(d3.format('.0%'));

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(" + 0 + " ," + (plotHeight - paddingBottom) + ")")
        .call(xAxis);

    svg.append("g")
        .attr("class", "y axis")
        .attr("transform", "translate(" + paddingLeft + " ," + 0 + ")")
        .call(yAxis);

    svg.append("text")
        .attr("style", "font-size:9pt")
        .attr("transform", "translate(" + (plotWidth / 2 - 150) + " ," + (plotHeight - paddingBottom / 2 + 10) + ")")
        .text(keyToLabel[key])
}

// d3.select("body")
//     .append("h2")
//     .text("Histograms of supporting fact rankings. (raw)")

// for (let key of keys) {
//     makePlot(key, dataSp);
// }

// d3.select("body")
//     .append("h2")
//     .text("Histograms of supporting fact rankings. (tfidf)")

// for (let key of keys) {
//     makePlot(key, dataTfidf);
// }

d3.select("body")
    .append("h2")
    .text("Histograms of supporting fact rankings. (tfidf and coref resolution, onetime ranking.)")

// for (let key of keys) {
//     makePlot(key, dataOnetime, false);
// }

for (let key of keys) {
    makePlot(key, dataOnetime, true);
}

d3.select("body")
    .append("h2")
    .text("Histograms of supporting fact rankings. (tfidf and coref resolution, multihop ranking.)")

// for (let key of keys) {
//     makePlot(key, dataMultihop, false);
// }

for (let key of keys) {
    makePlot(key, dataMultihop, true);
}

d3.select("body")
    .append("h2")
    .text("Histograms of supporting fact original positions.")

// for (let key of keysOriginal) {
//     makePlot(key, dataOriginal, false)
// }

for (let key of keysOriginal) {
    makePlot(key, dataOriginal, true)
}