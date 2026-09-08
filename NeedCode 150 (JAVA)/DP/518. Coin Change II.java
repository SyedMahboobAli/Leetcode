class Solution {
    public int change(int amount, int[] coins) {
        int[] dp = new int[amount+1];

        // One way to make amount 0: choose no coins
        dp[0] = 1;

        for(int coin: coins){
            for(int x = coin; x<=amount ; x++){
                dp[x] += dp[x-coin];
            }
        }
        return dp[amount];
    }
}
