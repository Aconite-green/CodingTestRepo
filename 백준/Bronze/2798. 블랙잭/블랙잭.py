
def get_cards_sum(N, M, cards):

    clossest_sum = 0
    current_sum = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                current_sum = cards[i]+cards[j]+cards[k]

                if clossest_sum < current_sum <= M:
                    clossest_sum = current_sum

    
    return clossest_sum

N, M = map(int, input().split())

cards = list(map(int, input().split()))

print(get_cards_sum(N, M, cards))