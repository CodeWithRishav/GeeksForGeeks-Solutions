class Solution:

    def solve(self, n, m, h, a, b):
        grp = [0] * m
        used = []
        unused = []
        cur = 0
        b = [x - 1 for x in b]
        for i in range(m):
            bisect.insort(unused, grp[i])

        k = 0
        res = [0] * (m + 1)

        for i in range(n):
            g = b[i]
            if grp[g] in used:
                used.remove(grp[g])
            else:
                unused.remove(grp[g])
                cur -= grp[g]

            grp[g] += a[i]
            bisect.insort(unused, grp[g])
            cur += grp[g]

            while len(used) < k:
                big = unused.pop()
                cur -= big
                bisect.insort(used, big)

            while used and unused:
                sml = used[0]
                big = unused[-1]

                if big > sml:
                    unused.pop()
                    bisect.insort(unused, sml)
                    cur -= big
                    cur += sml
                    used.pop(0)
                    bisect.insort(used, big)
                else:
                    break

            while cur >= h:
                res[k] = i
                k += 1
                big = unused.pop()
                cur -= big
                bisect.insort(used, big)

        while k <= m:
            res[k] = n
            k += 1

        return res