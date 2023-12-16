class Solution:

    def countStr(self, n):
        # calculating the total number of strings for given value of n
        res = 0
        # counting the number of string combinations with only one character
        res += 1 + (n * 2)
        # counting the number of string combinations with two characters using the formula (n*(n*n-1))/2
        res += n * ((n * n) - 1) / 2
        
        return int(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends