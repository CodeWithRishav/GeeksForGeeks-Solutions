def booleanMatrix(matrix):
    
    R = len(matrix)
    C = len(matrix[0])
    
    #using two list to keep track of the rows and columns 
    #that needs to be updated with 1.
    row = [0] * R  
    col = [0] * C  

    for i in range(0, R) :         
        for j in range(0, C) :
            
            #if we get 1 in matrix, we mark ith row and jth column as 1.
            if (matrix[i][j] == 1) : 
                row[i] = 1
                col[j] = 1
              
    for i in range(0, R) : 
        for j in range(0, C): 
            
            #if ith row or jth column is marked as 1, then all elements
            #of matrix in that row and column will be 1.
            if ( row[i] == 1 or col[j] == 1 ) : 
                matrix[i][j] = 1
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends