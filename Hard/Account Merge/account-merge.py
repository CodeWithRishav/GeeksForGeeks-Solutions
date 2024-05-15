#User function Template for python3

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find_parent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        par_u = self.find_parent(u)
        par_v = self.find_parent(v)
        if par_u == par_v:
            return
        if self.size[par_u] < self.size[par_v]:
            self.parent[par_u] = par_v
            self.size[par_v] += self.size[par_u]
        else:
            self.parent[par_v] = par_u
            self.size[par_u] += self.size[par_v]


class Solution:
    def accountsMerge(self, accounts):
        mp = {}
        n = len(accounts)
        ds = DisjointSet(n)
        par = 0
        for x in accounts:
            for i in range(1, len(x)):
                mail = x[i]
                if mail in mp:
                    ds.union_by_size(par, mp[mail])
                else:
                    mp[mail] = par
            par += 1
        merged_mail = [[] for _ in range(n)]
        for mail, par_node in mp.items():
            par_node = ds.find_parent(par_node)
            merged_mail[par_node].append(mail)
        ans = []
        for i in range(n):
            if not merged_mail[i]:
                continue
            merged_mail[i].sort()
            temp = [accounts[i][0]] + merged_mail[i]
            ans.append(temp)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        accounts = []
        for i in range(n):
            cntEmails = int(input())
            nameEmails = input().split()
            accounts.append(nameEmails)
        ob = Solution()
        res = ob.accountsMerge(accounts)
        res.sort()
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            for j in range(len(res[i])):
                if j != (len(res[i]) - 1):
                    print(res[i][j], end = ', ')
                else:
                    print(res[i][j], end='')
            if (i != len(res) - 1):
                print('], ')
            else:
                print(']', end = '')
        print(']')
# } Driver Code Ends