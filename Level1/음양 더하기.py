absolutes = [4,7,12]
signs = [True,False,True]

def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        if signs[i] == True:
            signs[i] = 1
        else:
            signs[i] = -1

        answer = answer + (signs[i] * absolutes[i])

    return answer

print(solution(absolutes,signs))