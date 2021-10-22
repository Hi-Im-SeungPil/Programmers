def solution(arr):
    index = arr.index(min(arr))
    arr.pop(index)
    if len(arr) == 0:
        return [-1]
    else:
        return arr

print(solution([10]))