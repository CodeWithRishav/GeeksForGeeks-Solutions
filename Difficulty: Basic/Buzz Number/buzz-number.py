class Solution:

    def isBuzz(self, n):
        # checking if the number ends with 7 or is divisible by 7
        return n % 10 == 7 or n % 7 == 0