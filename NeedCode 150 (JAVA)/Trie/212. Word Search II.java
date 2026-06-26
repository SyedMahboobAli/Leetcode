class Solution {
    private class TrieNode{
        TrieNode[] children = new TrieNode[26];
        String word; //Stores the word at the terminal node;
    }

    private TrieNode root = new TrieNode();
    private List<String> result = new ArrayList<>();
    private static final int[][] directions = {
        {1,0},
        {-1,0},
        {0,1},
        {0,-1},
    };

    public List<String> findWords(char[][] board, String[] words) {
        for(String s: words){
        insert(s);
        }

        int m = board.length;
        int n = board[0].length;

        for(int i =0 ;i<m;i++){
            for(int j = 0; j<n;j++){
                dfs(board,i,j,root);
            }
        }
        return result;
    }

    private void insert(String word){
        TrieNode node = root;

        for(char c: word.toCharArray()){
            int idx = c - 'a';

            if(node.children[idx] == null)
                node.children[idx] = new TrieNode();
            
            node = node.children[idx];

        }

        node.word = word;
    }

    private void dfs(char[][] board, int r, int c, TrieNode node){

        char ch = board[r][c];

        TrieNode  next = node.children[ch - 'a'];

        if(next == null) return;

        if(next.word != null){
            result.add(next.word);
            next.word = null;
        }

        board[r][c]= '#';

        for(int[] dir : directions){
            int nr = r + dir[0];
            int nc = c + dir[1];

            if(nr >= 0 && nr < board.length && nc >= 0 && nc < board[0].length && board[nr][nc] != '#'){
                dfs(board,nr,nc,next);
            }
        }

        board[r][c] = ch;

    }
}
