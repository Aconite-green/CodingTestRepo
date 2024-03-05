N = int(input())

def find_layer(N):
    if N == 1:
        return 1
    layer = 1
    count = 1
    while True:
        count += layer*6
        if N <= count:
            return layer+1
        layer += 1

print(find_layer(N))


