//JAVA
public class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        return false;
    }
}
//python
//class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))<len(nums)
