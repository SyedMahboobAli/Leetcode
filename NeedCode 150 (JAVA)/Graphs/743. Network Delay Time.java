/*
Why Dijkstra?

Because all edge weights are non-negative.

BFS does not work for weighted edges.
Dijkstra finds the shortest distance from one source to all nodes.
*/
class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {

    List<List<int[]>> graph = new ArrayList<>();
    for(int i =0;i<=n;i++){//nodes are labeled from 1 to n. we dont use 0, but 1 to n we use
        graph.add(new ArrayList<>());  
    }

    for(int[] time: times){
        int u = time[0];
        int v = time[1];
        int w = time[2];

        graph.get(u).add(new int[]{v,w});
    }

    PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
    pq.offer(new int[]{0,k});

    HashSet<Integer> visited = new HashSet<>(); //you can use boolean visited, but then you will also need count to check at the end
    int time = 0;

    while(!pq.isEmpty() && visited.size() < n){
        int[] curr = pq.poll();
        int d1 = curr[0];
        int node = curr[1];

        if(visited.contains(node))
            continue;
        visited.add(node);
        time = Math.max(time,d1); //the new node we are currently visting might have more time. so max. if We are polling any node. that is anyway the least time until now to reach that node.

        for(int[] nei: graph.get(node)){
            int next = nei[0];
            int d2 = nei[1];
            if(!visited.contains(next)){
                pq.offer(new int[]{d1+d2,next});
            }
        }
    }

    return visited.size() == n  ? time : -1;

    }
}
