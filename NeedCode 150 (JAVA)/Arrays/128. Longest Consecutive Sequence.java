//Key Idea
//Only start counting when num - 1 does not exist, meaning the number is the start of a sequence. and check only nums_set
class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> nums_set = new HashSet<>();

        for(int num:nums){
            nums_set.add(num);
        }

        int max= 0;
        for(int num:nums_set){
            if(!nums_set.contains(num-1)){
            int curr_num = num;
            int curr_streak = 1;

            while(nums_set.contains(curr_num+1)){
                curr_num = curr_num+1;
                curr_streak += 1;
            }

            max = Math.max(curr_streak,max);

            }
        }
        return max;
    }
}
