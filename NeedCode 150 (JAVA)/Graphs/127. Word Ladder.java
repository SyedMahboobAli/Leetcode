class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordset  = new HashSet<>(wordList);
        if(!wordset.contains(endWord)) return 0;

        //Pattern -> List of words matching that pattern
        Map<String, List<String>> patternMap = new HashMap<>();

        //Preprocess all the words in the dictionary
        for(String word: wordList){
            addPatterns(word,patternMap);
        }

        Queue<String> queue = new LinkedList<>();
        queue.offer(beginWord);

        Set<String> visited = new HashSet<>();
        visited.add(beginWord);

        int level = 1;

        while(!queue.isEmpty()){
            int size = queue.size();

            for(int s = 0; s<size; s++){
                String word = queue.poll();

                if(word.equals(endWord)) return level;

                char[] chars = word.toCharArray();

                for(int i = 0; i<chars.length; i++){
                    String pattern = word.substring(0,i) + "*" + word.substring(i+1);

                    List<String> neighbors = patternMap.getOrDefault(pattern,new ArrayList<>());

                    for(String neighbor: neighbors){
                        if(!visited.contains(neighbor)){
                            visited.add(neighbor);
                            queue.offer(neighbor);
                        }
                    }
                    //optional optimization :avoid re processing of this pattern
                    patternMap.put(pattern,new ArrayList<>());
                }
            }
            level++;
        }
        return 0;
    }

    private void addPatterns(String word, Map<String,List<String>> patternMap){
        for(int i = 0;i<word.length();i++){
            String pattern = word.substring(0,i) + "*" + word.substring(i+1);
            patternMap.computeIfAbsent(pattern, k-> new ArrayList<>()).add(word);
        }
    }
}
