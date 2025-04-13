#User function Template for python3

'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
'''

class Solution:

    def __init__(self):
        self.copies = {}

    def cloneGraph(self, node):
        if not node:
            return None

        if node not in self.copies:
            # Create a new node with the same value as the original node
            self.copies[node] = Node(node.val, [])
            # Copy the neighbors of the original node recursively
            for neighbor in node.neighbors:
                self.copies[node].neighbors.append(self.cloneGraph(neighbor))

        return self.copies[node]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from queue import Queue
import sys

sys.setrecursionlimit(10**6)


class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def compare(prev, new, prev_vis=set(), new_vis=set()):
    if prev == new:
        return False
    if not prev or not new:
        if (not prev and new) or (prev and not new):
            return False
        return True

    if prev in prev_vis or new in new_vis:
        if (prev in prev_vis and new not in new_vis) or (prev not in prev_vis
                                                         and new in new_vis):
            return False
        return True
    prev_vis.add(prev)
    new_vis.add(new)

    if prev.val != new.val:
        return False

    prev_n = len(prev.neighbors)
    new_n = len(prev.neighbors)
    if prev_n != new_n:
        return False

    prev.neighbors.sort(key=lambda x: x.val)
    new.neighbors.sort(key=lambda x: x.val)
    for i in range(prev_n):
        if not compare(prev.neighbors[i], new.neighbors[i], prev_vis, new_vis):
            return False

    return True


if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        v = [Node(i) for i in range(N)]
        for i in range(N):
            v[i].neighbors = [v[int(i)] for i in input().split()]
        ob = Solution()
        ans = ob.cloneGraph(v[0])
        # if ans == v[0]:
        #     print(0)
        print("true" if compare(v[0], ans) else "false")
        print("~")

# } Driver Code Ends