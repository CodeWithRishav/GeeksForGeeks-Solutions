class Solution:
    def pushZerosToEnd(self,arr, n):
        k = arr.count(0)  # Count the number of zeros in the array
        arr1 = []  # Create an empty list to store non-zero elements
        for i in range(n):
            if arr[i] != 0:
                arr1.append(arr[i])
        for i in range(k):
            arr1.append(0)
        for i in range(n):
            arr[i] = arr1[i]
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends