import json

import yaml
params = {}

with open("./wework.yaml", encoding="utf-8") as f:
    data = yaml.load(f)
    print(json.dumps(data['create'], indent=2))
params["userid"] = "01"
params["mobile"] = "17655515151"
params["name"] = "m01"
params["department"] = 1

print(type(data))

raw_data = json.dumps(data)
print(type(raw_data))
for key, value in params.items():
    print("*******************",key,value)
    raw_data = raw_data.replace("${" + str(key) + "}", str(value))
print(json.loads(raw_data))