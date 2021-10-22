def solution(price, money, count):
    sum = 0
    for i in range(1,count+1):
        sum += (price * i)

    result = money - sum
    if result >= 0:
        return 0
    else:
        return abs(result)

print(solution(3,20,4))