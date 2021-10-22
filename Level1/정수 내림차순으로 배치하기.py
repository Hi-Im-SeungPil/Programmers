def solution(n):
    array = list(map(int,str(n)))
    array.reverse()
    return array

print(solution(100000))