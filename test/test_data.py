import sys
from random import randint

from ..data_structure_lib import *


def init():
    test_m = randint(1, 1000)
    test_n = randint(1, 1000)
    test_list = [randint(1, 1000) for _ in range(100)]
    print("test_m =", test_m)
    print("test_n =", test_n)
    # print("test_list :", test_list)
    print("---")
    return test_m, test_n, test_list


# 二分探索
def test_binsearch(test_list, key):
    res = bin_search(test_list, key)
    if res == -1:
        if key not in test_list:
            print("key not in list")
            print("bin_search test success")
        else:
            print("key in list")
            print("bin_search test failed")
            sys.exit()
    else:
        test_list.sort()
        if test_list[res] == key:
            print("key in list")
            print("bin_search test success")
        else:
            print("incorrect index")
            print("bin_search test failed")
            sys.exit()

def main():
    """
    # How to runnning the tests:
    # $ cd ...
    # $ python3 -m library.test.test_math
    """
    
    test_m, test_n, test_list = init()
    test_binsearch(test_list, test_n)
    
    print("---")
    print("All tests passed")


if __name__ == '__main__':
    main()
