class Solution {
    int rows, cols;
    private int[][] directions = {
        {1,0},
        {-1,0},
        {0,1},
        {0,-1}
    };
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        rows = heights.length;
        cols = heights[0].length;

        boolean[][] pacific = new boolean[rows][cols];
        boolean[][] atlantic = new boolean[rows][cols];

        //Start from pacific and atlantic in same loop
        for(int r =0;r<rows;r++){
            dfs(heights,r,0,pacific);
            dfs(heights,r,cols-1,atlantic);
        }

        for(int c =0;c<cols;c++){
            dfs(heights,0,c,pacific);
            dfs(heights,rows-1,c,atlantic);
        }

        List<List<Integer>> res = new ArrayList<>();
        for(int r = 0; r< rows;r++){
            for(int c =0; c< cols;c++){
                if(pacific[r][c] && atlantic[r][c])
                    res.add(Arrays.asList(r,c));
            }
        }

        return res;
    }

    private void dfs(int[][] heights, int r , int c, boolean[][] visited){

        if(visited[r][c]) return;

        visited[r][c] = true;

        for(int[] dir: directions){
            int nr = r + dir[0];
            int nc = c + dir[1];

            if(nr<0 || nr >= rows || nc<0 || nc >= cols || heights[nr][nc] < heights[r][c]) continue;

            dfs(heights,nr,nc,visited);
        }
    }

}
