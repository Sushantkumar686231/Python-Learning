import json

with open ("data.json","r") as f:
    loader=json.load(f)

print(loader)