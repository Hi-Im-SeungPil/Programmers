def solution(s):
    answer = ""
    s = s.upper()
    array = list(s)
    count = 1
    for i in range(len(array)):
        count += 1
        if array[i] != " " and count % 2 != 0:
            array[i] = array[i].lower()
        elif array[i] == " ":
            count = 1
        answer += array[i]
    return answer

print(solution("try hello worlD"))

# a = ["sd"]
# a[0][1].upper()
# print(a)