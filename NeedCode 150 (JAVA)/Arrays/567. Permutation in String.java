class Solution {
    public boolean checkInclusion(String s1, String s2) {

        HashMap<Character,Integer> countS1 = new HashMap<>();

        for(char c: s1.toCharArray()){
            countS1.put(c,countS1.getOrDefault(c,0)+1);
        }

        HashMap<Character,Integer> countS2 = new HashMap<>();
        int l=0, n1 = s1.length();
        for(int r=0;r<s2.length();r++){
            char c = s2.charAt(r);
            countS2.put(c,countS2.getOrDefault(c,0)+1);
            while((r-l+1)>n1){
                c= s2.charAt(l);
                countS2.put(c,countS2.get(c)-1);
                if(countS2.get(c)==0){
                    countS2.remove(c);
                }
                l++;
            }
            if(countS1.equals(countS2))
                return true;
        }
        return false;
    }
}
