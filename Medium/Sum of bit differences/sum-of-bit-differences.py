#User function Template for python3
class Solution:
    def sumBitDifferences(self, arr, n):
        ans = 0  # Initialize result

        # Traverse over all bits
        for i in range(32):
            # Count number of elements with i'th bit set
            count = 0
            for j in range(n):
                if arr[j] & (1 << i):
                    count += 1

            # Add "count * (n - count) * 2" to the answer
            ans += count * (n - count) * 2

        return ans



#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends