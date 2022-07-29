'''
	https://leetcode.com/problems/equal-row-and-column-pairs/
'''


def equalPairs(grid: List[List[int]]) -> int:
	row_sums: dict[str, int] = defaultdict(int)
        col_sums: dict[int, tuple[int]] = defaultdict(lambda: tuple())
        rows: int = len(grid)
        cols: int = len(grid[0])
        
            
        for r in range(len(grid)):
            row_sum: tuple[int] = ()
            for c in range(cols):
                val: int = grid[r][c]
                row_sum += (val,)
                col_sums[c+1] += (val,)
            row_sums[row_sum] += 1
        
        return sum(row_sums[k] * v for k, v in Counter(col_sums.values()).items())
