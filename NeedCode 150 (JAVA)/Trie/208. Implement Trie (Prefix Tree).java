class Trie {

    private class TrieNode{
        TrieNode[] children = new TrieNode[26];
        boolean endofWord;
    }

    private TrieNode root;
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
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
        TrieNode node = findNode(word);
        return node != null && node.endofWord;
    }
    
    public boolean startsWith(String prefix) {
        return findNode(prefix) != null;
    }

    private TrieNode findNode(String s){
        TrieNode node = root;

        for(char c : s.toCharArray()){
            int idx = c - 'a';
            if(node.children[idx] == null){
                return null;
            }
            node = node.children[idx];
        }
        return node;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
