import os
import json

json_f = open(os.getcwd() + "/ios_caps.json")
#json_f = open('ios_caps.json') # local
desired_cap = json.load(json_f)
json_f.close()


print(desired_cap)
