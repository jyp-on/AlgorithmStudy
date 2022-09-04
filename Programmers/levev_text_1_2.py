def solution(numbers):
    answer = -1
    numbers.sort()


    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = 0

    for i in a:
        if i in numbers:
            continue
        else:
            res += i


    answer = res
    return answer