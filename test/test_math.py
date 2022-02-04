import sys
from math import gcd as gcd_math
from math import factorial as factorial_math
from scipy.special import perm
from scipy.special import comb
from random import randint

from ..math_lib import *


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


# 階乗
def test_factorial(test_n):
    fact_n = factorial(test_n)
    if fact_n == factorial_math(test_n):
        print("factorial test success")
    else:
        print("factorial test failed")
        sys.exit()


# 順列
def test_permutation(test_n, test_m):
    if test_n < test_m:
        test_n, test_m = test_m, test_n
    perm_n_m = permutation(test_n, test_m)
    if perm_n_m == perm(test_n, test_m, exact=True):
        print("permutation test success")
    else:
        print("permutation test failed")
        sys.exit()
        
# 組み合わせ
def test_cmb(test_n, test_m):
    if test_n < test_m:
        test_n, test_m = test_m, test_n
    cmb_n_m = cmb(test_n, test_m)
    if cmb_n_m == comb(test_n, test_m, exact=True):
        print("cmb test success")
    else:
        print("cmb test failed")
        sys.exit()
        
        
# 冪乗の剰余
def test_pos(test_x, test_n, test_m):
    pos_x_n_m = (test_x ** test_n) % test_m
    pos_res = pos(test_x, test_n, test_m)
    if pos_x_n_m == pos_res:
        print("pos test success")
    else:
        print("pos test failed")
        sys.exit()
    

def main():
    """docstring
    # How to runnning the tests:
    # $ cd ...
    # $ python3 -m library.test.test_math
    """
    test_m, test_n, test_list = init()
    test_to_n_base(test_n)
    test_gcd(test_n, test_m, test_list)
    test_lcm(test_n, test_m)
    test_factorial(test_n)
    test_permutation(test_n, test_m)
    test_cmb(test_n, test_m)
    test_pos(randint(1, 1000), test_n, test_m)
    
    print("---")
    print("All tests passed")


if __name__ == "__main__":
    main()
