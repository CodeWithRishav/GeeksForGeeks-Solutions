#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        mod = 10**9+7
        a = 1
        b = 1
        ans = 1
        if n < 3:return 1
        for i in range(3,n+1):
            c=(a+b)%mod
            a=b
            b=c
            ans=((ans*2)%mod+a)%mod
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends