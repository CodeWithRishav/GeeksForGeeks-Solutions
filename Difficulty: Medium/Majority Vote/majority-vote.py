class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, nums):
        #Your Code goes here.
        n = len(nums)
        can1, can2 = None, None
        counter1, counter2 = 0, 0

        # First pass to find potential candidates
        for num in nums:
            if num == can1:
                counter1 += 1
            elif num == can2:
                counter2 += 1
            elif counter1 == 0:
                can1, counter1 = num, 1
            elif counter2 == 0:
                can2, counter2 = num, 1
            else:
                counter1 -= 1
                counter2 -= 1

        # Second pass to count actual votes
        vote1, vote2 = 0, 0
        for num in nums:
            if num == can1:
                vote1 += 1
            elif num == can2:
                vote2 += 1

        # Collect results
        result = []
        if vote1 > n / 3:
            result.append(can1)
        if vote2 > n / 3:
            result.append(can2)

        # Return result or [-1] if no candidates qualify
        return result if result else [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends