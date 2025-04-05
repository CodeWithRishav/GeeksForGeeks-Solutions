#User function Template for python3

class Solution:

    # A function to check if a given
    # cell (r, c) can be included in DFS
    def isSafe(self, grid, r, c):
        row = len(grid)
        col = len(grid[0])

        # r is in range, c is in range, value is 'L' and not visited
        return (0 <= r < row) and (0 <= c < col) and grid[r][c] == 'L'

    def dfs(self, grid, r, c):
        # Arrays to get 8 neighbors
        rNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        cNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark current cell as visited
        grid[r][c] = 'W'

        # Recur for all 8 neighbors
        for k in range(8):
            newR = r + rNbr[k]
            newC = c + cNbr[k]
            if self.isSafe(grid, newR, newC):  # Check before recursion
                self.dfs(grid, newR, newC)

    def numIslands(self, grid):
        row = len(grid)
        col = len(grid[0])

        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 'L':  # Found an unvisited land cell
                    self.dfs(grid, r, c)  # Mark all connected land
                    count += 1  # Increment island count
        return count


#{ 
 # Driver Code Starts
# Driver code
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input().strip())
        m = int(input().strip())
        grid = [input().strip().split() for _ in range(n)]

        obj = Solution()
        print(obj.numIslands(grid))
        print("~")

# } Driver Code Ends