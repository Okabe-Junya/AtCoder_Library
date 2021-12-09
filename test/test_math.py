import sys
from math import gcd as gcd_math
from random import randint

from ..math_lib import *


# How to runnning the tests:
# $ cd ...
# $ python3 -m library.test.test_math

def init():
    test_m = randint(1, 1000)
    test_n = randint(1, 1000)
    test_list = [randint(1, 1000) for _ in range(10)]
    print("test_m =", test_m)
    print("test_n =", test_n)
    print("test_list :", test_list)
    print("---")
    return test_m, test_n, test_list


# n進数変換
def test_to_n_base(test_n):
    tmp =randint(1, 10)
    n_conversion = base_n(test_n, tmp)
    if base_10(n_conversion, tmp) == test_n:
        print("to_n test success")
    else:
        print("to_n test failed")
        sys.exit()


# 最大公約数
def test_gcd(test_n, test_m, test_list):
    gcd_mn = gcd(test_n, test_m)
    if gcd_mn == gcd_math(test_n, test_m):
        print("gcd test success")
    else:
        print("gcd test failed")
        sys.exit()
    gcd_list_res = gcd_list(test_list)
    if gcd_list_res == gcd_math(*test_list):
        print("gcd_list test success")
    else:
        print("gcd_list test failed")
        sys.exit()


# 最小公倍数
def test_lcm(test_n, test_m):
    lcm_mn = lcm(test_n, test_m)
    if lcm_mn == test_n * test_m // gcd(test_n, test_m):
        print("lcm test success")
    else:
        print("lcm test failed")
        sys.exit()


def main():
    test_m, test_n, test_list = init()
    test_to_n_base(test_n)
    test_gcd(test_n, test_m, test_list)
    test_lcm(test_n, test_m)


if __name__ == "__main__":
    main()
