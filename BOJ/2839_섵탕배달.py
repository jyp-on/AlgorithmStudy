sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0: #2. 5로 나누어떨어지면 전체 설탕을 5kg로 나눈 몫을 가방에 추가한다.
        bag += sugar//5
        print(bag)
        break
    sugar -=3 #1. 5로 나누어떨어지지 않으면 3개씩 줄여나가고 가방엔 3kg 봉지를 추가한다.
    bag += 1
else: #3. 3씩빼면서 5로 안나눠떨어지면 정확하게 나눌수없다는 거임.
    print(-1)





