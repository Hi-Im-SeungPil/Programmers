def solution(s):

    a = s.replace("zero","0")
    a = a.replace("one","1")
    a = a.replace("two","2")
    a = a.replace("three","3")
    a = a.replace("four","4")
    a = a.replace("five","5")
    a = a.replace("six","6")
    a = a.replace("seven","7")
    a = a.replace("eight","8")
    a = a.replace("nine","9")

    if a[0] == "0":
        return int(a[1:])
    else:
        return int(a)

print(solution(s))