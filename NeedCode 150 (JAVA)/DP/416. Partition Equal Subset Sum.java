class Solution {
    public boolean canPartition(int[] nums) {
        int total = 0;
        for(int num : nums){
            total += num;
        }

        if(total % 2 ==1){
            return false;
        }

        int target = total /2 ;

        boolean[] dp = new boolean[target + 1];
        dp[0] = true;

        for(int num: nums){
            for(int sum = target; sum>= num;sum--){
                dp[sum] = dp[sum] || dp[sum-num];
            }
        }

        return dp[target];
    }
}
