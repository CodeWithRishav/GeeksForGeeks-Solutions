#User function Template for python3

class Solution:
    def multiply_matrices(self, matrix1, matrix2, modulus):
            return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(3)) % modulus for j in range(3)] for i in range(3)]
    
        # Function to exponentiate a matrix
    def exponentiate_matrix(self, matrix, exponent, modulus):
        if exponent == 0:
            return [[(i==j)*1 for j in range(3)] for i in range(3)]
        elif exponent == 1:
            return matrix
        else:
            half_exponent_matrix = self.exponentiate_matrix(matrix, exponent//2, modulus)
            full_exponent_matrix = self.multiply_matrices(half_exponent_matrix, half_exponent_matrix, modulus)
            return self.multiply_matrices(full_exponent_matrix, matrix, modulus) if exponent%2 else full_exponent_matrix

    # Function to generate Fibonacci number
    def genFibNum(self, a, b, c, n, modulus):
        return sum(self.exponentiate_matrix([[a, b, c], [1, 0, 0], [0, 0, 1]], n-2, modulus)[0])%modulus if n > 2 else 1%modulus



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b,c,n,m=map(int,input().split())
        
        ob = Solution()
        print(ob.genFibNum(a,b,c,n,m))
# } Driver Code Ends