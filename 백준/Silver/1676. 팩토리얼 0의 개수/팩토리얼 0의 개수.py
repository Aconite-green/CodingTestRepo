def factorial(N):
    if N == 0:
        return 1
    return N * factorial(N-1)

def count_zero(N):
    num = factorial(N)
    count =0
    while True:
        if num %10 == 0:
            num //= 10
            count +=1
        else:
            break
    
    return count


N = int(input())

print(count_zero(N))

        