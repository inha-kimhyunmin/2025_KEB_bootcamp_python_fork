# Assignment Day 02
# v1.4) Make my_pow custom function instead of ** operator, power function and make it work.
import math


def my_pow(b, e) -> float:
    """
    A user-defined function that receives a base and exponent and returns the power result in the form of a real number
    :param b: base number
    :param e: exponent
    :return: the power result in the form of a real number
    """
    if e < 0:
        b = 1 / b
        e = e * -1

    result = 1

    i = int(e)
    f = e - i

    for _ in range(i):  # for k in range(e):
        result = result * b

    if f > 0:
        result = result * math.exp(f * math.log(b))

    return result


def is_prime(num) -> bool:
    if num >= 2:
        i = 2
        while i <= int(my_pow(num, 0.5)) + 1:
            if num % i == 0:
                return False
            i = i + 1
    else:
        return False
    return True


number = input("First number Second number : ").split()

n1 = int(number[0])
n2 = int(number[1])

if n1 > n2:
    n1, n2 = n2, n1

cnt = 0
while n1 <= n2:
    if is_prime(n1):
        print(f"{n1} ", end='')
        cnt = cnt + 1
    if cnt == 20:
        cnt = 0
        print()
    n1 = n1 + 1
