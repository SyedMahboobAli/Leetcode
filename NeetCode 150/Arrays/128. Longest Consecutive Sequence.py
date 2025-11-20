class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            # check if it's the start of a sequence
            if n-1 not in num_set:
                current_num = n
                current_streak = 1

                # count consecutive numbers
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest = max(longest,current_streak)

        return longest
