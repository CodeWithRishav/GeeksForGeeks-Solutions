class Solution:
    def findSwapValues(self,a, n, b, m):
        suma,sumb=sum(a),sum(b)
        if (suma+sumb)%2:return -1
        
        a.sort()
        b.sort()
        
        i,j=0,0
        
        while i<n and j<m:
            swap1,swap2=suma-a[i]+b[j],sumb-b[j]+a[i]
            if swap1==swap2:
                return 1
            elif swap1>swap2:
                i+=1
            else:
                j+=1
        
        return -1


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        m=l[1]
        a = list(map(int,input().split()))
        b = list(map(int, input().split()))
        ob = Solution()
        print(ob.findSwapValues(a,n,b,m))
# } Driver Code Ends