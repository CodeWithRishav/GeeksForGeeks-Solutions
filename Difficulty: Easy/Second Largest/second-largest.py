#User function Template for python3
class Solution:

    def getSecondLargest(self, arr):
        n = len(arr)
        if n < 2:
            return -1

        first = second = float('-inf')
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num

        if second == float('-inf'):
            return -1
        else:
            return second


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends