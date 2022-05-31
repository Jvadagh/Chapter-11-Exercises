"""
7. Consider the tuple tpl defined as tpl = 7, 10, -3, 18, 6, 10
Provide one assignment statement that uses tuple unpacking to assign x to the first element and y to
the last element."""

tpl = (7, 10, -3, 18, 6, 10)
(x, _, _, _, _, y) = tpl
print(tpl)
print(x)
print(y)

