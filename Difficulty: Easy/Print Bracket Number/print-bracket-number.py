#User function Template for python3
class Solution:
    def bracketNumbers(self, str):
        ans = []
        opening_bracket_num = 1
        closing_bracket_num = 1
        closed_taken = set()
        
        for ch in str:
            if ch == '(':
                ans.append(opening_bracket_num)
                closing_bracket_num = opening_bracket_num
                opening_bracket_num += 1
            elif ch == ')':
                while closing_bracket_num in closed_taken:
                    closing_bracket_num -= 1
                ans.append(closing_bracket_num)
                closed_taken.add(closing_bracket_num)
                closing_bracket_num -= 1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends