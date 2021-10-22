numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]

hand = "left"

location = {1 : [0,0],
            2 : [0,1],
            3 : [0,2],
            4 : [1,0],
            5 : [1,1],
            6 : [1,2],
            7 : [2,0],
            8 : [2,1],
            9 : [2,2],
            0 : [3,1]
            }

def solution(numbers, hand):
    answer = ''

    leftHandLocation = [3, 0]
    rightHandLocation = [3, 2]

    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            leftHandLocation = location[numbers[i]]
            numbers[i] = "L"
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            rightHandLocation = location[numbers[i]]
            numbers[i] = "R"
        elif numbers[i] == 2 or numbers[i] == 5 or numbers[i] == 8 or numbers[i] == 0:
            pressButton = location[numbers[i]]
            ll = abs(leftHandLocation[0] - pressButton[0]) + abs(leftHandLocation[1] - pressButton[1])
            rl = abs(rightHandLocation[0] - pressButton[0]) + abs(rightHandLocation[1] - pressButton[1])

            print(leftHandLocation,rightHandLocation,pressButton)

            if ll == rl and hand == "right":
                rightHandLocation = location[numbers[i]]
                numbers[i] = "R"
            elif ll == rl and hand == "left":
                leftHandLocation = location[numbers[i]]
                numbers[i] = "L"
            elif ll < rl:
                leftHandLocation = location[numbers[i]]
                numbers[i] = "L"
            elif rl < ll:
                rightHandLocation = location[numbers[i]]
                numbers[i] = "R"

    for i in numbers:
        answer = answer + i

    return answer

print(solution(numbers,hand))

# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #

# 2,0 3,2 3,1
# 1 + 1 0 + 1