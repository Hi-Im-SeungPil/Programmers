def solution(x, n):
    if x > 0:
        return list(range(x,x*n+1,x))
    elif x == 0:
        return list(map(int,'0'*n))
    else:
        return list(range(x,x*n-1,x))

print(solution(0,5))