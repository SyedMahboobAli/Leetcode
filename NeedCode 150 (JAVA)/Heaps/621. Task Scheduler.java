class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        for(char task: tasks){
            freq[task - 'A']++;
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder()); // Max Heap

        for(int f: freq){
            if (f>0)
                maxHeap.offer(f);
        }

        Queue<int[]> cooldown = new LinkedList<>();
        int time= 0;

        //Heap and Queue has same functions

        while(!cooldown.isEmpty() || !maxHeap.isEmpty()){
            time++;

             // Release tasks whose cooldown is over
            if(!cooldown.isEmpty() && cooldown.peek()[1] == time){
                maxHeap.offer(cooldown.poll()[0]); // check cooldown.poll()[0]
            }

            // Execute one task if possible
            if(!maxHeap.isEmpty()){

                int count = maxHeap.poll() - 1;//Executing it now, so -1 and add this to queue
                if(count>0){
                    // [remainingCount, availableTime]
                    cooldown.offer(new int[]{count,n+time +1}); // here we are adding +1 because it is available at that time. In between 2 executions, there should be n time. ALso ensure we have new int[]{} to create object
                }

            }
        }

        return time;
    }
}
