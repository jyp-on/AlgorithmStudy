from collections import defaultdict

id_list1=["muzi", "frodo", "apeach", "neo"]
id_list2=["con", "ryan"]
report1=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
report2=["ryan con", "ryan con", "ryan con", "ryan con"]
k=2

def solution(id_list, report, k):
    answer = []
    # 중복 신고 제거
    report = list(set(report))

    # user별 신고한 id 저장
    user = defaultdict(set)
    print(user)
    # user별 신고당한 횟수 저장
    cnt = defaultdict(int)

    for r in report:
        # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
        a, b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1

    print(user)
    print(cnt)
    for i in id_list:
        result = 0
        # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer


print(solution(id_list1, report1, k))