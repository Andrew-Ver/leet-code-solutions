'''
    https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
'''


from collections import defaultdict

def maximumSum(nums: list[int]) -> int:
    max_digit_sums = defaultdict(int)
    ans: int = -1
    
    for n in nums:
        '''
            If current digit sum has been seen before, 
            check if largest found so far
        '''
        digit_sum: int = sum(int(s) for s in str(n))
            
        if (digit_sum in max_digit_sums):
            ans = max(ans, n+max_digit_sums[digit_sum])
            
        max_digit_sums[digit_sum] = max(n, max_digit_sums[digit_sum])
    
    return ans if ans != 0 else -1

assert maximumSum(nums = [18,43,36,13,7]) == 54
assert maximumSum(nums = [10,12,19,14]) == -1
