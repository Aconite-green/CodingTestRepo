import sys



def count_recolor(board, start_row, start_col):
    white, black = 'W', 'B'

    start_color_w, start_color_b = 0,0

    for i in range(8):
        for j in range(8):
            # same color 
            if (i+j)%2==0:
                if board[start_row + i][start_col+j] != white:
                    start_color_w+=1
                elif board[start_row + i][start_col+j] != black:
                    start_color_b+=1
            else:
                if board[start_row + i][start_col+j] == white:
                    start_color_w+=1
                elif board[start_row + i][start_col+j] == black:
                    start_color_b+=1
    
    return min(start_color_b, start_color_w)

def get_min_recolor(board, N, M):

    min_color = float('inf')

    for i in range(N-7):
        for j in range(M-7):

            result = count_recolor(board, i, j)

            if min_color > result:
                min_color=result
    
    return min_color

N, M = map(int, input().split())

chess_board = [sys.stdin.readline().strip() for _ in range(N)]

print(get_min_recolor(chess_board, N, M))