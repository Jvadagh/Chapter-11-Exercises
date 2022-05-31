"""
13. What happens when an executing program attempts to retrieve a value using a key that is not present
in the dictionary?
None will be assigned to variable
for example:
"""
d = {"Fred": 19, "Javad": 20}
x = d.get("John")
print(x)

