#User function Template for python3
class Solution:

    def sumClosest(self, arr, target):
        arr.sort()
        n = len(arr)
        res = []
        minDiff = float('inf')

        left = 0
        right = n - 1

        while left < right:
            currSum = arr[left] + arr[right]

            # Check if this pair is closer than the closest
            # pair so far
            if abs(target - currSum) < minDiff:
                minDiff = abs(target - currSum)
                res = [arr[left], arr[right]]

            # If this pair has less sum, move to greater values
            if currSum < target:
                left += 1

            # If this pair has more sum, move to smaller values
            elif currSum > target:
                right -= 1

            # If this pair has sum = target, return it
            else:
                return res

        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends