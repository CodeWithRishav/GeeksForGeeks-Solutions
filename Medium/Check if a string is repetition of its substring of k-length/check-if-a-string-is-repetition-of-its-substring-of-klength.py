class Solution:
    def kSubstrConcat(self, n: int, s: str, k: int) -> int:
        if n % k != 0:
            return 0
        
        substrings = set()
        substring_count = {}
        
        for i in range(0, n, k):
            current_substr = s[i:i+k]
            substrings.add(current_substr)
            if current_substr not in substring_count:
                substring_count[current_substr] = 0
            substring_count[current_substr] += 1

        if len(substrings) > 2:
            return 0
        
        if len(substrings) == 2:
            it = iter(substrings)
            if substring_count[next(it)] > 1:
                if substring_count[next(it)] > 1:
                    return 0

        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends