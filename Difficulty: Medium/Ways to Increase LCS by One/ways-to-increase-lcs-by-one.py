class Solution:

    def waysToIncreaseLCSBy1(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        M = 26

        position = [[] for _ in range(M)]

        for i in range(n2):
            position[ord(s2[i]) - ord('a')].append(i + 1)

        lcsl = [[0] * (n2 + 2) for _ in range(n1 + 2)]
        lcsr = [[0] * (n2 + 3) for _ in range(n1 + 3)]

        # prefix LCS
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    lcsl[i][j] = lcsl[i - 1][j - 1] + 1
                else:
                    lcsl[i][j] = max(lcsl[i - 1][j], lcsl[i][j - 1])

        # suffix LCS
        for i in range(n1, 0, -1):
            for j in range(n2, 0, -1):
                if s1[i - 1] == s2[j - 1]:
                    lcsr[i][j] = lcsr[i + 1][j + 1] + 1
                else:
                    lcsr[i][j] = max(lcsr[i + 1][j], lcsr[i][j + 1])

        base = lcsl[n1][n2]
        ways = 0

        for i in range(n1 + 1):
            for c in range(26):
                for p in position[c]:
                    if lcsl[i][p - 1] + lcsr[i + 1][p + 1] == base:
                        ways += 1
                        break

        return ways