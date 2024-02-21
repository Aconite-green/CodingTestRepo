

def fast_power(base, power, mod):
    result = 1
    while power > 0:
        if power %2 == 1:
            result = (result*base) % mod
        base = (base*base)%mod
        power //=2
    
    return result

def get_hash_result(r,M,string):
    result = 0
    
    for i,char in enumerate(string):
        char_value = ord(char) - ord('a') + 1

        hash_value_r = fast_power(r, i, M)

        result = (result + char_value*hash_value_r)%M
    
    return result


L = int(input())
string = input()
r= 31
M = 1234567891

print(get_hash_result(r, M, string))