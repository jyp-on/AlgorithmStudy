from collections import deque


def solution(bridge_length:int, weight:int, truck_weights:list) -> int:
    ans = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_bridge_weight = 0
    while bridge:
        current_bridge_weight -= bridge.popleft()
        if truck_weights:
            if current_bridge_weight + truck_weights[0] <= weight:
                current_truck = truck_weights.popleft()
                current_bridge_weight += current_truck
                bridge.append(current_truck)
            else:
                bridge.append(0)
        ans += 1
    return ans