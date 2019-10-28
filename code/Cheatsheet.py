import json

stationinformatie = '''
{
    "menu": {
      "id": "file",
      "value": "File",
      "popup": {
        "menuitem": [
          {"value": "New", "onclick": "CreateNewDoc()"},
          {"value": "Open", "onclick": "OpenDoc()"},
          {"value": "Close", "onclick": "CloseDoc()"}
        ]
      }
    }
}
'''

# een Json heeft een paar andere 'namen' voor de objecten er in, en bijv een python True is een json true.
# hieraan kun je als je het print zien of je met een json of een python te maken hebt.

# nodig om de json te kunnen gebruiken.
data = json.loads(stationinformatie)     #maakt Python van een json

# het accessen van bepaalde informatie in de json
print(type(data['menu']['popup']['menuitem']))
print(data)
print("")

#loopen door een json
for item in data['menu']['popup']['menuitem']:
    print(item)
    print(item['value'])
print("")

#editten/deleten van data in een json
del data['menu']['popup']['menuitem'][1]
print(data['menu']['popup']['menuitem'])
data['menu']['popup']['menuitem'].append({"value": "Open", "onclick": "OpenDoc()"})
print(data['menu']['popup']['menuitem'])
print("")

#een nieuwe json maken
new_string = json.dumps(data, indent=2)  #Zet een string om naar een json, en 'format' hem direct om het leesbaar te maken.
other_new_string = json.dumps(data, indent=2, sort_keys=True) # yay alfabetische volgorde!
print(new_string)
print(other_new_string)

