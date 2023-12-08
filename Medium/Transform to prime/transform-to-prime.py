MAX=1000001
primes=[True]*MAX
primes[1]=False
for i in range(2,int(MAX**(0.5))+1):
    if(primes[i]):
        for j in range(2*i,MAX,i):
            primes[j]=False

class Solution:
            
    
    def minNumber(self, arr,n):

        sm=sum(arr)

        st=sm
        
        while(primes[st]==False): st+=1
        
        return int(st-sm)




#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends