#User function template for Python
class Solution:

    def myAtoi(self, s):
        sign = 1
        res = 0
        idx = 0

        # Ignore leading whitespaces
        while idx < len(s) and s[idx] == ' ':
            idx += 1

        # Store the sign of number
        if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
            if s[idx] == '-':
                sign = -1
            idx += 1

        # Construct the number digit by digit
        while idx < len(s) and '0' <= s[idx] <= '9':

            # Handling overflow/underflow test case
            if res > (2**31 - 1) // 10 or \
                    (res == (2**31 - 1) // 10 and ord(s[idx]) - ord('0') > 7):
                return sign * (2**31 - 1) if sign == 1 else -2**31

            # Append current digit to the result
            res = 10 * res + (ord(s[idx]) - ord('0'))
            idx += 1

        return res * sign


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends