class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROW = len(grid)
        COL = len(grid[0])
        seen = set()

        def dfs(r,c):
            if (r<0 or c<0 or
                r>=ROW or c>=COL or
                grid[r][c] == "0" or
                (r,c) in seen):
                return 
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        island = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r,c) not in seen:
                    dfs(r,c)
                    island += 1
        return island            

        