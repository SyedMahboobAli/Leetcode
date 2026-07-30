//DFS 
import java.util.*;

class Solution {

    public int countComponents(int n, int[][] edges) {

        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        // Undirected graph
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        boolean[] visited = new boolean[n];

        int components = 0;

        for (int i = 0; i < n; i++) {

            if (!visited[i]) {
                dfs(i, graph, visited);
                components++;
            }
        }

        return components;
    }

    private void dfs(int node, List<List<Integer>> graph, boolean[] visited) {

        visited[node] = true;

        for (int neighbor : graph.get(node)) {

            if (!visited[neighbor]) {
                dfs(neighbor, graph, visited);
            }
        }
    }
}

//-------------------------------------------------------------------------------------------------------------------------
//Union Find solution : DSU
class Solution {

    int[] parent;

    public int countComponents(int n, int[][] edges) {

        parent = new int[n];

        for (int i = 0; i < n; i++)
            parent[i] = i;

        int components = n;

        for (int[] edge : edges) {

            int p1 = find(edge[0]);
            int p2 = find(edge[1]);

            if (p1 != p2) {
                parent[p1] = p2;
                components--;
            }
        }

        return components;
    }

    private int find(int x) {

        if (parent[x] != x)
            parent[x] = find(parent[x]);

        return parent[x];
    }
}
