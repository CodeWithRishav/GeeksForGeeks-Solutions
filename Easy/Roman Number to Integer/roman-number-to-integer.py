class Solution:
    # This function returns value of each Roman symbol 
    def value(self, r): 
    	if (r == 'I'): 
    		return 1
    	if (r == 'V'): 
    		return 5
    	if (r == 'X'): 
    		return 10
    	if (r == 'L'): 
    		return 50
    	if (r == 'C'): 
    		return 100
    	if (r == 'D'): 
    		return 500
    	if (r == 'M'): 
    		return 1000
    	return -1
    	
    def romanToDecimal(self, str): 
    	res = 0
    	i = 0
    	while (i < len(str)):
    
    		# Getting value of symbol s[i] 
    		s1 = self.value(str[i]) 
    
    		if (i+1 < len(str)): 
    
    			# Getting value of symbol s[i+1] 
    			s2 = self.value(str[i+1]) 
    
    			# Comparing both values 
    			if (s1 >= s2): 
    
    				# Value of current symbol is greater 
    				# or equal to the next symbol 
    				res = res + s1 
    				i = i + 1
    			else: 
    
    				# Value of current symbol is greater 
    				# or equal to the next symbol 
    				res = res + s2 - s1 
    				i = i + 2
    		else: 
    			res = res + s1 
    			i = i + 1
    
    	return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends