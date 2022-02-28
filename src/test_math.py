import sys
from math import gcd as gcd_math
from math import factorial as factorial_math
from scipy.special import perm
from scipy.special import comb
from random import randint

import data_structure_lib
import math_lib


def init():
    test_m = randint(1, 100)
    test_n = randint(1, 100)
    test_list = [randint(1, 1000) for _ in range(100)]
    return test_m, test_n, test_list


# n進数変換
def test_to_n_base():
    tmp = randint(1, 10)
    test_n = randint(1, 1000)
    n_conversion = math_lib.nd_conv(test_n, tmp)
    assert math_lib.d_conv(n_conversion, tmp) == test_n


# 最大公約数
def test_gcd():
    test_n, test_m, _ = init()
    gcd_mn = math_lib.gcd(test_n, test_m)
    assert gcd_mn == gcd_math(test_n, test_m)


# 最大公約数（リスト）
def test_gcd_list():
    _, _, test_list = init()
    gcd_list_res = math_lib.gcd_list(test_list)
    assert gcd_list_res == gcd_math(*test_list)


# 最小公倍数
def test_lcm():
    test_n, test_m, _ = init()
    lcm_mn = math_lib.lcm(test_n, test_m)
    assert lcm_mn == test_n * test_m // math_lib.gcd(test_n, test_m)


# 順列
def test_perm():
    test_m = randint(1, 10)
    test_n = randint(1, 10)
    if test_m < test_n:
        test_m, test_n = test_n, test_m
    perm_m_n = math_lib.permutation(test_m, test_n)
    assert perm_m_n == perm(test_m, test_n)


# 階乗
def test_factorial():
    _, test_n, _ = init()
    fact_n = math_lib.factorial(test_n)
    assert fact_n == factorial_math(test_n)


# 組み合わせ
def test_cmb():
    test_m, test_n, _ = init()
    if test_n < test_m:
        test_n, test_m = test_m, test_n
    cmb_n_m = math_lib.cmb(test_n, test_m)
    assert cmb_n_m == comb(test_n, test_m, exact=True)


# 冪乗の剰余
def test_pos():
    test_m, test_n, _ = init()
    test_x = randint(1, 1000)
    pos_x_n_m = (test_x ** test_n) % test_m
    pos_res = math_lib.pos(test_x, test_n, test_m)
    assert pos_x_n_m == pos_res


# 逆元計算
def test_inv():
    test_n, test_m, _ = init()
    if test_n < test_m:
        test_n, test_m = test_m, test_n
    if len(math_lib.make_divistors(test_n)) == 2:
        inv_nm = math_lib.inv(test_n, test_m)
        inv_nm2 = math_lib.ext_gcd(test_n, test_m)[1]
        assert inv_nm == inv_nm2


# 二項係数の剰余
def nck_mod():
    assert 1 == 1

# --------------------------------------------------
# main


def main():
    msg = '''
    This module is test code.
    If you want to run tests, using pytest.
    If you run %pytest in your terminal, 
    all the tests will be executed automatically.
    '''
    print(msg)


if __name__ == '__main__':
    main()
