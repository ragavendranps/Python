import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

print(type(x))
print(type(y))


# the result is a Python dictionary:
print(y["age"])