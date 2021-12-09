import sys
from random import randint

from ..math import *


# How to runnning the tests:
# $ cd ...
# $ python3 -m library.test.test_math

test_m = randint(1, 1000)
test_n = randint(1, 1000)
test_list = [randint(1, 1000) for _ in range(10)]
print("test_m =", test_m)
print("test_n =", test_n)
print("test_list :", test_list)

# n進数変換
n_conversion = base_n(test_n, 7)
if base_10(n_conversion, 7) == test_n:
    print("test success")
else:
    print("test failed")
    sys.exit()

# 最大公約数
gcd_mn = gcd(test_n, test_m)
print("gcd_mn =", gcd_mn)

# 最大公約数（リスト）
gcd_list_res = gcd_list(test_list)
print("gcd_list_res =", gcd_list_res)

# 最小公倍数
lcm_mn = lcm(test_n, test_m)
print("lcm_mn =", lcm_mn)
