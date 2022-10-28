'''
	https://leetcode.com/problems/find-subarrays-with-equal-sum/

	Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.
	
	Return true if these subarrays exist, and false otherwise.
'''

def findSubarrays(nums: list[int]) -> bool:
        from collections import deque
        
        seen_sum: set[int] = set()
        curr: deque[int] = deque(nums[:1], maxlen=2)
            
        for n in nums[1:]:
            curr.append(n)
            s = sum(curr)
            if s in seen_sum:
                return True
            seen_sum.add(s)
                
        return False
