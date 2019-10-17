import json

a = """
{"a":1,"b":{"list":[]}}
"""

json_a = json.loads(a)
print(json_a)
print(json.dumps(json_a))
