# 数学用ライブラリ

## n進数変換

【概要】

第一引数に与えられた数値を，第二引数に与えられた基数に変換して返す．

【サンプル】

```python
>>> base_n(5, 2)
101

>>> base_n(7, 4)
13
```

## 10進数変換

第一引数に与えられた数値を，10進数に変換して返す．基数は第二引数で与える．

【】

【サンプル】

```python
>>> base_10(101, 2)
5

>>> base_10(13, 4)
7
```

## 最大公約数

【】

【サンプル】

```python
>>> gcd(12, 18)
6

>>> gcd(33, 22)
11
```

```python
>>> gcd_list([12, 18, 6])
6
```

## 最小公倍数

【概要】

【サンプル】

```python
>>> lcm(12, 18)
36

>>> lcm(33, 22)
66
```

```python
>>> lcm_list([12, 18, 6])
36
```

## 階乗

【概要】

【サンプル】

```python
>>> factorial(5)
120

>>> factorial(7)
5040
```

## 順列

【概要】

【サンプル】

```python
>>> permutation(5, 3)
60

>>> permutation(10, 2)
90
```

## 組合せ

【概要】

【サンプル】

```python
>>> cmb(5, 3)
10

>>> cmb(10, 2)
45
```

## エラトステネスの篩

【概要】

【サンプル】

```python
>>> sieve(10)
[False, True, True, False, True, False, True, False, False, False, True], [2, 3, 5, 7]

>>> sieve(5)
([False, True, True, False, True, True], [2, 3, 5])
```

## 素因数分解

【概要】

【サンプル】

```python
>>> factorization(9)
[[3, 2]]

>>> factorization(10)
[[2, 1], [5, 1]]

>>> factorization(48)
[[2, 4], [3, 1]]
```

## 約数列挙

【概要】

【サンプル】

```python
>>> make_divistors(9)
[1, 3, 9]

>>> make_divistors(48)
[1, 2, 3, 4, 6, 8, 12, 16, 24, 48]
```

## 冪乗の剰余

【概要】

【サンプル】

```python
>>> pos(2, 5, 3)
2

>>> pos(10, 4, 100)
0
```