"""
14. What happens when an executing program attempts to associate a value with a key that is not present
in the dictionary?
The new key will be added to the dictionary with its value.
"""
d = {"Fred": 19, "Javad": 20}
d["John"] = 35
print(d)