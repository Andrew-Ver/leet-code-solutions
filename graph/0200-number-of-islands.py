'''
    https://leetcode.com/problems/number-of-islands/
'''


def numIslands(grid: list[list[str]]) -> int:
    islands_count: int = 0
    seen: set[int] = set()
    rows: int = len(grid)-1
    cols: int = len(grid[0])-1
    
    def search(y: int, x: int) -> None:
        explore: list[int] = [(y, x)]
        
        while explore:
            r, c = explore.pop()
            seen.add((r, c))
            neighbours = [(R, C) for R, C in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                            if (R, C) not in seen and
                            (0 <= R <= rows) and (0 <= C <= cols) and 
                            grid[R][C] == '1']
            explore.extend(neighbours)
        
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in seen and (grid[r][c] == '1'):
                islands_count += 1
                search(y=r, x=c)
    
    return islands_count