#User function Template for python3

class Solution:
    # Function to multiply two strings
    def multiplyStrings(self, a, b):
        # Checking if either of the strings is zero
        if a == '0' or b == '0':
            return '0'

        # Setting a variable to keep track of the sign of the product
        negative = False
        # Checking if the first string is negative
        if a[0] == '-':
            negative = not negative
            a = a[1:]

        # Checking if the second string is negative
        if b[0] == '-':
            negative = not negative
            b = b[1:]

        # Initializing a list to store the product
        product = [0 for _ in range(len(a) + len(b))]

        # Multiplying each digit of the second string with each digit of the first string
        for i in range(len(b) - 1, -1, -1):
            digit1 = int(b[i])
            carry = 0

            # Iterating over each digit of the first string
            for j in range(len(a) - 1, -1, -1):
                digit2 = int(a[j])

                # Adding the product of the digits with the carry
                product[i + j + 1] += digit1 * digit2 + carry
                carry = product[i + j + 1] // 10
                product[i + j + 1] = product[i + j + 1] % 10

            # Handling any remaining carry
            nextIndex = i
            while carry:
                product[nextIndex] += carry
                carry = product[nextIndex] // 10
                product[nextIndex] = product[nextIndex] % 10
                nextIndex -= 1

        # Converting the product list to a string
        res = ''.join(str(x) for x in product)

        # Removing leading zeroes from the product
        zeroes = 0
        while zeroes < len(res) - 1 and res[zeroes] == '0':
            zeroes += 1
        res = res[zeroes:]

        # Adding the negative sign if necessary
        if negative and res != "0":
            res = '-' + res

        # Returning the final product
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a = input()
        b = input()
        print(Solution().multiplyStrings(a.strip(), b.strip()))

        print("~")

# } Driver Code Ends