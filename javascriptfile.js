function getchar(){
  ajaxGetRequest("/piechart", mypie);
  ajaxGetRequest("/barchart", mybar);
}

function getHourData(){
  let valinbox = document.getElementById("hour").value;
  let dict = {"hour": valinbox};
  let jsonpack = JSON.stringify(dict);
  ajaxPostRequest("/linegraph", jsonpack, myline);
}

function mypie(dicte){
  let usedict = JSON.parse(dicte);
  values = [];
  labels = [];
  let listofkeys = Object.keys(usedict);
  for (let key of listofkeys) {
    labels.push(key);
    values.push(usedict[key]);
  }
  let data = [{values: values, labels: labels, type: "pie"}];
    
  var layout = {
    title: "Incidents by day of the week",
    height: 400,
    width: 500
  };

  Plotly.newPlot('piechart', data, layout);
}

function mybar (dicte) {
  let usedicte = JSON.parse(dicte);
  let xaxs = [];
  let yaxs = [];
  let listofyears = Object.keys(usedicte);
  for (let year of listofyears) {
    xaxs.push(year);
    yaxs.push(usedicte[year]);
  }
  let data = [{x: xaxs, y: yaxs, type: 'bar'}];

  var layout = { title: "Incidents by Date", xaxis: {title: "Year"}, yaxis: {title: "# of Incidents"} };
    
  Plotly.newPlot('barchart', data, layout);
}

function myline (dicte) {
  let titleval = document.getElementById("hour").value;
  let usedict = JSON.parse(dicte);
  let xvals = [];
  let yvals = [];
  let listofkeys = Object.keys(usedict);
  for (let key of listofkeys) {
    xvals.push(key);
    yvals.push(usedict[key]);
  }
  var trace = {x: xvals, y: yvals, type: 'scatter'};

  var layout = {title: "# of Incidents at " + titleval + " hours", xaxis: {title: "Year"}, yaxis: {title: "# of Incidents"}};


  Plotly.newPlot('linegraph', [trace], layout);
}



