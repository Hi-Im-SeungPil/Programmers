def solution(numbers):
    answer = 0
    sum = 0

    for i in range(10):
        sum = sum + i

    for i in numbers:
        answer = answer + i


    return sum - answer