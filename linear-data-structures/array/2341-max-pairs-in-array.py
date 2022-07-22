'''
	https://leetcode.com/problems/maximum-number-of-pairs-in-array/
'''

def numberOfPairs(nums: list[int]) -> list[int]:
        nums_count: dict[int, int] = Counter(nums)
        
        pairs: int = 0
        left_over: int = 0
        
        for k, v in nums_count.items():
            d, m = (divmod(v, 2))
            pairs += d
            left_over += m
        
        return [pairs, left_over]
