class Solution {
    private final int[][] directions = {
        {1,0},
        {-1,0},
        {0,1},
        {0,-1}
    };
    public boolean exist(char[][] board, String word) {
        for(int r = 0; r<board.length; r++){
            for(int c = 0; c<board[0].length;c++){
                if(dfs(board,word,0,r,c))
                    return true;
            }
        }
        return false;
    }

    private boolean dfs(char[][] board, String word, int index, int r, int c){
        if(index == word.length()) return true;

        if(r<0 || r>= board.length || c<0 || c>=board[0].length || word.charAt(index) != board[r][c])
            return false;

        char temp = board[r][c];

        board[r][c] = '#';
        for(int[] dir : directions){
            int nr = r + dir[0];
            int nc = c + dir[1];

            if(dfs(board,word,index+1,nr,nc)){
                board[r][c] = temp; //restore
                return true;

            }
                
        }

        board[r][c] = temp; //backtrack
        return false;

    }
}
