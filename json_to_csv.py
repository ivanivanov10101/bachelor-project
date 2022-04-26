import json
import glob
import csv

data = []

files = glob.glob('json/*', recursive=True)

for file in files:
  with open(file, 'r') as f:

    try:
      json_file = json.load(f)
      data.append([
        json_file['url'],
        json_file['green'],
        json_file['bytes'],
        json_file['cleanerThan'],
        json_file['statistics']['adjustedBytes'],
        json_file['statistics']['energy'],
        json_file['statistics']['co2']['grid']['grams'],
        json_file['statistics']['co2']['grid']['litres'],
        json_file['statistics']['co2']['renewable']['grams'],
        json_file['statistics']['co2']['renewable']['litres'],
        json_file['timestamp']
      ])
    except KeyError:
      print(f'Skipping {file}')

data.sort()

data.insert(0, ['URL', 'Green Hosting', 'Bytes', 'Cleaner Than %', 'Stats_Adjusted Bytes', 'Stats_Energy', 'Stats_CO2_Grid_Grams', 'Stats_CO2_Grid_Litres', 'Stats_CO2_Renewable_Grams', 'Stats_CO2_Renewable_Litres'])

with open('database.csv', "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Updated CSV")