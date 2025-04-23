#User function Template for python3

class Solution:

    def singleNum(self, arr):

        # Get the XOR of the two numbers we need to find
        xor_val = 0
        for i in arr:
            xor_val ^= i

        # Get its last set bit
        xor_val &= -xor_val

        res = [0, 0]

        for num in arr:

            # If bit is not set, it belongs to the first set
            if (num & xor_val) == 0:
                res[0] ^= num

            # If bit is set, it belongs to the second set
            else:
                res[1] ^= num

        # Ensure the order of the returned numbers is consistent
        if res[0] > res[1]:
            res[0], res[1] = res[1], res[0]

        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends