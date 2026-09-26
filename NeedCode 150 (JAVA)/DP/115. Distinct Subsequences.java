class Solution {
    public int numDistinct(String s, String t) {
        //1D solution
        int m = s.length(), n = t.length();
        int[] dp = new int[n+1];

        //base case, empty t
        dp[0]=1;

        for(int i = 1; i<=m;i++){
            //go backwards
            for(int j = n; j>=1;j--){
                if(s.charAt(i-1) == t.charAt(j-1))
                    dp[j] = dp[j-1]+dp[j];
            }
        }

        return dp[n];
        /*
        //2D solution
        int m = s.length(), n = t.length();
        int[][] dp = new int[m+1][n+1];
        
        dp[0][0] = 1; //base case
        // Empty t can always be formed in exactly one way
        for(int i = 1; i <= m; i++)
            dp[i][0] = 1;

        for(int i =1;i <=m; i++){
            for(int j=1;j<=n;j++){
                if(s.charAt(i-1) == t.charAt(j-1))
                    // Take s[i-1] OR skip s[i-1]
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                else
                    dp[i][j] = dp[i-1][j];
            }
        }
        return dp[m][n];
        */
    }
}
