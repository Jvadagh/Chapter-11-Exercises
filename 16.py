"""
16. Given the following dictionary:
d = {3:0, 5:1, 10:1, 8:2, 15:4}
Indicate what each of the following code fragments will print:
(a) print(d) ==> Full dictionary will be printed

(b) for x in d:
        print(x) ==> Only keys will be printed

(c) for x in d.keys():
        print(x) ==> Only keys will be printed

(d) for x in d.values():
        print(x) ==> Only values of dictionary will be printed

"""
d = {3:0, 5:1, 10:1, 8:2, 15:4}
# a
print(d)
print('-----------------------')
# b
for x in d:
    print(x)
print('-----------------------')
# c
for x in d.keys():
        print(x)
print('-----------------------')
# d
for x in d.values():
        print(x)