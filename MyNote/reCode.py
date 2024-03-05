# 입력 예제
K, N = 4, 11  # 이미 가지고 있는 랜선 개수 K, 필요한 랜선 개수 N
lan_cables = [802, 743, 457, 539]  # 각 랜선의 길이

# 이진 탐색을 이용하여 최대 랜선 길이를 구하는 함수
def max_cable_length(K, N, cables):
    start, end = 1, max(cables)  # 이진 탐색의 시작점과 끝점

    while start <= end:
        mid = (start + end) // 2  # 중간 길이
        num_cables = sum(cable // mid for cable in cables)  # 중간 길이로 잘랐을 때 만들 수 있는 랜선 개수

        if num_cables < N:  # 필요한 랜선 개수보다 적게 만들어지면, 길이를 줄임
            end = mid - 1
        else:  # 필요한 랜선 개수보다 많이 만들어지거나 같으면, 길이를 늘림
            start = mid + 1

    return end  # 최대 랜선 길이 반환

# 예제 입력에 따른 최대 랜선 길이 계산
print(max_cable_length(K, N, lan_cables))




###############################################################3


n = 8  # 수열의 길이
sequence = [4, 3, 6, 8, 7, 5, 2, 1]  # 주어진 수열

def stack_sequence(n, sequence):
    stack = []  # 스택 구현
    result = []  # 결과 저장 (+, -)
    current = 1  # 현재 스택에 push할 숫자

    for num in sequence:
        while current <= num:  # 현재 숫자를 스택에 push
            stack.append(current)
            result.append('+')
            current += 1
        
        if stack[-1] == num:  # 스택의 top이 현재 숫자와 같으면 pop
            stack.pop()
            result.append('-')
        else:  # 만들 수 없는 수열
            return ['NO']

    return result

# 예제 입력에 대한 연산 결과 출력
operations = stack_sequence(n, sequence)
for op in operations:
    print(op)

###############################################################


def find_primes_optimized(M, N):
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:  # i가 소수인 경우
            for j in range(i*i, N+1, i):  # i의 배수들을 소수가 아니라고 표시
                is_prime[j] = False

    # M이상 N이하의 소수 출력
    for i in range(M, N + 1):
        if is_prime[i]:
            print(i)

# 예제 입력에 따라 M이상 N이하의 소수 출력
find_primes_optimized(3, 16)

###############################################################

from collections import deque

def printer_queue_case():
    test_cases = int(input())  # 테스트 케이스의 수 입력 받음
    results = []  # 결과를 저장할 리스트

    for _ in range(test_cases):
        N, M = map(int, input().split())  # 문서의 개수와 궁금한 문서의 위치
        priorities = list(map(int, input().split()))  # 문서의 중요도 리스트
        queue = deque([(value, idx) for idx, value in enumerate(priorities)])  # 중요도와 원래 인덱스를 함께 저장
        print_order = 0  # 인쇄 순서

        while queue:
            # 현재 큐에서 가장 중요도가 높은 문서 찾기
            top_priority = max(queue, key=lambda x: x[0])[0]
            current = queue.popleft()

            if current[0] < top_priority:
                queue.append(current)  # 중요도가 더 높은 문서가 있다면 큐의 끝으로 보냄
            else:
                print_order += 1  # 인쇄 순서 증가
                if current[1] == M:  # 궁금한 문서가 인쇄되었다면
                    results.append(print_order)  # 결과에 추가
                    break

    # 각 테스트 케이스에 대한 결과 출력
    for result in results:
        print(result)

# 이 코드를 실행하려면, 주석을 제거하고 파이썬 환경에서 실행해야 합니다.
# printer_queue_case()


###############################################################
        
from collections import Counter
from statistics import mean, median

def calculate_statistics(numbers):
    # 산술평균
    arithmetic_mean = round(mean(numbers))
    # 중앙값
    median_value = int(median(numbers))
    # 최빈값
    mode_count = Counter(numbers).most_common()
    if len(mode_count) > 1 and mode_count[0][1] == mode_count[1][1]:
        mode_value = sorted([item[0] for item in mode_count if item[1] == mode_count[0][1]])[1]
    else:
        mode_value = mode_count[0][0]
    # 범위
    range_value = max(numbers) - min(numbers)

    return arithmetic_mean, median_value, mode_value, range_value

# 입력 예제
numbers = [1, 3, 8, -2, 2]
statistics = calculate_statistics(numbers)

# 출력
for value in statistics:
    print(value)


###############################################################
    
def sugar_delivery(N):
    # 5kg 봉지의 최대 사용 가능 수
    for five in range(N // 5, -1, -1):
        # 남은 설탕 양이 3kg 봉지로 정확히 나눠떨어지는지 확인
        if (N - (5 * five)) % 3 == 0:
            three = (N - (5 * five)) // 3
            return five + three
    return -1


###############################################################


# 사용자 입력 시뮬레이션 (실제 코드에서는 input() 함수를 사용하여 입력 받음)
# N = int(input())  # 전체 사람 수 입력
# people = [tuple(map(int, input().split())) for _ in range(N)]  # 몸무게와 키 입력

# 가정된 사용자 입력
N = 5
people_input = """
55 185
58 183
88 186
60 175
46 155
"""

# 입력 문자열을 처리하여 몸무게와 키 정보를 리스트에 저장
people = [tuple(map(int, line.split())) for line in people_input.strip().split('\n')]

# 덩치 등수 계산
ranks = [1] * N  # 모든 사람의 초기 덩치 등수를 1로 설정

# 모든 사람에 대해 다른 모든 사람과 비교
for i in range(N):
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ranks[i] += 1  # i번째 사람보다 j번째 사람의 덩치가 더 크다면, i의 등수를 1 증가

ranks


###############################################################
import sys
input = sys.stdin.readline

def round2(num): # 사사오입
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

# 입력
n = int(input())
ban = round2(n*0.15)

if n == 0:
    print(0)
else:
    score = []
    for _ in range(n):
        score.append(int(input()))
    score.sort()
    
    # 출력
    res = 0
    for i in range(ban, n-ban):
        res += score[i]
    res = res/(n-2*ban)
    print(round2(res))


    # 사용자 입력을 받는 코드 (주석 처리하고 예시 입력으로 대체하여 실행)


###############################################################
    

# N, M, B = map(int, input().split())
# ground = [list(map(int, input().split())) for _ in range(N)]

# 예시 입력
N, M, B = 3, 4, 1
ground = [
    [64, 64, 64, 64],
    [64, 64, 64, 64],
    [64, 64, 64, 63]
]

# 가능한 모든 높이에 대해 집터를 그 높이로 맞출 때 필요한 시간과 블록 수를 계산
min_time = float('inf')
best_height = 0

for target_height in range(257):
    time = 0
    inventory = B
    for i in range(N):
        for j in range(M):
            height_diff = ground[i][j] - target_height
            if height_diff > 0:  # 현재 높이가 목표 높이보다 높다면, 블록 제거
                time += 2 * abs(height_diff)
                inventory += abs(height_diff)
            elif height_diff < 0:  # 현재 높이가 목표 높이보다 낮다면, 블록 추가
                time += abs(height_diff)
                inventory -= abs(height_diff)
    
    # 인벤토리에 있는 블록 수가 음수가 아니어야 하며, 계산된 시간이 최소 시간보다 작거나 같을 경우 업데이트
    if inventory >= 0 and time <= min_time:
        min_time = time
        best_height = target_height

(min_time, best_height)
