class manacher:
    # Build modified string and run Manacher's algorithm
    def __init__(self, s):
        self.ms = "@"
        for c in s:
            self.ms += "#" + c
        self.ms += "#$"
        self.p = [0] * len(self.ms)
        self.runManacher()

    # Fill the palindrome radius array
    def runManacher(self):
        n = len(self.ms)
        l, r = 0, 0

        for i in range(1, n - 1):
            # If inside current right boundary, use previously
            # computed value by mirroring
            if 0 <= r + l - i < n:
                self.p[i] = max(0, min(r - i, self.p[r + l - i]))

            # Expand the palindrome centered at i
            while (i + self.p[i] + 1 < n and i - self.p[i] - 1 >= 0 and
                   self.ms[i + 1 + self.p[i]] == self.ms[i - 1 - self.p[i]]):
                self.p[i] += 1

            # Update the current palindrome boundary
            # if this one extends further
            if i + self.p[i] > r:
                l = i - self.p[i]
                r = i + self.p[i]

    # Returns the radius of the longest palindrome centered \
    # at index `cen`
    def getLongest(self, cen, odd):
        pos = 2 * cen + 2 + (0 if odd else 1)
        return self.p[pos]

    # Check if s[l...r] is a palindrome of expected type
    def check(self, l, r):
        length = r - l + 1
        mid = (l + r) // 2
        return length <= self.getLongest(mid, length % 2)


class Solution:

    def maxSum(self, s):
        n = len(s)
        leftMark = [1] * n
        rightMark = [1] * n

        mr = manacher(s)

        # Store the max odd-length palindrome ending at or
        # before each index
        for i in range(n):
            val = mr.getLongest(i, 1)
            li = i + val // 2
            if li < n:
                leftMark[li] = max(leftMark[li], val)

        # Spread max values backwards by reducing length by 2
        for i in range(n - 2, -1, -1):
            leftMark[i] = max(leftMark[i], leftMark[i + 1] - 2)

        # Make prefix max array
        for i in range(1, n):
            leftMark[i] = max(leftMark[i], leftMark[i - 1])

        # Store the max odd-length palindrome starting at or
        # after each index
        for i in range(n - 1, -1, -1):
            val = mr.getLongest(i, 1)
            ri = i - val // 2
            if ri >= 0:
                rightMark[ri] = max(rightMark[ri], val)

        # Spread max values forward by reducing length by 2
        for i in range(1, n):
            rightMark[i] = max(rightMark[i], rightMark[i - 1] - 2)

        # Make suffix max array
        for i in range(n - 2, -1, -1):
            rightMark[i] = max(rightMark[i], rightMark[i + 1])

        # Try every cut point and compute the best non-overlapping sum
        ans = 1
        for i in range(n - 1):
            ans = max(ans, leftMark[i] + rightMark[i + 1])

        return ans