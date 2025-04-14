#User function Template for python3
class Solution:

    def findOrder(words):

        # Adjacency list
        graph = [[] for _ in range(26)]

        # In-degree array
        inDegree = [0] * 26

        # To track which letters exist in input
        exists = [False] * 26

        # Mark existing characters
        for word in words:
            for ch in word:
                exists[ord(ch) - ord('a')] = True

        # Build graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minlen = min(len(w1), len(w2))
            j = 0
            while j < minlen and w1[j] == w2[j]:
                j += 1

            if j < minlen:
                u = ord(w1[j]) - ord('a')
                v = ord(w2[j]) - ord('a')
                graph[u].append(v)
                inDegree[v] += 1
            elif len(w1) > len(w2):
                # Invalid case
                return ""

        # Topological sort
        q = deque([i for i in range(26) if exists[i] and inDegree[i] == 0])
        result = []

        while q:
            u = q.popleft()
            result.append(chr(u + ord('a')))
            for v in graph[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)

        if len(result) != sum(exists):

            # Cycle detected or incomplete order
            return ""

        return ''.join(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
from collections import deque

#Position this line where user code will be pasted.


def validate(original, order):
    char_map = {}
    for word in original:
        for ch in word:
            char_map[ch] = 1

    for ch in order:
        if ch not in char_map:
            return False
        del char_map[ch]

    if char_map:
        return False

    char_index = {ch: i for i, ch in enumerate(order)}

    for i in range(len(original) - 1):
        a, b = original[i], original[i + 1]
        k, n, m = 0, len(a), len(b)
        while k < n and k < m and a[k] == b[k]:
            k += 1
        if k < n and k < m and char_index[a[k]] > char_index[b[k]]:
            return False
        if k != n and k == m:
            return False

    return True


if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    index = 0
    t = int(input_data[index])
    index += 1
    while t > 0:
        words = input_data[index].split()
        index += 1
        original = words[:]

        order = Solution.findOrder(words)

        if order == "":
            print("\"\"")
        else:
            print("true" if validate(original, order) else "false")
        print("~")
        t -= 1

# } Driver Code Ends