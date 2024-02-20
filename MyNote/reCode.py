def count_recolor(board, start_row, start_col):
    # 체스판의 시작 위치에서 8x8 크기의 부분을 확인하여 다시 칠해야 하는 최소 사각형의 수를 계산하는 함수

    color1, color2 = ('W', 'B')
    # 체스판을 이루는 두 가지 색상을 정의합니다.

    recolor_count1 = recolor_count2 = 0
    # 첫 번째 색상으로 시작할 경우와 두 번째 색상으로 시작할 경우 각각 다시 칠해야 할 사각형의 수를 카운트하는 변수를 초기화합니다.

    for i in range(8):
        for j in range(8):
            # 8x8 크기의 체스판을 순회합니다.

            if (i + j) % 2 == 0:
                # 짝수 위치에 있는 경우(체스판에서 같은 색이어야 하는 위치)

                if board[start_row + i][start_col + j] != color1:
                    recolor_count1 += 1
                # 첫 번째 색상과 다른 경우, 첫 번째 경우의 카운트를 증가시킵니다.
                
                if board[start_row + i][start_col + j] != color2:
                    recolor_count2 += 1
                # 두 번째 색상과 다른 경우, 두 번째 경우의 카운트를 증가시킵니다.

            else:
                # 홀수 위치에 있는 경우(체스판에서 반대 색이어야 하는 위치)

                if board[start_row + i][start_col + j] != color2:
                    recolor_count1 += 1
                # 첫 번째 색상의 반대 색과 다른 경우, 첫 번째 경우의 카운트를 증가시킵니다.
                
                if board[start_row + i][start_col + j] != color1:
                    recolor_count2 += 1
                # 두 번째 색상의 반대 색과 다른 경우, 두 번째 경우의 카운트를 증가시킵니다.

    return min(recolor_count1, recolor_count2)
    # 두 경우 중 최소값을 반환합니다.

def find_minimum_recolor(board, n, m):
    # 주어진 보드에서 8x8 체스판으로 잘랐을 때, 다시 칠해야 하는 사각형의 최소 개수를 찾는 함수

    min_recolor = float('inf')
    # 최소값을 찾기 위해 min_recolor를 무한대로 초기화합니다.

    for i in range(n - 7):
        for j in range(m - 7):
            # 모든 가능한 8x8 크기의 체스판 위치를 순회합니다.

            recolor = count_recolor(board, i, j)
            # 현재 위치에서 다시 칠해야 하는 사각형의 수를 계산합니다.

            if recolor < min_recolor:
                min_recolor = recolor
                # 현재까지의 최소값보다 작은 경우, 최소값을 업데이트합니다.

    return min_recolor
    # 최종적으로 계산된 최소값을 반환합니다.

n, m = map(int, input().split())
# 사용자로부터 보드의 크기(NxM)를 입력받습니다.

board = [input().strip() for _ in range(n)]
# 보드의 각 행을 입력받아서 리스트로 구성합니다.

print(find_minimum_recolor(board, n, m))
# 계산된 최소 다시 칠하기 개수를 출력합니다.


#################################################################

# 빠른 거듭제곱 알고리즘을 구현하는 함수
def fast_power(base, power, mod):
    result = 1
    while power > 0:
        # power가 홀수일 경우, base를 한 번 더 곱해준다.
        if power % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        power //= 2
    return result

def calculate_hash(string, r, M):
    hash_value = 0
    for i, char in enumerate(string):
        # 문자를 해당하는 숫자로 변환 (a=1, b=2, ..., z=26)
        char_value = ord(char) - ord('a') + 1
        # 빠른 거듭제곱을 사용하여 r^i 계산
        r_power_i = fast_power(r, i, M)
        # 해시 값 계산
        hash_value = (hash_value + char_value * r_power_i) % M
    return hash_value

# 주어진 값
r = 31
M = 1234567891
string = "abc"

# 해시 값 계산 및 출력
hash_value = calculate_hash(string, r, M)
print(f"Hash value of '{string}' is: {hash_value}")




#################################################################


def find_closest_sum(cards, N, M):
    closest_sum = 0
    # 모든 카드 3장의 조합을 탐색합니다.
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                current_sum = cards[i] + cards[j] + cards[k]
                # 현재 합이 M을 넘지 않으면서, 이전에 찾은 합보다 크고 M에 더 가까우면 업데이트합니다.
                if closest_sum < current_sum <= M:
                    closest_sum = current_sum
    return closest_sum

# 사용자 입력을 받습니다.
N, M = map(int, input("카드의 개수와 목표값을 입력하세요 (예: 5 21): ").split())
cards = list(map(int, input(f"{N}장의 카드에 쓰인 숫자를 입력하세요: ").split()))

# 결과를 계산하고 출력합니다.
closest_sum = find_closest_sum(cards, N, M)
print(f"M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합은: {closest_sum}")

