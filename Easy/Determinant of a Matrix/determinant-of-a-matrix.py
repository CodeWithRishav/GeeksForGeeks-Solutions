class Solution:
    
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,matrix,n):

        def determinant(matrix):
            n = len(matrix)

            if n == 1:
                return matrix[0][0]

            det = 0
            for i in range(n):
                cofactor = matrix[0][i] * ((-1) ** i) * determinant(get_minor(matrix, 0, i))
                det += cofactor
            return det

        def get_minor(matrix, row, col):
            return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]

        return determinant(matrix)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends