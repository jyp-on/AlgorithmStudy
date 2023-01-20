
def solution(survey, choices):
    answer = ''
    text = 'RTCFJMAN'
    dic = {}

    for t in text:
        dic[t] = 0

    for i, item in enumerate(survey):
        dic[item[0]] = 0
        dic[item[1]] = 0

    for i, item in enumerate(survey):
        if choices[i] != 4:
            if choices[i] <= 3:
                dic[item[0]] += 4 - choices[i]
            else:
                dic[item[1]] += choices[i] - 4

    sort_dic = sorted(dic.items(), key=lambda x:x[1])
    sort_dic = dict(sort_dic)

    if sort_dic['R'] >= sort_dic['T']:
        answer += 'R'
    else:
        answer += 'T'

    if sort_dic['C'] >= sort_dic['F']:
        answer += 'C'
    else:
        answer += 'F'

    if sort_dic['J'] >= sort_dic['M']:
        answer += 'J'
    else:
        answer += 'M'

    if sort_dic['A'] >= sort_dic['N']:
        answer += 'A'
    else:
        answer += 'N'



    return answer


def solution2(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}

    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            A = A[::-1]
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        if my_dict[name] > 0:
            result += name[1]
        elif my_dict[name] < 0:
            result += name[0]
        else:
            result += sorted(name)[0]

    return result

# print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
# print(solution(["TR", "RT", "TR"], [7, 1, 3]))


print(solution2(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution2(["TR", "RT", "TR"], [7, 1, 3]))
