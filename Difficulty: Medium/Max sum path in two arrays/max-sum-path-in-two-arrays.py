#Your task is to complete this function
#Function should return an integer denoting the required answer
class Solution:

    def maxPathSum(self, arr1, arr2):
        i, j = 0, 0
        result, sum1, sum2 = 0, 0, 0
        m, n = len(arr1), len(arr2)

        # Using two pointers to iterate over two arrays
        while i < m and j < n:
            # if arr1 is smaller than arr2, increasing arr1 and adding its value to sum1
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            # if arr2 is smaller than arr1, increasing arr2 and adding its value to sum2
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            # if arr1 equals arr2, checking the maximum sum obtained from both the arrays
            # updating result and sum1 and sum2 are again changed to zero
            else:
                result += max(sum1, sum2)
                sum1 = 0
                sum2 = 0
                while i < m and j < n and arr1[i] == arr2[j]:
                    result += arr1[i]
                    i += 1
                    j += 1

        # if jth pointer reaches end
        while i < m:
            sum1 += arr1[i]
            i += 1
        # if ith pointer reaches end
        while j < n:
            sum2 += arr2[j]
            j += 1

        # last maximum sum to be added after the end of the loop
        result += max(sum1, sum2)

        return result


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPathSum(arr1, arr2)
        print(ans)

# } Driver Code Ends