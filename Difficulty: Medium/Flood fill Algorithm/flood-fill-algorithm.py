class Solution:

    def dfs(self, image, x, y, oldColor, newColor):

        # Check boundary conditions and color match
        if (x < 0 or x >= len(image) or y < 0 or y >= len(image[0])
                or image[x][y] != oldColor):
            return

        # Change the color
        image[x][y] = newColor

        # Visit all adjacent pixels
        self.dfs(image, x + 1, y, oldColor, newColor)
        self.dfs(image, x - 1, y, oldColor, newColor)
        self.dfs(image, x, y + 1, oldColor, newColor)
        self.dfs(image, x, y - 1, oldColor, newColor)

    # Function to perform flood fill on the image.
    def floodFill(self, image, sr, sc, newColor):

        # If the starting pixel already has the new color
        if image[sr][sc] == newColor:
            return image

        # Call DFS with the starting pixel's original color
        self.dfs(image, sr, sc, image[sr][sc], newColor)

        return image



#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)

T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    for row in ans:
        print(" ".join(map(str, row)))
    print("~")

# } Driver Code Ends