#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        maxEle=max(arr)
        freq={}
        for i in arr:
            freq[i]=freq.get(i,0)+1
        count=0
        for i in range(maxEle+1):
            if i in freq:
                count+=freq[i]
                if count>=k:
                    return i
        return -1
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends