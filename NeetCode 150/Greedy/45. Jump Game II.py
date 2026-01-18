class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_end = 0
        curr_farthest =0

        for i in range(len(nums) -1):
            #update farthest we can reach
            curr_farthest = max(curr_farthest,i+nums[i])
            #if we reach the end of the cur jump
            if i == curr_end:
                jumps+=1
                curr_end = curr_farthest
        return jumps
