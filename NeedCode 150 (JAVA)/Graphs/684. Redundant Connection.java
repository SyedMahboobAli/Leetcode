class Solution {
    private int[] parent;
    private int[] rank;
    public int[] findRedundantConnection(int[][] edges) {
        //Given there are n edges and n nodes. nodes from 1 to n
        int n = edges.length;
        parent = new int[n+1]; // 1 to n
        rank = new int[n+1];

        //Initialize
        for(int i = 1; i<=n;i++){
            parent[i] = i; //every node is its own parent
            rank[i] = 0; //how many children it has
        }


        for(int[] edge: edges){
            int u = edge[0], v = edge[1];
            int pu = find(u), pv = find(v);

            if(pu == pv) return edge;

            union(pu,pv); //do union on parent
        }

        return new int[0];

    }

    private int find(int x){
        if(parent[x]!=x){
            parent[x]=find(parent[x]);
        }
        return parent[x];
    }

    private void union(int x, int y){
        if(rank[x] > rank[y]){
            parent[y] = parent[x];
        }
        else if(rank[y] > rank[x]){
            parent[x] = parent[y];
        }
        else{
            parent[y] = x;
            rank[x]++;
        }
    }

}
