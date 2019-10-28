import json

with open('test.json') as f:
    data = json.load(f)

#print(json.dumps(data, indent=2))

for station in data['payload']:                 #Want lijsten en dictionaries.
    del station['heeftFaciliteiten']
    del station['heeftVertrektijden']
    del station['heeftReisassistentie']

with open('another_test.json', 'w') as f:
    json.dump(data, f, indent=2)