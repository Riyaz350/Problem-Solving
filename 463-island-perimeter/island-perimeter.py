class Solution(object):
    def islandPerimeter(self, grid):
        m, n, param = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                param +=4*grid[i][j]
                if i>0: param-=grid[i][j]*grid[i-1][j]
                if i<m-1: param-=grid[i][j]*grid[i+1][j]
                if j>0: param-=grid[i][j]*grid[i][j-1]
                if j<n-1: param-=grid[i][j]*grid[i][j+1]
        return param
        