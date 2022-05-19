'''
    https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
'''


def maxConsecutive(bottom: int, top: int, special: list[int]) -> int:
    length_special = len(special)
    # No special floors
    if not length_special:
        return top-bottom

    max_range_ans = float('-inf')
    special.sort()
    curr_floor = bottom
    curr_special = 0

    while curr_floor <= top:
        if curr_special < len(special):
            max_range_ans = max(max_range_ans, special[curr_special] - curr_floor)
            curr_floor = special[curr_special]+1
            curr_special += 1
        else:
            max_range_ans = max(max_range_ans, (top - curr_floor+1))
            break
        
    return max_range_ans


assert maxConsecutive(bottom = 2, top = 9, special = [4, 6]) == 3
assert maxConsecutive(bottom = 6, top = 8, special = [7,6,8]) == 0
