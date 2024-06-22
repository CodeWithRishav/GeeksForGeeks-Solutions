import re
class Solution:
    def ExtractNumber(self,sentence):
        #code here
        def find_numbers(string):
            return re.findall(r'\d+', string)
        numbers = find_numbers(sentence)
        numbers = list(map(int, numbers))  # Convert to integers

        while numbers:
            max_value = max(numbers)
            if '9' in str(max_value):
                numbers.remove(max_value)
            else:
                return max_value
        return -1


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends