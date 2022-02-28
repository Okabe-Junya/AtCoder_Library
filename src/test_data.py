import sys
from math import gcd as gcd_math
from math import factorial as factorial_math
from scipy.special import perm
from scipy.special import comb
from random import randint

import data_structure_lib
import math_lib


# --------------------------------------------------
# data_structure_lib

def init():
    test_m = randint(1, 100)
    test_n = randint(1, 100)
    test_list = [randint(1, 1000) for _ in range(100)]
    return test_m, test_n, test_list


# 二分探索
def test_binsearch():
    _, key, test_list = init()
    res = data_structure_lib.bin_search(test_list, key)
    if res == -1:
        assert key not in test_list
    else:
        assert res == test_list.index(key)


# ダイクストラ法，ワーシャルフロイド法
def test_warshall_floyd():
    assert 1 == 1



# 部分和問題
def test_subset_sum():
    # case1
    test_list1 = [2, 5, 9]
    Sum1 = 11
    res1 = data_structure_lib.subset_sum(test_list1, Sum1)
    assert res1
    
    # case2
    test_list2 = [3, 1, 4, 5]
    Sum2 = 11
    res2 = data_structure_lib.subset_sum(test_list2, Sum2)
    assert not res2


"""
# BST
def test_BST():
    l = [randint(1, 100) for _ in range(20)]
    print("sorted list:", sorted(l))
    tree = data_structure_lib.BST(l)
    if tree.search_min() != min(l):
        print("search_min test failed")
        sys.exit()
    if tree.search_max() != max(l):
        print("search_max test failed")
        sys.exit()
"""



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
