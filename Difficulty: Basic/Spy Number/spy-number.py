class Solution:

    def checkSpy(self, n):
        digit = 0
        sum_ = 0
        product = 1
        while n > 0:
            digit = n % 10

            # getting sum of digits
            sum_ += digit

            # getting product of digits
            product *= digit
            n = n // 10

        if sum_ == product:
            return True
        else:
            return False