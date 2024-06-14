#User function Template for python3

from typing import List

class Solution:
    def armstrongNumber (self, n):
        # code here 
        digits_str = str(n)
        
        num_digits = len(digits_str)
        
        
        sum_of_powers = 0
        
        for digit_str in digits_str:
            digit = int(digit_str)
            sum_of_powers += digit ** num_digits
        
        if sum_of_powers == n:
            return "true"
        else:
            return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends