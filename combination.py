import operator as op #사칙연산을 해주는 모듈
from functools import reduce #누적연산을 해주는 함수

def combination(n, r):
    r = min(r, n-r)
    numerator = reduce(op.mul, range(n, n-r, -1), 1)
    denominator = reduce(op.mul, range(1, r+1), 1)
    return numerator // denominator

if __name__ == '__main__':
    n, r = map(int, input().split())
    print(combination(n, r))