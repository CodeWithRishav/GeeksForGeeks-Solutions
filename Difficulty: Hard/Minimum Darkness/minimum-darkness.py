class Solution:
    INF = int(1e7)

    def solve(self, n, k, query, edges):
        # Step 1: Build the tree as adjacency list
        tree = [[] for _ in range(n + 1)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Step 2: Process queries
        dis = [self.INF] * (n + 1)
        isclr = [False] * (n + 1)
        out = []
        ans = self.INF

        for i in range(k):
            ele = query[i]
            dis[ele] = 0
            ans = self.dfs(ele, -1, tree, dis, isclr, ans)
            isclr[ele] = True

            if i == 0:
                out.append(-1)
            else:
                out.append(ans)

        return out

    def dfs(self, node, parent, tree, dis, isclr, ans):
        if dis[node] >= ans:
            return ans

        if isclr[node]:
            ans = min(ans, dis[node])

        for child in tree[node]:
            if child == parent:
                continue

            if dis[child] > dis[node] + 1:
                dis[child] = dis[node] + 1
                ans = self.dfs(child, node, tree, dis, isclr, ans)
            else:
                ans = min(ans, dis[node] + dis[child] + 1)

        return ans