"""
5. Rewrite the last assignment statement in the following interactive sequence so that it behaves identically but uses tuple unpacking instead of tuple slicing.
"""
a = (1, 2, 3, 4, 5, 6, 7, 8)
print(a)
s = _, _, *s, _, _ = a
print(s)
