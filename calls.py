import json
import requests
import csv

sites = []

with open('final.csv', newline='') as inputfile:
    for row in csv.reader(inputfile):
        sites.append(row[0])

api = "https://api.websitecarbon.com/site?url="
for site in sites:
    re = requests.get(api+site)
    r = re.json()
    with open(f'json\\{site}.json', 'w+') as f:
        json.dump(r, f)