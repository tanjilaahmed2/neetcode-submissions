class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visit = set()

        def dfs(r,c):
            if (r>=ROW or c>=COL or
                r<0 or c<0 or
                (r,c) in visit or 
                grid[r][c] == 0):
                return 0
            visit.add((r,c))

            return (1+dfs(r+1,c)+dfs(r-1,c) + dfs(r, c+1) +dfs(r,c-1))

        area = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]== 1 and (r,c) not in visit:
                    area = max(area, dfs(r,c))
        return area                    