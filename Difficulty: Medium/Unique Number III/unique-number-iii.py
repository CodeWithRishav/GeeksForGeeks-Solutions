#User function Template for python3

class Solution:

    def getSingle(self, arr):
        ones, twos = 0, 0

        for num in arr:

            # Bits in both 'ones' and current number
            twos |= ones & num

            # XOR to get odd frequency bits
            ones ^= num

            # Remove common bits (appear 3 times)
            mask = ~(ones & twos)
            ones &= mask
            twos &= mask

        return ones

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSingle(arr)
        print(ans)
        print("~")
# } Driver Code Ends