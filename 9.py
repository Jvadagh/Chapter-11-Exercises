"""
9. Write a function named zero_sum that accepts any number of integer arguments. The function
should return True if the sum of its arguments is zero; otherwise, it should return False. The call
zero_sum(2, 3, -5), for example, would evaluate to True, since 2 + 3 + −5 = 0. On the other
hand, zero_sum(2, 3, -10, 4) evaluates to False because 2 + 3 + − 10 + 4 = − 1 6= 0.
zero_sum should return True when called with no arguments.
"""


def zero_sum(*arg):
    sum = 0
    for i in arg:
        sum += i
    if sum == 0:
        return True
    else:
        return False


print(zero_sum())
print(zero_sum(1, 2, 3, -6))
print(zero_sum(1, 2, 3, -5))
