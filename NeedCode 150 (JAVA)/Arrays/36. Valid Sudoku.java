class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character>[] row = new HashSet[9];
        HashSet<Character>[] col = new HashSet[9];
        HashSet<Character>[] grid = new HashSet[9];

        for(int i = 0;i<9;i++){
            row[i]= new HashSet<>();
            col[i] = new HashSet<>();
            grid[i] = new HashSet<>();
        }

        for (int i =0;i<9;i++){
            for(int j =0;j<9;j++){
                if (board[i][j] =='.') continue;
                
                char num = board[i][j];

                if(row[i].contains(num)) return false;
                row[i].add(num);

                if(col[j].contains(num)) return false;
                col[j].add(num);

                int grid_index= (i/3) *3+ (j/3);

                if(grid[grid_index].contains(num)) return false;
                grid[grid_index].add(num);
            }
        }
        return true;

    }
}
