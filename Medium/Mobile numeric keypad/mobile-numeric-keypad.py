#User function Template for python3
class Solution:
    def getCount(self, n):
        # code here
        allow_press={0:[0,8],1:[1,2,4],2:[1,2,3,5],3:[2,3,6],4:[1,4,5,7],
             5:[2,4,5,6,8],6:[3,5,6,9],7:[4,7,8],8:[5,7,8,9,0],9:[6,8,9]}
             
        def find(i,n):
            if n==0:
                return 1
            if (i,n) in dp:
                return dp[(i,n)]
            par_ans=0
            for el in allow_press[i]:
                par_ans+=find(el,n-1)
            dp[(i,n)]=par_ans
            return par_ans

        dp={}
        ans=0   
        for i in range(10):    
            ans+=find(i,n-1)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends