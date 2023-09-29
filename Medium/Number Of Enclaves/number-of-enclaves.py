import sys
from typing import List
sys.setrecursionlimit(10**8)

#recursive function to perform depth-first search
def dfs(i, j, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
        return
    
    #mark the current cell as visited (0)
    grid[i][j] = 0
    dfs(i + 1, j, grid)
    dfs(i, j + 1, grid)
    dfs(i, j - 1, grid)
    dfs(i - 1, j, grid)

class Solution:
    #function to calculate the number of enclaves
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        #perform DFS on boundary cells
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0 or i == n - 1 or j == m - 1 and grid[i][j] == 1:
                    dfs(i, j, grid)
        
        #count the remaining enclaves
        count = 0
        for i in range(n):
            for j in range(m):
                count += grid[i][j]

        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends