import json
data = json.load(open("data.json"))

from difflib import get_close_matches
# help(get_close_matches)
print(get_close_matches("rain",["help","pyrmaid","rain"],3,0.6)) # ['rain']
print(get_close_matches("rain",["help","pyrmaid","rain"])) # ['rain']

print(type(data.keys())) # <class 'dict_keys'>

print(get_close_matches("rainn", data.keys())) # ['rain', 'train', 'rainy']
print(get_close_matches("rainn", data.keys(), n=5)) # ['rain', 'train', 'rainy', 'grain', 'drain']



