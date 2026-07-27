class Solution {
    private int[][] directions = {
        {1,0},
        {-1,0},
        {0,1},
        {0,-1}
    };
    public int maxAreaOfIsland(int[][] grid) {
        int max_area = 0;

        for(int r = 0;r<grid.length;r++){
            for(int c=0;c<grid[0].length;c++){
                if(grid[r][c] == 1){
                    max_area = Math.max(max_area,dfs(grid,r,c));
                }
            }
        }
        return max_area;
    }
    private int dfs(int[][] grid,int r, int c){
        if(r<0 || r>=grid.length || c<0 || c>= grid[0].length || grid[r][c] == 0) return 0;

        int area = 1;
        grid[r][c] = 0;
        for(int[] dir : directions){
            int nr = r+dir[0];
            int nc = c+dir[1];
            area += dfs(grid,nr,nc);
        }
        return area;
    }
}
