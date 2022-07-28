'''
    https://leetcode.com/problems/jump-game-ii/
'''

from collections import defaultdict


def jump(nums: list[int]) -> int:
    '''
        Map index to the minimal jumps to the end
    '''
    MIN_LENGTH_FROM_INDICE_TO_END = defaultdict(int)


    def explore(index: int, initial_idx: int, arr: list[int]=nums, end: int=len(nums)-1) -> int:
        s = [(index, 1)]
        shortest_path = float('inf')

        while s:
            idx, path_length = s.pop()

            if (idx + nums[idx] >= end):
                MIN_LENGTH_FROM_INDICE_TO_END[initial_idx] = path_length
                shortest_path = min(shortest_path, path_length)
                
            #only enqueue if current length is less than shortest one found
            elif (path_length <= shortest_path):
                for i in range(idx+1, min(idx+nums[idx]+1, end)):
                    if MIN_LENGTH_FROM_INDICE_TO_END[i]:
                        print(f'We found a path from {i} before.')
                        s.append((i, path_length+MIN_LENGTH_FROM_INDICE_TO_END[i]))
                    else:
                        s.append((i, path_length+1))

        return shortest_path

    shortest_path_to_end = float('inf')
    
    for i in range(0, min(len(nums)-1, nums[0])):
        if MIN_LENGTH_FROM_INDICE_TO_END[i]:
            shortest_path_to_end = min(shortest_path_to_end, 1+MIN_LENGTH_FROM_INDICE_TO_END[i])
        else:
            explore(i, i)
            print(MIN_LENGTH_FROM_INDICE_TO_END)
            shortest_path_to_end = min(shortest_path_to_end, 1+MIN_LENGTH_FROM_INDICE_TO_END[i])


    return shortest_path_to_end


print(jump(nums = [2,3,1,1,4]))
print(jump(nums = [2,3,0,1,4]))

jump(nums = [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5])
