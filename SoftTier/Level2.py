# 배낭
def fractional_knapsack(W, N, items):
    # 무게당 가치를 기준으로 내림차순 정렬
    items.sort(key=lambda x: x[1]/x[0], reverse=True)

    total_value = 0  # 배낭에 담을 수 있는 총 가치
    for weight, value in items:
        if W >= weight:
            # 배낭에 아이템을 전부 담을 수 있으면 전부 담고, W 감소
            total_value += value
            W -= weight
        else:
            # 배낭에 부분적으로만 담을 수 있으면 해당 부분만큼의 가치만 추가
            total_value += (value/weight) * W
            break  # 배낭이 꽉 찼으므로 반복문 종료

    return total_value

# 입력 받기
W, N = map(int, input().split())  # 배낭의 무게와 귀금속 종류의 수
items = []
for _ in range(N):
    weight, value_per_weight = map(int, input().split())
    items.append((weight, value_per_weight * weight))  # (무게, 총 가치)

# 가장 값비싼 가격 계산
max_value = fractional_knapsack(W, N, items)
print(max_value)
