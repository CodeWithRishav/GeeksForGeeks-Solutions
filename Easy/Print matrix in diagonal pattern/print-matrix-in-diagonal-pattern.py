# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        if not mat:
            return []
    
        result = []
        numRows, numCols = len(mat), len(mat[0])
        row, col = 0, 0
        direction = 1  # 1 for upward, -1 for downward
    
        while row < numRows and col < numCols:
            result.append(mat[row][col])
    
            # Moving diagonally upward
            if direction == 1:
                if col == numCols - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            # Moving diagonally downward
            else:
                if row == numRows - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1
    
        return result

#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends