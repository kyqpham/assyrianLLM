import json

with open("data/raw/saao/saa08/catalogue.json") as f:
    catalogue = json.load(f)

print(catalogue.keys())

ids = sorted(catalogue["members"].keys())
print(len(ids))
print(ids[:5])