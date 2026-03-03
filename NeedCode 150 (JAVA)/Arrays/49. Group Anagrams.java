class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap <String,List<String>> map = new HashMap<>();

        for (String s: strs){
            int[] freq = new int[26];

            for (char c:s.toCharArray()){
                freq[c-'a']++;
            }

            StringBuilder keybuilder = new StringBuilder();

            for(int i:freq){
                keybuilder.append(i).append('#');
            }

            String key = keybuilder.toString();
            //We can also create string from char arr like:
            //char[] arr = s.toCharArray();
            //Array.sort(arr) : we can sort on char arr not string
            //String key = new String(arr);
            map.putIfAbsent(key,new ArrayList<>());
            map.get(key).add(s);


        }
        return new ArrayList<>(map.values());
    }
}
