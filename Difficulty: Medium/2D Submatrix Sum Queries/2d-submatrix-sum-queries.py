class Solution:

    def prefixSum2D(self, mat, queries):
        rows, cols = len(mat), len(mat[0])

        # build prefix sum over rows
        for i in range(1, rows):
            for j in range(cols):
                mat[i][j] += mat[i - 1][j]

        # build prefix sum over columns
        for j in range(1, cols):
            for i in range(rows):
                mat[i][j] += mat[i][j - 1]

        result = []

        # process each query using inclusion-exclusion
        for r1, c1, r2, c2 in queries:
            # get the total prefix sum from (0,0) to (r2,c2)
            total = mat[r2][c2]

            # subtract the area to the left of the submatrix (if any)
            left = mat[r2][c1 - 1] if c1 > 0 else 0

            # subtract the area above the submatrix (if any)
            top = mat[r1 - 1][c2] if r1 > 0 else 0

            # add back the top-left overlapping area (subtracted twice)
            overlap = mat[r1 - 1][c1 - 1] if r1 > 0 and c1 > 0 else 0

            # final submatrix sum using inclusion-exclusion
            sum_val = total - left - top + overlap
            result.append(sum_val)

        return result