class Solution:

    def substrWithVowels(self, s1, s2):
        # Store unique vowels from s1
        required = set(s1)
        window = {}
        left = 0
        matchCount = 0
        minLen = float('inf')

        # Expand window using right pointer
        for right in range(len(s2)):
            ch = s2[right]
            if ch in required:
                window[ch] = window.get(ch, 0) + 1
                if window[ch] == 1:
                    matchCount += 1

            # Shrink from left while all required vowels matched
            while matchCount == len(required):
                minLen = min(minLen, right - left + 1)
                leftCh = s2[left]
                left += 1
                if leftCh in required:
                    window[leftCh] -= 1
                    if window[leftCh] == 0:
                        matchCount -= 1

        return -1 if minLen == float('inf') else minLen