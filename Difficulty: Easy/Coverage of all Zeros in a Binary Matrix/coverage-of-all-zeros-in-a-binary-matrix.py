#User function Template for python3

class Solution:
    def findCoverage(self, matrix):
# Code here
        n = len(matrix)
        m = len(matrix[0])
        total_coverage = 0
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # Check left
                    if j > 0 and matrix[i][j - 1] == 1:
                        total_coverage += 1
                    # Check right
                    if j < m - 1 and matrix[i][j + 1] == 1:
                        total_coverage += 1
                    # Check up
                    if i > 0 and matrix[i - 1][j] == 1:
                        total_coverage += 1
                    # Check down
                    if i < n - 1 and matrix[i + 1][j] == 1:
                        total_coverage += 1
        
        return total_coverage


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends