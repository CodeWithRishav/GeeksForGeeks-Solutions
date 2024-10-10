class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        d={}
        sum=0
        maxi=-1
        for i in range(len(arr)):
            if arr[i] in d:
                sum=i-d[arr[i]]
                maxi=max(maxi,sum)
            else:
                d[arr[i]]=i
        return maxi



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends