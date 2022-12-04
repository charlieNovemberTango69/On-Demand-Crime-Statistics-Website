import bottle
import json
import data 
import process 
import os.path


@bottle.route('/')
def htmlfileasstatic():
  response = bottle.static_file("websiteH.html",root=".")
  return response

@bottle.route('/javascriptfile.js')
def serveupjss():
  response = bottle.static_file("javascriptfile.js",root=".")
  return response

@bottle.route('/ajax.js')
def serveupajax():
  response = bottle.static_file("ajax.js",root=".")
  return response

@bottle.get('/barchart')
def servupbarchar():
  barchartdata = data.load_data("saved_data.csv")
  yeardict = process.generatingadictcounter(barchartdata, "year")
  desireddict = process.remove_min(yeardict, 20)
  response = json.dumps(desireddict)
  return response

@bottle.get('/piechart')
def servuppiechar():
  piechartdata = data.load_data("saved_data.csv")
  daydict = process.generatingadictcounter(piechartdata, "day_of_week")
  response = json.dumps(daydict)
  return response

@bottle.post("/linegraph")
def servelinegraph():
  inputhourval = bottle.request.body.read().decode()
  dictwithinput = json.loads(inputhourval)
  valindict = dictwithinput["hour"]
  linegraphdata = data.load_data("saved_data.csv")
  predata = process.totalmatchlist(linegraphdata, "hour_of_day", valindict)
  procdata= process.generatingadictcounter(predata, "year")
  retvalue = json.dumps(procdata)
  return retvalue
  
  
  

  

def startup():
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.buffalony.gov/resource/d6g9-xbgu.json?$limit=50000'
    info = data.json_loader(url)
    data.fix_data(info,"incident_datetime")
    heads = ['year','month','hour_of_day','incident_type_primary','day_of_week']
    data.save_data(info, heads, csv_file)

startup()
  
bottle.run(host="0.0.0.0", port=8080)