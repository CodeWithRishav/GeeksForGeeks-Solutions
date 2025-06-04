class Solution:

    def lcsOf3(self, s1: str, s2: str, s3: str) -> int:
        # Lengths of the three strings
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        # Initialize two 2D DP arrays
        # prev holds values for the previous i-1 level
        # curr holds values for the current i level
        prev = [[0] * (n3 + 1) for _ in range(n2 + 1)]
        curr = [[0] * (n3 + 1) for _ in range(n2 + 1)]

        # Iterate over all characters of s1
        for i in range(1, n1 + 1):

            # Iterate over all characters of s2
            for j in range(1, n2 + 1):

                # Iterate over all characters of s3
                for k in range(1, n3 + 1):

                    # If characters match in all three strings
                    if s1[i - 1] == s2[j - 1] and s2[j - 1] == s3[k - 1]:
                        curr[j][k] = 1 + prev[j - 1][k - 1]
                    else:

                        # Take max by excluding current char from one of the strings
                        curr[j][k] = max(prev[j][k], curr[j - 1][k],
                                         curr[j][k - 1])

            # Copy curr to prev for the next i-level iteration
            prev = [row[:] for row in curr]

        # The final LCS length is at curr[n2][n3]
        return curr[n2][n3]