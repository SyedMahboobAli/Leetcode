class Solution {
    private int rows,cols;
    private int[][] directions = {
        {1,0},
        {-1,0},
        {0,1},
        {0,-1},
    };
    public void solve(char[][] board) {
        if(board == null || board.length == 0) return;
        rows= board.length;
        cols = board[0].length;

        for(int r = 0;r<rows;r++){
            dfs(board,r,0);
            dfs(board,r,cols-1);
        }

        for (int c =0;c<cols;c++){
            dfs(board,0,c);
            dfs(board,rows-1,c);
        }

        for(int r=0;r<rows;r++){
            for(int c =0;c<cols;c++){
                //Ensure first 'O' to 'X' is done or use else if in next line. Since if 'T' becomes 'O' then that 'O' becomes 'X' which is wrong
                if(board[r][c] == 'O')
                    board[r][c] = 'X';
                if(board[r][c] == 'T')
                    board[r][c] = 'O';

            }
        }
    }

    private void dfs(char[][] board,int r,int c){
        if(r<0 || r>=rows || c<0 || c>=cols || board[r][c] != 'O')
            return;

        board[r][c] = 'T';
        for(int[] dir : directions){
            int nr = r+dir[0];
            int nc = c+dir[1];

            dfs(board,nr,nc);
        }
    }
}
