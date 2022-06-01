"""
23. Given the following initialization statements:
A = {20, 19, 2, 10, 7}
B = {4, 10, 5, 6, 9, 7}
C = {10, 19}
evaluate the following expressions:
(a) A                                  ==> {2, 19, 20, 7, 10}
(b) 20 in A                            ==> True
(c) 20 not in A                        ==> False
(d) A & B                              ==> {10, 7}
(e) A | B                              ==> {2, 4, 5, 6, 7, 9, 10, 19, 20}
(f) C < A                              ==> True
(g) C <= A                             ==> True
(h) C <= B                             ==> False
(i) A <= A                             ==> True
(j) A < A                              ==> False
(k) len(A)                             ==> 5
(l) {x + 2 for x in range(10)}         ==> {2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
(m) {x - 2 for x in A}                 ==> {0, 5, 8, 17, 18}
(n) {x - 2 for x in A if x < 10}       ==> {0, 5}
"""
A = {20, 19, 2, 10, 7}
B = {4, 10, 5, 6, 9, 7}
C = {10, 19}
print(A)
print(20 in A)
print(20 not in A)
print(A & B)
print(A | B)
print(C < A)
print(C <= A)
print(C <= B)
print(A <= A)
print(A < A)
print(len(A))
print({x + 2 for x in range(10)})
print({x - 2 for x in A})
print({x - 2 for x in A if x < 10})

