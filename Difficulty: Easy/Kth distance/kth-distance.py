#User function Template for python3
class Solution:

    def checkDuplicatesWithinK(self, arr, k):
        n = len(arr)
        # Creates an empty set
        myset = set()

        # Traverse the input array
        for i in range(n):
            # If already present in set, then we found
            # a duplicate within k distance
            if arr[i] in myset:
                return True

            # Add this item to set
            myset.add(arr[i])

            # Remove the k+1 distant item
            if i >= k:
                myset.remove(arr[i - k])

        return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends