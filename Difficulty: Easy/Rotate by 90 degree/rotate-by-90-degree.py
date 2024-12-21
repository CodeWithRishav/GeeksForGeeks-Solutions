#User function Template for python3


class Solution:

    #Function to do transpose of mat.
    def transpose(self, mat, n):
        R, C = n, n
        for i in range(R):
            for j in range(i, C):

                #swapping elements at (i,j) and (j,i).
                t = mat[i][j]
                mat[i][j] = mat[j][i]
                mat[j][i] = t

    #after transposing we swap elements of each column (1st with last, 2nd with
    #second last) one by one for finding left rotation of mat by 90 degree.
    def reverseColumns(self, mat, n):
        C = n
        R = n
        for i in range(C):
            j = 0
            k = C - 1
            while j < k:

                #swapping elements in each column.
                t = mat[j][i]
                mat[j][i] = mat[k][i]
                mat[k][i] = t
                j += 1
                k -= 1

    #Function to rotate mat anticlockwise by 90 degrees.
    def rotateby90(self, mat):
        n = len(mat)
        self.transpose(mat, n)
        self.reverseColumns(mat, n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        n = int(data[index])
        index += 1
        matrix = []
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.rotateby90(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()

        print("~")

# } Driver Code Ends