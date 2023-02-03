def solution(bridge_length, weight, truck_weights):
    bridge = [0 for _ in range(bridge_length)]
    cnt = 0
    while True:
        temp = 0 # 마지막에 다리에 들어온 weight
        cnt += 1
        if len(truck_weights) == 0:
            cnt += bridge.index(temp)
            return cnt

        if sum(bridge[1:]) + truck_weights[0] <= weight:
            temp = truck_weights[0]
            bridge.append(truck_weights.pop(0))
            bridge.pop(0)
        else:
            bridge.pop(0)
            bridge.append(0)

print(solution(2, 10, [7,4,5,6]))