class Solution:

    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])

        low, high = 0, m - 1

        # binary search on columns
        while low <= high:
            mid = (low + high) // 2

            # find the row with the maximum element in
            # the current column
            maxRow = 0
            for i in range(1, n):
                if mat[i][mid] > mat[maxRow][mid]:
                    maxRow = i

            # get the left and right neighbors
            # treat missing neighbors as -?
            left = mat[maxRow][mid - 1] \
                            if mid > 0 else float('-inf')
            right = mat[maxRow][mid + 1] \
                            if mid + 1 < m else float('-inf')

            # check if the current element is greater than or
            # equal to its neighbors
            if mat[maxRow][mid] >= left \
                    and mat[maxRow][mid] >= right:
                return [maxRow, mid]

            # if right neighbor is greater, move to right half
            elif right > mat[maxRow][mid]:
                low = mid + 1

            # else, move to left half
            else:
                high = mid - 1

        return [-1, -1]