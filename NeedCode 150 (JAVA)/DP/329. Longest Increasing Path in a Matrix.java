class Solution {

    private int[][] matrix,dp,directions= {{0,1},{0,-1},{1,0},{-1,0}};
    private int m,n;

    public int longestIncreasingPath(int[][] matrix) {
        this.matrix = matrix;
        m = matrix.length;
        n = matrix[0].length;
        dp = new int[m][n];

        int ans = 0;
        for(int i =0;i<m;i++){
            for(int j=0;j<n;j++){
                ans = Math.max(ans,dfs(i,j));
            }
        }
        return ans;
    }

    private int dfs(int r, int c){
        if(dp[r][c] != 0)
            return dp[r][c];
        
        int best = 1;//path length cell itself which is 1

        for(int[] dir: directions){
            int nr = r + dir[0], nc = c + dir[1];

            if(nr>=0 && nr < m && nc >=0 && nc<n && matrix[nr][nc] > matrix[r][c]){
                best = Math.max(best,1 + dfs(nr,nc));
            }
        }

        dp[r][c] = best;
        return best;

    }
}
