class Solution {
    public int countSubstrings(String s) {
        int n = s.length();

        boolean[][] dp = new boolean[n][n];
        int count = 0;

        for(int i = n-1; i>=0;i--){
            for(int j = i; j <n;j++){
                if(s.charAt(i) == s.charAt(j) && (j-i<3 || dp[i+1][j-1])){
                    dp[i][j] = true;
                    count++;
                }
            }
        }
        return count;
    }
}
