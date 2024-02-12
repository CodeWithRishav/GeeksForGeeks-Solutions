#User function Template for python3

class Solution:
    def sequence(self, n):
        # code here
        x = 1
        y = 1
        F = 0
        while(x <= n):
            F1 = 1
            for i in range(x):
                F1 *= y
                y += 1
            x += 1
            F = F + F1
        return F%1000000007


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends