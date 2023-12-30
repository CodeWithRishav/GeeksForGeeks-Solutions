import collections
class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        lk = collections.Counter(arr)
        m = max(lk.values())
        ans = []
        
        for k,v in lk.items():
            if v == m:
                ans.append([k,v])
        
        if len(ans)==1:
            return ans[0]
        ans.sort(key = lambda x:x[0])
        return ans[0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends