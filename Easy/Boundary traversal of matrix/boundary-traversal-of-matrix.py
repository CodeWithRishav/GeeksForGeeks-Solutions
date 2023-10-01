class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        output = []
        
        #base case if number of row or column is 1 then adding all elements.
        if(n == 1):
            i = 0;
            while i < m:
                output.append(matrix[0][i])
                i+=1
        elif(m == 1):
            i = 0;
            while i < n:
                output.append(matrix[i][0])
                i+=1
        else:
            
            #we take care of fact that we don't add any number multiple times.
            
            #traversing first row and adding elements in the list.
            row_ind = 0
            col_ind = 0
            while col_ind < m:
                output.append(matrix[row_ind][col_ind])
                col_ind+=1
    
            #traversing last column and adding elements in the list.
            col_ind = m-1
            row_ind += 1
            while row_ind < n:
                output.append(matrix[row_ind][col_ind])
                row_ind += 1
    
            #traversing last row and adding elements in the list.
            row_ind = n-1
            col_ind -= 1
            while col_ind > -1:
                output.append(matrix[row_ind][col_ind])
                col_ind -= 1
    
            #traversing first column and adding elements in the list.
            col_ind = 0
            row_ind -= 1
            while row_ind > 0:
                output.append(matrix[row_ind][col_ind])
                row_ind -= 1
    
        #returning the list.
        return output

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends