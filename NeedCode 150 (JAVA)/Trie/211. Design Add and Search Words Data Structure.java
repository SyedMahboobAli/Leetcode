class WordDictionary {


    private class TrieNode{
        TrieNode[] children = new TrieNode[26];
        boolean endofWord;
    }
     
    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode node = root;

        for(char c : word.toCharArray()){
            int idx = c - 'a';
            if(node.children[idx] == null)
                node.children[idx] = new TrieNode();
            node = node.children[idx];
        }
        node.endofWord = true;
        
    }
    
    public boolean search(String word) {
        return dfs(word,0,root);
    }

    private boolean dfs(String word, int index, TrieNode node){
        if (node == null) return false;
        if (word.length() == index) return node.endofWord;

        char c = word.charAt(index);
        if(c =='.'){
            for(TrieNode child: node.children){
                if (dfs(word, index+1, child))
                    return true;
            }
            return false;
        }
        else{
            int idx = c - 'a';
            return dfs(word, index+1, node.children[idx]);
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
