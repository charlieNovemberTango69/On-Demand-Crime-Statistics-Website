def gen_dictionary (listofdict, keyasstrng):
  ret_dict = {}
  for individual_dict in listofdict:
    if keyasstrng in individual_dict:
      v = individual_dict[keyasstrng]
      ret_dict[v] = 0
    else:
      continue
      
      
  return ret_dict



def total_matches(lod,k,v):
  list=[]
  for i in lod:
    if i[k]==str(v):
      list.append(i)
    
  retval=generatingadictcounter(list,'year')
  return retval


def total_matches_specific (lod, k, v, k2, v2):
  ret_var = 0
  for dict_in_lod in lod:
    if (k in dict_in_lod) and (k2 in dict_in_lod):
      g = dict_in_lod[k]
      p = dict_in_lod[k2]
      if g == v and p == v2:
        ret_var = ret_var + 1
      else:
        continue
    else:
      continue
  return ret_var


def remove_min (dictionaryinuse, minvalint):
  ret_dict1 = {}
  for keyss in dictionaryinuse:
    if dictionaryinuse[keyss] > minvalint:
      ret_dict1[keyss] = dictionaryinuse[keyss]
  return ret_dict1
  
#data processing for part 4



def generatingadictcounter (lod, strng):
  retdict = {}
  for dict in lod:
    innerval = dict[strng]
    if retdict.get(innerval, 0) == 0:
      retdict[innerval] = 1
    else:
      retdict[innerval] = retdict[innerval] + 1
  return retdict

def totalmatchlist (lod, k, v):
  retlist = []
  for dict in lod:
    if dict[k] == str(v):
      retlist.append(dict)

  return retlist
    
  
  

