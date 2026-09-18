class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int total = 0;
        for(int num: nums)
            total += num;
        
        if(Math.abs(target) > total || (target + total) % 2 != 0)
            return 0;

        int P = (total+target)/2;
        int[] dp = new int[P + 1];
        dp[0] = 1;

        for(int num : nums){

            //Reverse loop: each number can be used once
            for(int sum = P; sum >= num; sum--){
                dp[sum] += dp[sum-num];
            }
        }
        return dp[P];
    }
}
