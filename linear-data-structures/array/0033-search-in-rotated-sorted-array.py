'''
    https://leetcode.com/problems/search-in-rotated-sorted-array/
'''


def search(nums: list[int], target: int) -> int:
    i: int = 0
    j: int = len(nums)-1
        
    while i <= j:
        if nums[i] == target:
            return i
        elif nums[j] == target:
            return j
        
        i += 1
        j -= 1
        
    return -1