# 各位の和
def n_sum(n):
    return sum(list(map(int, str(n))))


# n進数変換
def base_n(num_10, n):  # num_10: 10進数, n: 基数
    str_n = ''
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return int(str_n[::-1])


# 10進数変換
def base_10(num_n, n):  # num_n: n進数, n: 基数
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
    return num_10


# 最大公約数
def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)


# 最大公約数(リスト)
def gcd_list(l):
    from math import gcd as gcd_list
    return gcd_list(*l)


# 最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


# 階乗
def factorial(n):  # n > 0
    if n == 0:
        return 1
    return n * factorial(n - 1)


# 順列
def permutation(n, r):  # n > 0, r <= n
    return factorial(n) // factorial(n - r)


# 組み合わせ
def cmb(n, r):  # n > 0, r <= n
    return factorial(n) // (factorial(n - r) * factorial(r))


# エラトステネスの篩
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table


# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr


# 約数列挙
def make_divistors(n):
    lower_divistors, upper_divistors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divistors.append(i)
            if i != n // i:
                upper_divistors.append(n // i)
        i += 1
    return lower_divistors + upper_divistors[::-1]


# xのn乗をmで割った余り
def pos(x, n, m):
    if n == 0:
        return 1
    res = pos(x*x % m, n//2, m)
    if n % 2 == 1:
        res = res*x % m
    return res