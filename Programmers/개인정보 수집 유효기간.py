def solution(today, terms, privacies):

    answer = []

    today = list(map(int, today.split('.')))

    today_year = int(today[0])
    today_month = int(today[1])
    today_day = int(today[2])

    today_sum = 0

    today_sum += today_year * 28 * 12
    today_sum += today_month * 28
    today_sum += today_day

    terms_dic = {}

    for term in terms:
        string = term.split(' ')[0]
        mon = term.split(' ')[1]
        terms_dic[string] = mon

    for idx, privacy in enumerate(privacies, start=1):
        date_sum = 0
        date = (privacy.split(' ')[0])
        code = privacy.split(' ')[1]

        date_sum += int(date.split('.')[0]) * 12 * 28
        date_sum += int(date.split('.')[1]) * 28 + int(terms_dic[code]) * 28
        date_sum += int(date.split('.')[2])

        if today_sum >= date_sum:
            answer.append(idx)






    return answer

print(solution('2022.05.19', ['A 6', 'B 12', 'C 3'], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))