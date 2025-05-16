class Solution:
    # Function to apply quadratic transformation
    def evaluate(self, x, A, B, C):
        return A * x * x + B * x + C

    # Function to transform and sort the array
    def sortArray(self, arr, A, B, C):
        n = len(arr)
        newArr = [0] * n

        left, right = 0, n - 1
        index = n - 1 if A >= 0 else 0

        # Two-pointer approach to fill newArr
        # from end or start
        while left <= right:
            leftVal = self.evaluate(arr[left], A, B, C)
            rightVal = self.evaluate(arr[right], A, B, C)

            if A >= 0:
                # Fill from end
                if leftVal > rightVal:
                    newArr[index] = leftVal
                    left += 1
                    index -= 1
                else:
                    newArr[index] = rightVal
                    right -= 1
                    index -= 1
            else:
                # Fill from start
                if leftVal < rightVal:
                    newArr[index] = leftVal
                    left += 1
                    index += 1
                else:
                    newArr[index] = rightVal
                    right -= 1
                    index += 1

        return newArr


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        a = int(input())
        b = int(input())
        c = int(input())

        ob = Solution()
        ans = ob.sortArray(arr, a, b, c)
        print(' '.join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends