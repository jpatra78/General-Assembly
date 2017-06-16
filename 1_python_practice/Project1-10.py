#Project 1 - Problem 10
#Function that traverses through dictionary

#credit
#http://stackoverflow.com/questions/380734/how-to-do-this-python-dictionary-traverse-and-search

tiered_dict = {'T1.1':'V1.1', 
               'T1.2':'V1.2',
               'T1.3':{'T2.1':'V2.1',
                       'T2.2':['V2.2.1','V2.2.2'],
                       'T2.3':{'T3.1':['V3.1.1','V3.1.2'],
                               'T3.2':'V3.2',
                               'T3.3':'V3.3'}},
               'T1.4':{'T2.4':{'T3.4':{'T4.1':'V4.1',
                                       'T4.2':'V4.2'},
                               'T3.5':{'T4.3':'V4.3'}},
                       'T2.5':['V2.3.1','V2.3.2']},
               }

def traverse_tree(dictionary, id=None):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            traverse_tree(value, id+1,)
        else:
            print '\t %s \t %s' % (key,value) #prints key, value but indentation is off
    return

print traverse_tree(tiered_dict,id=1)

'''
#Experimenting with json.  Not working though
def json_dict(dictionary):
  import json

  with open("my.json","w") as f:
      d = json.dump(dictionary,f)
      return d
    

print json_dict(tiered_dict)
'''