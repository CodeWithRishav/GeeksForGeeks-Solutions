#User function Template for python3

from heapq import heappush as hpush, heappop as hpop
class Solution:
    def findOrder(self, n, m, p):
        # Code here
        a=[[] for k in range(n)]
        indeg=[0] * n
        for i,j in p:
            a[j].append(i)
            indeg[i]+=1
        h=[]
        for i in range(n):
            if indeg[i]==0:
                hpush(h,i)
        r=[]
        while h:
            node=hpop(h)
            r.append(node)
            for j in a[node]:
                indeg[j]-=1
                if indeg[j]==0:
                    hpush(h,j)
        if len(r)!=n:
            return []
        return r


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
	map=[0]*N
	for i in range(N):
		map[res[i]]=i
	for i in range(N):
		for v in graph[i]:
			if map[i] > map[v]:
				return False
	return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends