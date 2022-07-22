'''
	https://leetcode.com/problems/pascals-triangle/
'''

def generate(numRows: int) -> list[list[int]]:
        ans: list[list[int]] = [[1], [1, 1]]
            
        if numRows <= 2:
            return ans[:numRows]
        
        curr: int = 2
        
        while curr < numRows:
            prev_row: list[int] = ans[-1]
            new_row: list[int] = []
                
            for i in range(len(prev_row)-1):
                new_row.append(sum(prev_row[i:i+2]))
            
            ans.append([1] + new_row + [1])
            curr += 1
            
        return ans

assert generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
assert generate(1) == [[1]]
