/*Prim’s algorithm grows the MST one node at a time.

At each step:

pick the not-yet-used point with the smallest connection cost
add it to the MST
update the best known cost for the remaining points
*/
class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        boolean[] visited = new boolean[n];

        pq.offer(new int[]{0,0}); //pq.offer([0,0]) will not work. it is python
        //visited[0] = true; Note, do not add visited here. Visited should only be update in while loop and after polling from PQ. Or else the Points Connection will never start

        int total_cost = 0;
        int count = 0; //since point 0 is not included, we are not adding +1 here

        while(!pq.isEmpty() && count < n){
            int[] curr = pq.poll();
            int cost = curr[0];
            int point = curr[1];

            if(visited[point])
                continue;
            
            visited[point] = true;
            total_cost += cost;
            count++;

            //Since the graph is complete (every point can connect to every other point), you don't build an adjacency list. When you remove a point from the heap, you compute its distance to every unvisited point on the fly. Loop is from 0 to n
            for(int next = 0; next<n;next++){
                if(!visited[next]){
                    int dist = Math.abs(points[point][0] - points[next][0]) + Math.abs(points[point][1] - points[next][1]);

                    pq.offer(new int[]{dist,next});
                }
            }
        }

        return total_cost; 
    }
}
