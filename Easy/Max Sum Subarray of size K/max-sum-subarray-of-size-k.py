#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        subarray = sum(Arr[:K])
        max_sum = subarray
        
        for i in range(K,N):
            subarray = subarray - Arr[i - K] + Arr[i]
            max_sum = max(max_sum, subarray)
        return max_sum 

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends