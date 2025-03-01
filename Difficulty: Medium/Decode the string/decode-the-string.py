
class Solution:

    def decodedString(self, s):
        st = []

        # Traverse the input string
        for i in range(len(s)):
            # Push characters into the stack until ']' is encountered
            if s[i] != ']':
                st.append(s[i])
            # Decode when ']' is found
            else:
                temp = []

                # Pop characters until '[' is found
                while st and st[-1] != '[':
                    temp.append(st.pop())
                temp.reverse()  # Reverse extracted string
                # Remove '[' from the stack
                st.pop()

                num = []
                # Extract the number (repetition count) from the stack
                while st and st[-1].isdigit():
                    num.insert(0, st.pop())

                # Convert extracted number to integer
                number = int("".join(num))
                repeat = "".join(
                    temp
                ) * number  # Repeat the extracted string 'number' times

                # Push the expanded string back onto the stack
                st.extend(repeat)

        # Pop all characters from stack to form the final result
        return "".join(st)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends