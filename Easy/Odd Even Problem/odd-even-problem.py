
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        from collections import Counter
        freq = Counter(s)
        x = 0
        y = 0
        for char, count in freq.items():
            position = ord(char) - ord('a') + 1  # Calculate the position in the alphabet (1-indexed)
            
            if position % 2 == 0 and count % 2 == 0:
                # Even position and even frequency
                x += 1
            elif position % 2 != 0 and count % 2 != 0:
                # Odd position and odd frequency
                y += 1
        result_sum = x + y
        
        # Determine if the sum is EVEN or ODD
        if result_sum % 2 == 0:
            return "EVEN"
        else:
            return "ODD"
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends