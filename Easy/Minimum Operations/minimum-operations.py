class Solution:
    #Function to find minimum number of operations required.
    def minOperation(self, n):
        #initialize count to keep track of operations.
        c = 0
        #loop until n is not zero.
        while n != 0:
            #if n is even, divide it by 2.
            if n % 2 == 0:
                n = n // 2
            #if n is odd, subtract 1 from it.
            else:
                n = n - 1
            #increment count.
            c = c + 1
        
        #return the count.
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends