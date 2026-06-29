class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a,b) -> Integer.compare(distance(b) , distance(a)));

        for(int[] point : points){
            maxHeap.offer(point);
            if(maxHeap.size() > k)
                maxHeap.poll();
        }

        int[][] result = new int[k][2];
        for(int i =0;i<k;i++){
            result[i] = maxHeap.poll();
        }

        return result;
    }

    private int distance(int[] point){
        return point[0] * point[0] + point[1] * point[1];
    }
}
