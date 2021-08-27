import json
o = '{"Type": "Short", "Qno": "1", "Q": "sds svsvsvs"} '
print(o)

k = json.loads(o)
print(k)