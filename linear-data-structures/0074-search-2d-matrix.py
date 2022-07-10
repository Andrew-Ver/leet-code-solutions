'''
    https://leetcode.com/problems/search-a-2d-matrix/
'''


import math


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    row: int = 0
        
    while row < len(matrix):
        if target <= matrix[row][-1]:
            low: int = 0
            high: int = len(matrix[row])-1
            #Binary search
            while low <= high:
                mid: int = math.floor((low+high)/2)
                    
                print(f'Current mid: {matrix[row][mid]}')
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    low = mid+1
                elif matrix[row][mid] > target:
                    high = mid-1
        row += 1
        
    return False


print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13))