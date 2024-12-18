class Solution:

    # Function to check if the current minimum value is feasible or not.
    def isPossible(self, arr, n, k, curr_min):

        studentsRequired = 1
        curr_sum = 0

        # Iterating over all the books.
        for i in range(n):

            # If the current number of pages are greater than curr_min, return False.
            if arr[i] > curr_min:
                return False

            # Counting the number of students required to distribute curr_min pages.
            if curr_sum + arr[i] > curr_min:

                # Incrementing student count and updating curr_sum.
                studentsRequired += 1
                curr_sum = arr[i]

                # If students required becomes greater than the given number of students, return False.
                if studentsRequired > k:
                    return False

            # Else updating curr_sum.
            else:
                curr_sum += arr[i]

        return True

    # Function to find the minimum number of pages.
    def findPages(self, arr, k):
        n = len(arr)
        total_pages = sum(arr)

        # Returning -1 if the number of books is less than the number of students.
        if n < k:
            return -1

        # Initializing start as 0 pages and end as total pages.
        start, end = 0, total_pages
        result = 10**9

        while start <= end:

            mid = (start + end) // 2

            # Checking if it is possible to distribute books using mid as the current minimum.
            if self.isPossible(arr, n, k, mid):

                # If yes, then we find the minimum distribution.
                result = min(result, mid)

                # As we are finding minimum and books are sorted, reducing end as end = mid - 1.
                end = mid - 1

            # If not possible, pages should be increased so updating start = mid + 1.
            else:
                start = mid + 1

        # Returning the minimum number of pages.
        if result == 10**9:
            return -1
        else:
            return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends