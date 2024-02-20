def fast_power(base, power, mod):
    result = 1
    while power > 1:
        if power %2 == 1:
            result = (result *base) % mod
        base = (base*base)%mod
        power //=2
    
    return result



def calculate_hash(string, r, M):
    result = 0

    for i, char in enumerate(string):
        char_value = ord(string[i]) - ord('a')+1

        r_power_i = fast_power(r, i, M)

        result = (result+ char_value*r_power_i)


r = 31
M = 1234567891

L = int(input())
string = input()

