#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;

class DisJointSet {
  public:
    vector<int> size, parent, rank;
    int components;

    DisJointSet(int n) {
        components = n;
        size.resize(n + 1, 1);
        rank.resize(n + 1, 0);
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0);
    }

    int findUltimateParent(int node) {
        if (node == parent[node])
            return node;
        return parent[node] = findUltimateParent(parent[node]);
    }

    void unionBySize(int u, int v) {
        int ulp_u = findUltimateParent(u);
        int ulp_v = findUltimateParent(v);

        if (ulp_u == ulp_v)
            return;

        if (size[ulp_u] > size[ulp_v]) {
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        } else {
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        }

        components--;
    }
};

class Solution {
  public:
    int findComponents(int n, int m, const vector<vector<int>>& arr) {
        vector<vector<int>> res(n + 1, vector<int>(11, 0));

        for (int i = 0; i < m; ++i) {
            int a = arr[i][0], d = arr[i][1], k = arr[i][2];
            res[a][d] = max(res[a][d], k);
        }

        DisJointSet ds(n);

        for (int d = 1; d <= 10; ++d) {
            for (int i = 1; i <= n; ++i) {
                int iter = res[i][d];
                int start = i;

                while (iter > 0 && start + d <= n) {
                    ds.unionBySize(start, start + d);
                    res[start][d] = 0;
                    start += d;
                    iter = max(iter - 1, res[start][d]);
                }
            }
        }

        return ds.components;
    }
};