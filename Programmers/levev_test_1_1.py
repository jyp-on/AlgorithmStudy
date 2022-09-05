def solution(s):
    answer = True

    if (len(s) == 4) or (len(s) == 6):
        answer = True
    else:
        answer = False

    if s.isnumeric() == True:
        pass
    else:
        answer = False

    return answer