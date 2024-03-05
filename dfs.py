def dfs(grid, x=1, y=0, moves=0):
    # 마지막 행에 도달했을 때, 현재까지의 이동 횟수 반환
    if y == len(grid)-1:
        return moves

    # 오른쪽, 아래, 왼쪽 이동
    directions = [(1, 1), (0, 1), (-1, 1), (2, 1), (-2,1)]
    min_moves = float('inf')

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 이동 가능한 칸인지 확인 (다음 위치가 유효 범위 내이고, 사람이 없는 경우)
        if 0 <= nx < 3 and 0 <= ny < len(grid) and grid[ny][nx] == 0:
            # 좌우 이동 시 이동 횟수 증가
            current_moves = moves + abs(dx)
            # 다음 위치로 DFS 수행
            next_moves = dfs(grid, nx, ny, current_moves)
            # 최소 이동 횟수 갱신
            min_moves = min(min_moves, next_moves)

    return min_moves

# 사용자 입력 대신 예제 입력으로 테스트
N = 3
grid = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
    
]


# DFS를 사용하여 모든 경로 탐색 후 최소 이동 횟수 계산
min_moves = dfs(grid)
print(f"최소 이동 횟수: {min_moves}")
