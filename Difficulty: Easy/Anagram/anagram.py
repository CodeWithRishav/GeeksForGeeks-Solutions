#User function Template for python3


import sys

sys.setrecursionlimit(10**6)


class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, str1, str2):

        # A dictionary to store the count of characters.
        mp = {}

        # Storing count of each character in the first string.
        for i in str1:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1

        # Decrementing the count of characters encountered in the second string.
        for i in str2:
            if i not in mp:
                return False
            else:
                mp[i] -= 1

        # Iterating over the dictionary to check if the count is zero for all characters.
        for i in mp:
            if mp[i] != 0:
                return False

        # Returning the result.
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = input().strip()
        b = input().strip()
        if (Solution().areAnagrams(a, b)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends