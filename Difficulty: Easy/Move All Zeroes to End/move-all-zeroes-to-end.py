#User function Template for python3

class Solution:

    def pushZerosToEnd(self, arr):
        count = 0
        n = len(arr)
        # Traverse the array. If element encountered is non-
        # zero, then replace the element at index 'count'
        # with this element
        for i in range(n):
            if (arr[i] != 0):
                arr[count] = arr[i]
                count += 1

        # Now all non-zero elements have been shifted to
        # front and 'count' is set as index of first 0.
        # Make all elements 0 from count to end.
        while (count < n):
            arr[count] = 0
            count += 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends