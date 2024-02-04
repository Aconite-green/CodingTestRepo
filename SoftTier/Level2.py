

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

from collections import deque

# 입력 받기
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

block_sizes = []
visited = [[False]*N for _ in range(N)]

# BFS 실행을 위한 방향 벡터
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and not visited[i][j]:
            queue = deque([(i, j)])
            visited[i][j] = True
            count = 0

            while queue:
                x, y = queue.popleft()
                count += 1
                # 상하좌우 탐색
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 1 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

            block_sizes.append(count)

block_sizes.sort()

# 결과 출력
print(len(block_sizes))
for size in block_sizes:
    print(size)

########################################### 지도 자동 구축

import sys

N = int(sys.stdin.readline())
dp = [0] * 16 # N의 최댓값은 15이기 때문에 0단계 ~ 15단계 총 16개 칸 생성
dp[0] = 2 # Start 지점의 한변의 점의 개수 = 2

# N번째 단계의 한 변의 점의 개수는 (N-1번째 점의 개수 + N-1번째 점의 개수-1) 과 같다
for i in range(1,N+1):
    dp[i] = dp[i-1] + (dp[i-1] -1) 

# print(dp) -> 각 단계에서 한 변의 점의 개수
print(dp[N]**2) # 총 점의 개수 = 한 변의 점 개수의 제곱

########################################### GBC
def calculate_speed_violation(N, M, limits, tests):
    max_violation = 0
    limit_index, test_index = 0, 0
    limit_distance, limit_speed = limits[limit_index]
    test_distance, test_speed = tests[test_index]

    while limit_index < N and test_index < M:
        min_distance = min(limit_distance, test_distance)
        speed_difference = test_speed - limit_speed
        max_violation = max(max_violation, speed_difference)

        limit_distance -= min_distance
        test_distance -= min_distance

        if limit_distance == 0:
            limit_index += 1
            if limit_index < N:
                limit_distance, limit_speed = limits[limit_index]

        if test_distance == 0:
            test_index += 1
            if test_index < M:
                test_distance, test_speed = tests[test_index]

    return max(0, max_violation)

# 입력 받기
N, M = map(int, input().split())
limits = [tuple(map(int, input().split())) for _ in range(N)]
tests = [tuple(map(int, input().split())) for _ in range(M)]

# 제한 속도 초과 계산
max_speed_violation = calculate_speed_violation(N, M, limits, tests)
print(max_speed_violation)


########################################### 비밀 메뉴

def check_secret_menu(M, N, secret, operations):
    for i in range(N - M + 1):
        if operations[i:i+M] == secret:
            return "secret"
    return "normal"

# 입력 받기
M, N, K = map(int, input().split())
secret = list(map(int, input().split()))
operations = list(map(int, input().split()))

# 비밀 메뉴 확인
result = check_secret_menu(M, N, secret, operations)
print(result)

########################################### 전광판

# 입력 받기
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    # 각 숫자별로 켜져 있어야 하는 전구의 상태
    digit_state = {
        '0': '1110111', '1': '0010010', '2': '1011101', '3': '1011011', '4': '0111010',
        '5': '1101011', '6': '1101111', '7': '1010010', '8': '1111111', '9': '1111011',
    }

    # 숫자 A를 전광판 상태로 변환
    state_A = ['0'] * 35  # 모든 전구가 꺼진 상태
    A_str = str(A).zfill(5)  # 5자리로 맞춤
    for i, digit in enumerate(A_str):
        for j, val in enumerate(digit_state[digit]):
            state_A[i*7 + j] = val
    state_A = ''.join(state_A)

    # 숫자 B를 전광판 상태로 변환
    state_B = ['0'] * 35  # 모든 전구가 꺼진 상태
    B_str = str(B).zfill(5)  # 5자리로 맞춤
    for i, digit in enumerate(B_str):
        for j, val in enumerate(digit_state[digit]):
            state_B[i*7 + j] = val
    state_B = ''.join(state_B)

    # 스위치를 눌러야 하는 횟수 계산
    switch_presses = sum(1 for a, b in zip(state_A, state_B) if a != b)

    # 결과 출력
    print(switch_presses)

########################################### 회의실 예약

def format_time_range(start, end):
    return f'{start:02d}-{end:02d}'

def find_available_times(N, M, rooms, meetings):
    # 회의실별 예약된 시간대 저장
    reserved_times = {room: [] for room in rooms}
    for meeting in meetings:
        room, start, end = meeting
        reserved_times[room].append((start, end))

    # 각 회의실별로 예약 가능한 시간대 찾기
    results = {}
    for room in rooms:
        reserved = sorted(reserved_times[room])
        available = []
        last_end = 9
        for start, end in reserved:
            if last_end < start:
                available.append(format_time_range(last_end, start))
            last_end = max(last_end, end)
        if last_end < 18:
            available.append(format_time_range(last_end, 18))

        results[room] = available

    return results

# 입력 받기
N, M = map(int, input().split())
rooms = sorted([input() for _ in range(N)])
meetings = [input().split() for _ in range(M)]
meetings = [(meeting[0], int(meeting[1]), int(meeting[2])) for meeting in meetings]

# 예약 가능한 시간 찾기
available_times = find_available_times(N, M, rooms, meetings)

# 출력 형식에 맞게 출력
for room in rooms:
    print(f"Room {room}:")
    if available_times[room]:
        print(f"{len(available_times[room])} available:")
        for time in available_times[room]:
            print(time)
    else:
        print("Not available")
    print("-----")

########################################### X marks the Spot

import sys

# 입력 받기
N = int(sys.stdin.readline().strip())

result = []
for _ in range(N):
    S, T = sys.stdin.readline().strip().split()
    index = S.find('x') if 'x' in S else S.find('X')
    result.append(T[index].upper())

# 결과 출력
print(''.join(result))


########################################### 연탄의 크기

import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
rad_array = map(int, sys.stdin.readline().strip().split())
counts = Counter()


for r in rad_array:
    for j in range(2, r+1):
        if r%j == 0:
            counts[j] += 1

print(max(counts.values()))
            

########################################### 진정한 효도

def min_cost_to_farm(land):
    # 가능한 모든 1 x 3 영역을 탐색
    def get_areas(land):
        areas = []
        # 가로 방향 영역
        for i in range(3):
            areas.append(land[i])
        # 세로 방향 영역
        for j in range(3):
            areas.append([land[i][j] for i in range(3)])
        return areas

    # 주어진 영역의 높이를 동일하게 만드는 데 필요한 비용 계산
    def cost_to_even(area):
        # 각 땅의 높이를 평균 높이로 맞추는 데 필요한 비용 계산
        average_height = round(sum(area) / len(area))
        return sum(abs(h - average_height) for h in area)

    areas = get_areas(land)
    return min(cost_to_even(area) for area in areas)

# 입력 받기
land = [list(map(int, input().split())) for _ in range(3)]

# 최소 비용 계산
result = min_cost_to_farm(land)
print(result)

