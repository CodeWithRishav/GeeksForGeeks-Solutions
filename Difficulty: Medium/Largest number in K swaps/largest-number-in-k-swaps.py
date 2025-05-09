#User function Template for python3

class Solution:

    # Function to keep the maximum result
    def match(self, curr, res):

        # If current number is larger, update result
        if curr > res:
            res = curr
        return res

    # Function to set highest possible digits
    # at given index
    def setDigit(self, s, index, res, k):

        # Base case: If no swaps left or index reaches
        # the last character, update result
        if k == 0 or index == len(s) - 1:
            res = self.match(s, res)
            return res

        maxDigit = 0

        # Finding maximum digit for placing at given index
        for i in range(index, len(s)):
            maxDigit = max(maxDigit, int(s[i]))

        # If the digit at current index is already max
        if int(s[index]) == maxDigit:
            res = self.setDigit(s, index + 1, res, k)
            return res

        # Try swapping with the maximum digit found
        for i in range(index + 1, len(s)):

            # If max digit is found at current position
            if int(s[i]) == maxDigit:

                # Swap to get the max digit at the required index
                s = self.swap(s, index, i)

                # Call the recursive function to set the next digit
                res = self.setDigit(s, index + 1, res, k - 1)

                # Backtrack: swap the digits back
                s = self.swap(s, index, i)

        return res

    # Function to swap characters in the string
    def swap(self, s, i, j):

        # Convert string to list for mutation,
        # then back to string
        s_list = list(s)
        s_list[i], s_list[j] = s_list[j], s_list[i]
        return ''.join(s_list)

    # Function to find the largest number after k swaps
    def findMaximumNum(self, s, k):
        res = s
        res = self.setDigit(s, 0, res, k)

        # Returning the result
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob = Solution()
        print(ob.findMaximumNum(s, k))

        print("~")

# } Driver Code Ends