#User function Template for python3

class Solution:

    def longestUniqueSubstr(self, s):
        MAX_CHAR = 26
        if len(s) == 0 or len(s) == 1:
            return len(s)

        res = 0
        vis = [False] * MAX_CHAR

        # left and right pointer of sliding window
        left = 0
        right = 0
        while right < len(s):

            # If character is repeated, move left pointer marking
            # visited characters as false until the repeating
            # character is no longer part of the current window
            while vis[ord(s[right]) - ord('a')] == True:
                vis[ord(s[left]) - ord('a')] = False
                left += 1

            vis[ord(s[right]) - ord('a')] = True

            # The length of the current window (right - left + 1)
            # is calculated and answer is updated accordingly.
            res = max(res, (right - left + 1))
            right += 1

        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends