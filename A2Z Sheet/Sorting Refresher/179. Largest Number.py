class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        numbers = [str(num) for num in nums]
        #insertion sort
        for i in range(1,len(nums)):
            curr = numbers[i]
            j = i - 1
            while j>=0 and curr + numbers[j] > numbers[j] + curr:
                numbers[j+1] = numbers[j]
                j-=1
            numbers[j+1] = curr
        
        if numbers[0] == "0": #to handle"00
            return "0"
        
        return "".join(numbers)
