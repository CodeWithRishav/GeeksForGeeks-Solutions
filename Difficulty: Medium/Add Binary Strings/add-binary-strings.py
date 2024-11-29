#User function Template for python3
class Solution:

    def addBinary(self, s1, s2):
        i = len(s1)  # length of string str1
        j = len(s2)  # length of string str2

        if i == 0:
            return s2  # if s1 is empty, return str2
        if j == 0:
            return s1  # if s2 is empty, return str1

        i -= 1  # decrement i by 1
        j -= 1  # decrement j by 1

        res = ""  # initialize an empty string
        carry = '0'  # initialize carry as '0'

        while (i >= 0 or j
               >= 0):  # loop while either i or j is greater than or equal to 0
            if i >= 0:
                ch1 = s1[i]  # store the current character of str1 in ch1
            else:
                ch1 = '0'  # if str1 is exhausted, set ch1 to '0'

            if j >= 0:
                ch2 = s2[j]  # store the current character of str2 in ch2
            else:
                ch2 = '0'  # if str2 is exhausted, set ch2 to '0'

            temp = int(ch1) + int(ch2) + int(
                carry)  # add the current digits and the carry
            if temp == 0:
                res += '0'  # if the sum is 0, append '0' to the result
                carry = '0'  # set carry to '0'

            elif temp == 1:
                res += '1'  # if the sum is 1, append '1' to the result
                carry = '0'  # set carry to '0'

            elif temp == 2:
                res += '0'  # if the sum is 2, append '0' to the result
                carry = '1'  # set carry to '1'

            else:
                res += '1'  # if the sum is 3, append '1' to the result
                carry = '1'  # set carry to '1'

            i -= 1  # decrement i by 1
            j -= 1  # decrement j by 1

        if carry == '1':
            res += carry  # if there is a remaining carry, append it to the result

        l = len(res)  # find the length of the result
        while l > 0 and res[
                l -
                1] == '0':  # loop while there are trailing zeros in the result
            l -= 1  # decrement l by 1

        if l == 0:
            return "0"  # if the result is all zeros, return "0"

        res = list(res)  # convert the result back to a list

        for i in range(l // 2):  # reverse the result by swapping characters
            res[i], res[l - i - 1] = res[l - i - 1], res[i]

        res = "".join(res)  # convert the result back to a string

        return res[0:l]  # return


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends