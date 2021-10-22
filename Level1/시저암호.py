def solution(s, n):

    answer = ""
    s = list(map(ord,s))
    A = ord("A")
    Z = ord("Z")
    a = ord("a")
    z = ord("z")

    for i in range(len(s)):
        if s[i] >= A and s[i] <= Z:
            if s[i] + n > Z:
                s[i] = A + (n-1 - (Z - s[i]))
                answer += chr(s[i])
            else :
                answer += chr(s[i] + n)
        elif s[i] >= a and s[i] <= z:
            if s[i] + n > z:
                s[i] = a + (n-1 - (z - s[i]))
                answer += chr(s[i])
            else :
                answer += chr(s[i] + n)
        elif s[i] == ord(" "):
                answer += " "
    return answer

print(solution("a B z",4))