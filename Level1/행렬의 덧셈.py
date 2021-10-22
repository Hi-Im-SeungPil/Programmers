def solution(arr1, arr2):
    answer = []
    array = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            array.append(arr1[i][j] + arr2[i][j])
        answer.append(array)
        array = []
    return answer

print(solution([[1],[2]],[[3],[4]]))