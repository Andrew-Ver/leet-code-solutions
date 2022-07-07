'''
	https://leetcode.com/problems/longest-consecutive-sequence/
'''


def longestConsecutive(nums: list[int]) -> int:
    #Convert to set for o(1) lookup
    nums: set[int] = set(nums)
        
    seen: set[int] = set()
    longest: int = 0
    
    for curr_n in nums:
        curr_sequence: set[int] = {curr_n}
        curr: int = curr_n
        
        # Only check if the number hasn't 
        # been previously visited
        if (curr_n not in seen):
            while (curr-1) in nums:
                curr_sequence.add(curr-1)
                seen.add(curr-1)
                curr -= 1
                
            curr: int = curr_n
                
            while (curr+1) in nums:
                curr_sequence.add(curr+1)
                seen.add(curr+1)
                curr += 1
            
        if len(curr_sequence) > longest:
            longest = len(curr_sequence)

    return longest