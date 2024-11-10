#User function Template for python3

class Solution:

    def computeLPSArray(self, s):
        lps = [0] * len(s)
        len_ = 0
        idx = 1

        # the loop calculates lps[i] for
        # i = 1 to str.length() - 1
        while idx < len(s):
            if s[idx] == s[len_]:
                len_ += 1
                lps[idx] = len_
                idx += 1
            else:

                # If len is 0, then we have no common prefix
                # which is also a suffix
                if len_ == 0:
                    lps[idx] = 0
                    idx += 1
                else:

                    # Note that we do not move to the next index
                    len_ = lps[len_ - 1]
        return lps

    # function to find the occurrence of pat in txt

    def KMPSearch(self, txt, pat, lps, rep):
        n, m = len(txt), len(pat)
        i = j = 0

        # Iterate till s1 is repeated rep times
        while i < n * rep:

            # If characters match, move both pointers forward
            if txt[i % n] == pat[j]:
                i += 1
                j += 1

                # If the entire pattern is matched
                if j == m:
                    return True

                    # Use lps of previous index to skip
                    # unnecessary comparisons
                    j = lps[j - 1]
            else:

                # If there is a mismatch, use lps value of
                # previous index to avoid redundant comparisons
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False

    # function to find Minimum number of times s1 has to be
    # repeated such that s2 is a substring of it

    def minRepeats(self, s1, s2):

        # Find lengths of strings
        n, m = len(s1), len(s2)

        # Declare and Compute the LPS Table
        lps = self.computeLPSArray(s2)

        # Find the minimum number of times s1 needs to be
        # repeated to become as long as s2
        x = (m + n - 1) // n

        # Check when string s1 is repeated x times
        if self.KMPSearch(s1, s2, lps, x):
            return x

        # Check when string s1 is repeated (x + 1) times
        if self.KMPSearch(s1, s2, lps, x + 1):
            return x + 1

        # If string s2 was not found, return -1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))

# } Driver Code Ends