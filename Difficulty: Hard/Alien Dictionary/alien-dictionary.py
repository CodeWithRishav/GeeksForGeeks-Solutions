#User function Template for python3

from collections import deque
from typing import List
class Solution:
    def topoSort(self, V, adj):
        indegree = [0]*V
        for u in adj:
            for v in adj[u]:
                indegree[ord(v) - ord('a')] += 1
        
        que = deque()
                
        for i in range(V): 
            if indegree[i] == 0: que.append(chr(ord('a')+i))
            
        result = []
        
        while que:
            node = que.popleft()
            result.append(node)
            
            for x in adj[node]:
                indegree[ord(x)-ord('a')] -= 1
                if indegree[ord(x)-ord('a')] == 0: que.append(x)
        return result
                
    def findOrder(self, alien_dict: List[str], N: int, K: int) -> str:
    
        adj = {chr(97+i):[] for i in range(K)}
        for i in range(N-1):
            s1,s2 = alien_dict[i],alien_dict[i+1]
            n = min(len(s1),len(s2))
            for j in range(n):
                
                if s1[j] != s2[j]:
                    adj[s1[j]].append(s2[j])
                    break
        return self.topoSort(K,adj)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


class sort_by_order:

    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends