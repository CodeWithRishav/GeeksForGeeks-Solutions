
class Solution:

    def findPeakUtil(self, arr, low, high, n):
        # Calculating mid
        mid = (low + high) // 2

        # If mid is the first or last index and the element is greater than the next or previous element
        if (mid == 0 or arr[mid - 1]
                <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
            return mid

        # If the middle element is smaller than the previous element, recurse on the left side
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return self.findPeakUtil(arr, low, mid - 1, n)

        # Else recurse on the right side
        else:
            return self.findPeakUtil(arr, mid + 1, high, n)

    def peakElement(self, arr):
        n = len(arr)  # Get the size of the array
        return self.findPeakUtil(arr, 0, n - 1, n)



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends