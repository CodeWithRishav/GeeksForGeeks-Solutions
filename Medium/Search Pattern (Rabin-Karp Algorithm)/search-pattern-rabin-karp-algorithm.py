#User function Template for python3

import hashlib

class Solution:
    
    def sha_256_hash(self,s):
        sha256 = hashlib.sha256()
        sha256.update(s.encode('utf-8'))
        return sha256.hexdigest()
    
    def search(self, pattern, text):
        # code here
        occurence = []
        pattern_len = len(pattern)
        text_len = len(text)
        pattern_hash = self.sha_256_hash(pattern)
        text_hash = self.sha_256_hash(text[:pattern_len])
        
        for i in range(len(text) - len(pattern) + 1):
            if pattern_hash == text_hash and text[i:i+len(pattern)] == pattern:
                occurence.append(i+1)
            if i < (text_len - pattern_len):
                text_hash = self.sha_256_hash(text[i+1:i + pattern_len + 1])
        return occurence


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends