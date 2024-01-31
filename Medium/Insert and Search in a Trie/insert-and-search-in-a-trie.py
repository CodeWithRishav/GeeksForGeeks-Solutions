#User function Template for python3

"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""

class Solution:
    #Function to insert string into TRIE.
    def insert(self, root, key):
        cur=root
        for v in key:
            v=ord(v)-ord('a')
            if cur.children[v]:
                cur=cur.children[v]
            else:
                cur.children[v]=TrieNode()
                cur=cur.children[v]
        cur.isEndOfWord=True
    
    #Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        cur=root
        for v in key:
            v=ord(v)-ord('a')
            if cur.children[v]:
                cur=cur.children[v]
            else:
                return False
        return cur.isEndOfWord


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        ob = Solution()
        
        for s in arr:
            ob.insert(t.root,s)
        
        if ob.search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends