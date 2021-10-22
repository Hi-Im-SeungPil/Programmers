from math import gcd
from math import lcm

def solution(n, m):
    answer = []

    answer.append(gcd(n,m))
    answer.append(lcm(n,m))
    return answer

print(solution(2,5))