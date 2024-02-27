import sys

def is_sosu(num_array):
    count = 0
    
    for num in num_array:
        if num == 1:
            continue
        
        is_sosu = True
        for i in range(2, num):
            if num % i == 0:
                is_sosu = False
            
        if is_sosu : 
            count +=1
    return count

N = int(input())

num_array = list(map(int, sys.stdin.readline().split()))

print(is_sosu(num_array))