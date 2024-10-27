class Solution:
    def findTriplet(self, arr):
        n=len(arr)
        s=set(arr)
        for i in range(n-1):
            for j in range(i+1,n):
                if arr[i]+arr[j] in s :
                    return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends