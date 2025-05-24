class Solution:

    def sumSubstrings(self, s):

        # Initialize result
        sum = 0
        mf = 1
        for i in range(len(s) - 1, -1, -1):
            sum = sum + (int(s[i])) * (i + 1) * mf
            mf = mf * 10 + 1

        return sum