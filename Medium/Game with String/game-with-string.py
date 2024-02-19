class Solution:
    def minValue(self, s, k):
        
        temp_dict = {}
        
        for ch in s:
            temp_dict[ch] = temp_dict.get(ch, 0) + 1
            
        dict_list = []
        for val in temp_dict.values():
            dict_list.append(val)
            
        dict_list.sort(reverse = True)
        # print(dict_list)
        
        while k != 0:
            dict_list[0] -= 1
            dict_list.sort(reverse = True)
            
            # print(dict_list)
            k -= 1
        
        ans = 0
        for val in dict_list:
            ans += (val**2)
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends