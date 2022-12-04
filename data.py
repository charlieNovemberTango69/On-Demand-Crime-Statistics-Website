import json
import urllib.request
import csv

def split_date(date):
  year = int(date[0:4])
  month = int(date[5:7])
  return ([year, month])

def fix_data(lod, k):
  for i in range(len(lod)):
    if (lod[i].get(k, 0) != 0):
      date = split_date(lod[i][k])
      lod[i]["year"] = date[0]
      lod[i]["month"] = date[1]
  return(lod)

def json_loader(url):
  request = urllib.request.urlopen(url)
  request = request.read().decode()
  return (json.loads(request))

def make_values_numeric(strLst, dic):
  for str in strLst:
    for key in dic:
      if (key == str):
        dic[key] = float(dic[key])
  return (dic)

def save_data(lod, keys, filename):
  data = list_gen(lod, keys)
  with open (filename, "w") as f:
    writer = csv.writer(f)
    writer.writerow(keys)
    writer.writerows(data)

def load_data(filename):
  acc = [{}]
  keys = []
  acc2 = {}
  with open (filename) as f:
    reader = csv.reader(f)
    keys = next(reader)
    for line in reader:
      for i in range(len(line)):
        acc2[keys[i]] = line[i]
      acc.append(acc2)
      acc2 = {}
  acc.pop(0)
  return(acc)


def list_dic_gen(list1,list2):
    diclist = []
    l=len(list1)
    for x in list2:
        dic={}
        for i in range(l):
            dic.update({list1[i]:x[i]})
        diclist.append(dic)
    return diclist

print(list_dic_gen(['One','Two'], [['First','Second']]))


def read_values(file_name):
    file = open(file_name, "r")
    read_csv=csv.reader(file)
    next(read_csv)
    csv_to_list=[]
    for row in read_csv:
        csv_to_list.append(row)

    return csv_to_list

def list_gen(list_of_dick, list_ofkeys):
  retlist = []
  for dict in list_of_dick:
      boogalist = []
      for key in list_ofkeys:
          boogalist.append(dict.get(key))
      retlist.append(boogalist)

  print(retlist)
  return retlist
    

def write_values(list_of_lists, filename):
  with open(filename,'a') as fobject:
    writer = csv.writer(fobject)
    for list in list_of_lists:
      writer.writerow(list)

