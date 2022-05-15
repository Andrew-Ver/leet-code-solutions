#https://leetcode.com/problems/find-the-k-beauty-of-a-number/

def divisorSubstrings(num: int, k: int) -> int:
    num_str = str(num)
    k_beauty = 0
    for i in range(0, len(num_str)-(k-1)):
        n = int(num_str[i:i+k])
        if n != 0 and (num % n) == 0:
            k_beauty += 1
    
    return k_beauty

print(divisorSubstrings(num=240, k=2))