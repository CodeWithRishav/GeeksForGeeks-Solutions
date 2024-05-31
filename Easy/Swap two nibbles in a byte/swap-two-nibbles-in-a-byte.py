#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        # code here                                                                                                                 
        return (n>>4)+((n&15)*(1<<4))


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends