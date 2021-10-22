def solution(x):
    sum = 0
    array = list(str(x))
    for i in array:
        sum += int(i)
    return True if x % sum == 0 else False

print(solution(18))