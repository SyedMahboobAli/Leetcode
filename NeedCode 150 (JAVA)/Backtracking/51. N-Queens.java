class Solution {
    private List<List<String>> res = new ArrayList<>();
    private char[][] board;
    private boolean[] cols;
    private boolean[] diag1;
    private boolean[] diag2;

    public List<List<String>> solveNQueens(int n) {
        board = new char[n][n];
        cols = new boolean[n];
        diag1 = new boolean[2 * n - 1]; // row - col + (n - 1)
        diag2 = new boolean[2 * n - 1]; // row + col

        for (char[] row : board) {
            Arrays.fill(row, '.');
        }

        backtrack(0, n);
        return res;
    }

     private void backtrack(int row, int n) {
        if (row == n) {
            List<String> current = new ArrayList<>();
            for (char[] r : board) {
                current.add(new String(r));
            }
            res.add(current);
            return;
        }

        for (int col = 0; col < n; col++) {
            int d1 = row - col + (n - 1);
            int d2 = row + col;

            if (cols[col] || diag1[d1] || diag2[d2]) continue;

            board[row][col] = 'Q';
            cols[col] = true;
            diag1[d1] = true;
            diag2[d2] = true;

            backtrack(row + 1, n);

            board[row][col] = '.';
            cols[col] = false;
            diag1[d1] = false;
            diag2[d2] = false;
        }
    }
}
