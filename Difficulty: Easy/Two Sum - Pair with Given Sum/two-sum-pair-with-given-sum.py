#User function Template for python3
class Solution:

    def twoSum(self, arr, target):
        hash_map = {}
        for i in range(len(arr)):
            number_to_find = target - arr[i]
            # if numberToFind is found in map, return true
            if number_to_find in hash_map:
                return True
            # number was not found. Put it in the map.
            hash_map[arr[i]] = i
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends