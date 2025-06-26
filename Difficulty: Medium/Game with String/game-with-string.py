class Solution:

    def minValue(self, s, k):
        n = len(s)

        # Count of each letter (a-z)
        alphabetCount = [0] * 26

        # Count frequency of each character
        for c in s:
            alphabetCount[ord(c) - ord('a')] += 1

        maxi = max(alphabetCount)  # Max frequency of any character

        # freq[i] = number of characters with frequency i
        freq = [0] * (maxi + 1)

        # Fill frequency bucket
        for count in alphabetCount:
            if count > 0:
                freq[count] += 1

        maxFreq = maxi

        # Remove k characters by reducing higher frequencies
        while k > 0 and maxFreq > 0:
            count_at_max = freq[maxFreq]
            if count_at_max == 0:
                maxFreq -= 1
                continue

            if count_at_max <= k:
                k -= count_at_max
                freq[maxFreq - 1] += count_at_max
                freq[maxFreq] = 0
                maxFreq -= 1
            else:
                freq[maxFreq] -= k
                freq[maxFreq - 1] += k
                k = 0

        # Calculate the result: sum of (freq^2 * number of chars with that freq)
        result = 0
        for i in range(1, len(freq)):
            result += (i * i * freq[i])

        return result