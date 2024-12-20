class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        r = len(mat)
        c = len(mat[0])
        output = []

        row = 0
        col = 0

        while row < r and col < c:
            # storing the elements of 1st row from the remaining rows, in a list.
            for i in range(col, c):
                output.append(mat[row][i])
            row += 1

            # storing elements of last column from remaining columns, in list.
            for i in range(row, r):
                output.append(mat[i][c - 1])
            c -= 1

            # storing the elements of last row from remaining rows, in a list.
            if row < r:
                for i in range(c - 1, col - 1, -1):
                    output.append(mat[r - 1][i])
                r -= 1

            # storing elements of 1st column from the remaining columns, in list.
            if col < c:
                for i in range(r - 1, row - 1, -1):
                    output.append(mat[i][col])
                col += 1

        # returning the list.
        return output

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))
        print("~")

# } Driver Code Ends