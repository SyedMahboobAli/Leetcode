class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        if (n==0) return new int[0];
        int[] result = new int[n-k+1]; //total possible no of windows
        Deque<Integer> dq = new LinkedList<>(); // Stores Indices
        for(int i = 0;i<n;i++){
            //Remove indices out of window
            if(!dq.isEmpty() && dq.peekFirst() == i-k){
                dq.pollFirst();
            }

            //Maintain Decreasing Order
            while(!dq.isEmpty() && nums[dq.peekLast()] < nums[i]){
                dq.pollLast();

            }

            //Add curr index
            dq.offerLast(i);

            //Add to the result when window is ready
            if(i>=k-1){
                result[i-k+1] = nums[dq.peekFirst()];
            }
        }
        return result;
    }
}
