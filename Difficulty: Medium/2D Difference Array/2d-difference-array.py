class Solution:

    def applyDiff2D(self, mat, opr):
        n = len(mat)
        m = len(mat[0])

        # diff matrix of size n x m
        diff = [[0] * m for _ in range(n)]

        # apply all operations using 4-point updates
        for q in opr:
            v = q[0]
            r1, c1, r2, c2 = q[1], q[2], q[3], q[4]

            # top-left -> add
            diff[r1][c1] += v
            # top-right -> subtract
            if c2 + 1 < m:
                diff[r1][c2 + 1] -= v
            # bottom-left -> subtract
            if r2 + 1 < n:
                diff[r2 + 1][c1] -= v
            # bottim-right -> add
            if r2 + 1 < n and c2 + 1 < m:
                diff[r2 + 1][c2 + 1] += v

        # row-wise prefix sum
        for i in range(n):
            for j in range(1, m):
                diff[i][j] += diff[i][j - 1]

        # column-wise prefix sum
        for j in range(m):
            for i in range(1, n):
                diff[i][j] += diff[i - 1][j]

        # apply diff to original matrix
        res = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(mat[i][j] + diff[i][j])
            res.append(row)

        return res