from collections import deque

T = int(input())

def printer_queue(N, M):
    N_array = list(map(int, input().split()))
    printer = deque()
    
    for index, priority in enumerate(N_array):
        printer.append((index, priority))
    
    print_order = 0
    while printer:

        max_priority = max(printer, key=lambda x:x[1])[1]

        current = printer.popleft()

        if max_priority > current[1]:
            printer.append(current)
        else:
            print_order += 1
            if current[0] == M:
                return print_order

for _ in range(T):
    N, M = map(int, input().split())

    print(printer_queue(N, M))

        