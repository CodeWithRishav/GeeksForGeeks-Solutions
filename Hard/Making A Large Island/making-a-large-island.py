from collections import defaultdict

class Solution:
    def dfs(self, grid, i, j, index):
        n = len(grid)
        if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
            return 0
        grid[i][j] = index
        count = self.dfs(grid, i + 1, j, index) + \
                self.dfs(grid, i - 1, j, index) + \
                self.dfs(grid, i, j + 1, index) + \
                self.dfs(grid, i, j - 1, index)
        return count + 1

    def findNeighbours(self, grid, i, j, s):
        n = len(grid)
        if i > 0:
            s.add(grid[i - 1][j])
        if j > 0:
            s.add(grid[i][j - 1])
        if i < n - 1:
            s.add(grid[i + 1][j])
        if j < n - 1:
            s.add(grid[i][j + 1])

    def largestIsland(self, grid):
        n = len(grid)
        res = 0
        index = 2
        area = defaultdict(int)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[index] = self.dfs(grid, i, j, index)
                    res = max(res, area[index])
                    index += 1
                    

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    s = set()
                    self.findNeighbours(grid, i, j, s)
                    count = 1
                    for k in s:
                        count += area[k]
                    res = max(res, count)

        return res


#{ 
 # Driver Code Starts

class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n,n)
        
        obj = Solution()
        res = obj.largestIsland(grid)
        
        print(res)
# } Driver Code Ends