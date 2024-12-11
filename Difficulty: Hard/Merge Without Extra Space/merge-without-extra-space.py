class Solution:

    # Function to find the next gap.
    def nextGap(self, gap):
        # It returns the ceil value of gap/2 or 0 if gap is 1.
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)

    # Function to merge the arrays.
    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        gap = self.nextGap(n + m)
        i = 0
        j = 0

        while gap > 0:

            # Comparing elements in the first array itself with the gap.
            i = 0
            while i + gap < n:
                if a[i] > a[i + gap]:
                    a[i], a[i + gap] = a[i + gap], a[i]  # Swap
                i += 1

            # Comparing elements in both arrays.
            j = 0
            if gap > n:
                j = gap - n
            else:
                j = 0

            while i < n and j < m:
                if a[i] > b[j]:
                    a[i], b[j] = b[j], a[i]  # Swap
                i += 1
                j += 1

            # Comparing elements in the second array itself.
            if j < m:
                j = 0
                while j + gap < m:
                    if b[j] > b[j + gap]:
                        b[j], b[j + gap] = b[j + gap], b[j]  # Swap
                    j += 1
            gap = self.nextGap(gap)


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends