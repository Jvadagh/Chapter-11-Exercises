"""
8. Write a function named product that computes the product of any number of floating-point arguments;
for example, the call product(2.5, 2, 10.0) would evaluate to 50.0. The function should
return 1 (the identity element for multiplication) if the caller passes no arguments
"""


def product(*nums):
    Product = 1
    for i in nums:
        Product *= i
    return Product


print(product(2.5, 2, 10.0))
print(product())
