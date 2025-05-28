class Solution:

    def ValidCorner(self, mat):
        rows = len(mat)
        if rows == 0:
            return False
        columns = len(mat[0])

        # Check all pairs of rows
        for i in range(rows):
            for p in range(i + 1, rows):
                count = 0
                for k in range(columns):
                    if mat[i][k] == 1 and mat[p][k] == 1:
                        count += 1
                if count >= 2:
                    return True
        return False