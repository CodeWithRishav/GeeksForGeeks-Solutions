#User function Template for python3

class Solution:

    def search(self, arr, key):
        # Initialize two pointers, lo and hi, at the start
        # and end of the array
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # If key found, return the index
            if arr[mid] == key:
                return mid

            # If Left half is sorted
            if arr[mid] >= arr[lo]:

                # If the key lies within this sorted half,
                # move the hi pointer to mid - 1
                if key >= arr[lo] and key < arr[mid]:
                    hi = mid - 1

                # Otherwise, move the lo pointer to mid + 1
                else:
                    lo = mid + 1

            # If Right half is sorted
            else:

                # If the key lies within this sorted half,
                # move the lo pointer to mid + 1
                if key > arr[mid] and key <= arr[hi]:
                    lo = mid + 1

                # Otherwise, move the hi pointer to mid - 1
                else:
                    hi = mid - 1

        # Key not found
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends