from typing import List
import sys
sys.setrecursionlimit(10**8)

# Depth First Search to check if a cycle is present and mark the nodes present in the cycle
def dfs(u, adj, is_visited, in_stack, nodes_present_in_cycle):
    is_visited[u] = True
    in_stack[u] = True

    # Explore all the adjacent nodes
    for v in adj[u]:
        if is_visited[v] == False:
            # Recursive call to check if there is a cycle
            is_cycle_present = dfs(v, adj, is_visited, in_stack, nodes_present_in_cycle)
            if is_cycle_present == True:
                # Mark the current node as present in the cycle and return True
                nodes_present_in_cycle[u] = True
                return True
        # If an adjacent node is visited and is in the current recursion stack, a cycle is present
        elif is_visited[v] == True and in_stack[v] == True:
            nodes_present_in_cycle[u] = True
            return True

    # Mark the current node as not in recursion stack
    in_stack[u] = False
    return False 


class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        safeNodes = []
        is_visited = [False] * V
        in_stack = [False] * V
        nodes_present_in_cycle = [False] * V

        # Traverse each node and perform a DFS
        for i in range(V):
            if is_visited[i] == False:
                dfs(i, adj, is_visited, in_stack, nodes_present_in_cycle)
        
        # Add the nodes that are not present in any cycle to the safeNodes list
        for i in range(V):
            if nodes_present_in_cycle[i] == False:
                safeNodes.append(i)

        return safeNodes


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends