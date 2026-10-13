import json

data={
"employee":{"name":"John", "age":30, "city":"New York"}
}

with open("data.json","w") as f:
    json.dump(data,f)

#basically saying JSON.DUMP data part into file F

