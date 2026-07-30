class Solution {
    int[] parent;
    int[] rank;

    public boolean validTree(int n, int[][] edges) {
        // A valid tree must have exactly n - 1 edges
        if (edges.length != n - 1) return false;

        parent = new int[n];
        rank = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            int pu = find(u);
            int pv = find(v);

            // Cycle detected
            if (pu == pv) return false;

            union(pu, pv);
        }

        return true;
    }

    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    private void union(int x, int y) {
        if (rank[x] < rank[y]) {
            parent[x] = y;
        } else if (rank[x] > rank[y]) {
            parent[y] = x;
        } else {
            parent[y] = x;
            rank[x]++;
        }
    }
}
