class Solution:
    def isPossible(self, N, arr):
        rem = 0
        # Calculating the remainder when the sum of array elements is divided by 3.
        for i in range(N):
            rem = (rem + arr[i]) % 3
        # Returning 1 if the remainder is 0, indicating that the array can be divided into 3 parts with equal sum.
        return int(rem == 0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.isPossible(N, arr))
# } Driver Code Ends