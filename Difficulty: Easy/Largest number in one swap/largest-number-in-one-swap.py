class Solution:

    def largestSwap(self, s):
        arr = list(s)
        maxDigit = '0'
        maxIndx, l, r = -1, -1, -1

        # Traverse from right to left
        for i in range(len(arr) - 1, -1, -1):
            # Update maxDigit if current digit is larger
            if arr[i] > maxDigit:
                maxDigit = arr[i]
                maxIndx = i
            elif arr[i] < maxDigit:
                l, r = i, maxIndx

        # If no swap needed, return original
        if l == -1:
            return s

        # Perform swap
        arr[l], arr[r] = arr[r], arr[l]
        return "".join(arr)