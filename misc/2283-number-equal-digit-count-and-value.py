'''
    https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
'''

from collections import Counter


def digitCount(num: str) -> bool:
    num_counter = Counter(num)
    
    for i, n in enumerate(num):
        if num_counter[str(i)] != int(n):
            return False
    
    return True
    