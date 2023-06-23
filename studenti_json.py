import json

with open('body.json', encoding='utf-8') as data:
    seznam_zaku = json.load(data)


print(seznam_zaku.items())  

novy_seznam = {}
for zak, pocet_bodu in seznam_zaku.items():
        if pocet_bodu >= 60:
            novy_seznam [zak] = "Pass"
        else:
             novy_seznam[zak] = "Fail"
print(novy_seznam)

with open('prospech.json', mode='w', encoding='utf-8') as file: 
    json.dump(novy_seznam, file)