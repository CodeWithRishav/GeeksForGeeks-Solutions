from collections import deque


class Solution:
    # Check if i, j is within the array
    # limits of row and column
    def isSafe(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def orangesRotting(self, mat):
        n = len(mat)
        m = len(mat[0])

        # all four directions
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # queue to store cell position
        q = deque()

        # find all rotten oranges
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j))

        # counter of elapsed time
        elapsedTime = 0

        while q:
            # increase time by 1
            elapsedTime += 1

            for _ in range(len(q)):
                i, j = q.popleft()

                # change 4-directionally connected cells
                for dir in directions:
                    x = i + dir[0]
                    y = j + dir[1]

                    # if cell is in the matrix and
                    # the orange is fresh
                    if self.isSafe(x, y, n, m) and mat[x][y] == 1:
                        mat[x][y] = 2
                        q.append((x, y))

        # check if any fresh orange is remaining
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    return -1

        return max(0, elapsedTime - 1)

#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends