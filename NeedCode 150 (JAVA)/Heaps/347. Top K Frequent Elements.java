class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freqmap = new HashMap<>();

        for(int num: nums){
            freqmap.put(num,freqmap.getOrDefault(num,0)+1);
        }

        PriorityQueue<Integer> minheap = new PriorityQueue<>((a,b) -> freqmap.get(a) - freqmap.get(b));
        //to implement max heap:
        //PriorityQueue<Integer> pq =
    //new PriorityQueue<>((a, b) -> b - a);
    
        for(int num: freqmap.keySet()){
            minheap.offer(num);
            if(minheap.size() > k){
                minheap.poll();
            }
        }

        int[] result = new int[k];
        int i = 0;
        while(!minheap.isEmpty()){
            result[i++] = minheap.poll();
        
        }
        return result;
    }
}
