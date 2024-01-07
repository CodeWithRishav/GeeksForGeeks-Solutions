class Solution:
    def splitArray(self, arr, N, K):
        # code here 
        
        l=max(arr)
        r=sum(arr)
        while(l<=r):
            m=(l+r)//2
            mp=Solution.findsub(arr,m)
            if mp>K:
                l=m+1
            else:
                r=m-1
        return l
        
    def findsub(arr,m):
        k,s=1,0
        for i in arr:
            if s+i<=m:
                s+=i
            else:
                k+=1
                s=i
        return k 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends