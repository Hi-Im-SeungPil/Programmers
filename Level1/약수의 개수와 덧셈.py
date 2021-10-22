def solution(left, right):
    sum = 0
    count = 0
    array = list(map(int,range(left,right+1)))
    for i in range(len(array)):
        for j in range(1,array[i]+1):

            if array[i] % j == 0:
                count += 1

        if count % 2 == 0:
            sum += array[i]
        else :
            sum -= array[i]

        count = 0

    return sum

