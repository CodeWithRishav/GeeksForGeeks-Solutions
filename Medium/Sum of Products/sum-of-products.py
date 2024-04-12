#User function Template for python3

class Solution:
    def pairAndSum(self, n, arr):
        #code here
        #here we will first use the logic of set bits to solve this 
        ans=0
        for i in range(0,32):
            count=0 #this will help us to count the number following the bitwise and 
            for j in range(0,n):
                if(arr[j]&(1<<i)):
                    #means this bit is set
                    count+=1
            ans+=(count*(count-1)//2)*(1<<i)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        Arr=list(map(int,input().strip().split(' ')))
        ob=Solution()
        print(ob.pairAndSum(N,Arr))
# } Driver Code Ends