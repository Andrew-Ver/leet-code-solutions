'''
    https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
'''


def largestCombination(candidates: list[int]) -> int:
    from collections import defaultdict
    one_bit_count = defaultdict(int)

    for num in candidates:
        binary = bin(num)[2:].zfill(24)
        for i, bit in enumerate(binary):
            if bit == '1':
                one_bit_count[i] += 1

    return max(one_bit_count.values())


print(largestCombination([16, 17, 71, 62, 12, 24, 14]))
print(largestCombination([8, 8]))