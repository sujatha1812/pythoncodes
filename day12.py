import json

print(json.dumps({"name": "aaa", "age": 30}))#dict
print(json.dumps(["lemon", "bananas"]))#list
print(json.dumps(("apple", "bananas")))#tuple
print(json.dumps("hello"))#string
print(json.dumps(42))#int
print(json.dumps(31.76))#float
print(json.dumps(True))#boolean
print(json.dumps(False))
print(json.dumps(None))#statement
