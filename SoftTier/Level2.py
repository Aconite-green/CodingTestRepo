

########################################### 바이러스

def calculate_virus_count(K, P, N):
    MOD = 1000000007
    
    final_count = K
    exponent = N * 10

    while exponent > 0:
        if exponent % 2 == 1:
            final_count = (final_count * P) % MOD
        P = (P * P) % MOD
        exponent //= 2

    return final_count


K, P, N = map(int, input().split())

final_virus_count = calculate_virus_count(K, P, N)
print(final_virus_count)

########################################### 금고털이이

def fractional_knapsack(W, items):
    
    items.sort(key=lambda x: x[1]/x[0], reverse=True)

    total_value = 0
    for weight, value in items:
        if W >= weight:
           
            total_value += value
            W -= weight
        else:
            
            total_value += (value / weight) * W
            break

    return total_value


W, N = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]


max_value = fractional_knapsack(W, items)
print(max_value)

########################################### 8단 변속

def check_shift_order(shifts):
    if shifts == list(range(1, 9)):
        return "ascending"
    elif shifts == list(range(8, 0, -1)):
        return "descending"
    else:
        return "mixed"


shifts = list(map(int, input().split()))


shift_order = check_shift_order(shifts)
print(shift_order)


########################################### 장애물 인식 프로그램
