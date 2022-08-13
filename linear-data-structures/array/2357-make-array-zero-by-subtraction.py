'''
	https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
'''

def minimumOperations(self, nums: List[int]) -> int:
    ans: int = 0
    subtraction: int = 0
            
    for n in sorted(nums):
        if (n - subtraction) > 0:
            subtraction += (n-subtraction)
            ans += 1
        
    return ans
