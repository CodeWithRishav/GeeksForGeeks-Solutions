class Solution:

    def subarrayXor(self, arr, m):
        res = 0

        # Create map that stores number of prefix arrays
        # corresponding to a XOR value
        mp = {}

        prefXOR = 0

        for val in arr:
            # Find XOR of current prefix
            prefXOR ^= val

            # If prefXOR ^ k exists in mp then there is a subarray
            # ending at i with XOR equal to k
            res += mp.get(prefXOR ^ k, 0)

            # If this prefix subarray has XOR equal to k
            if prefXOR == k:
                res += 1

            # Add the XOR of this subarray to the map
            mp[prefXOR] = mp.get(prefXOR, 0) + 1

        # Return total count of subarrays having XOR of
        # elements as given value k
        return res


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends