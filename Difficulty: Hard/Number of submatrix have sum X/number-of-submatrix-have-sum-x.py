class Solution:

    def countSquare(self, mat, x):
        res = 0
        n = len(mat)
        m = len(mat[0])

        # Compute row-wise prefix sum
        rowPrefix = [row[:] for row in mat]
        for i in range(n):
            for j in range(1, m):
                rowPrefix[i][j] += rowPrefix[i][j - 1]

        maxSize = min(n, m)

        for size in range(1, maxSize + 1):
            for i in range(m - size + 1):
                j = i + size - 1
                total = 0

                for row in range(size - 1):
                    total += rowPrefix[row][j] - (rowPrefix[row][i - 1]
                                                  if i > 0 else 0)

                for row in range(size - 1, n):
                    total += rowPrefix[row][j] - (rowPrefix[row][i - 1]
                                                  if i > 0 else 0)

                    if total == x:
                        res += 1

                    total -= rowPrefix[row - size + 1][j] - (
                        rowPrefix[row - size + 1][i - 1] if i > 0 else 0)

        return res