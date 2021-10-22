# 스테이지 머물러 있는 분
dict = {}

def solution(N, stages):
    answer = []
    # 스테이지 몇명 머물러 있는지 카운트
    count = 0
    #스테이지 몇명 머물러 있는지 카운트 append 할 list
    userStage = []
    for i in range(1,N+2):
        for j in stages:
            if i == j:
                count += 1
        #유저가 있는 스테이지 append
        userStage.append(count)
        count = 0

    sumUserStage = 0

    for i in range(N,-1,-1):
        sumUserStage += userStage[i]
        try:
            dict[i] = userStage[i]/sumUserStage
        except:
            dict[i] = 0

    sorted_dict = sorted(dict.items(),key = lambda item : item[1])

    for i in range(len(sorted_dict)-1,-1,-1):
        print(i)
        if sorted_dict[i][0] != N:
            answer.append(sorted_dict[i][0]+1)

    print(sorted_dict)

    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
#[2, 1, 2, 6, 2, 4, 3, 3]