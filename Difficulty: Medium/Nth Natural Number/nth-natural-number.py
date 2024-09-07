#User function Template for python3

class Solution:

    def findNth(self, n):
        result = 0
        p = 1
        while (n > 0):
            result += (p * (n % 9))
            n = n // 9
            p = p * 10

        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends