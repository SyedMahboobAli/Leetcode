class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==0):
            return 0
        if(n==1):
            return nums[0]
        
        def rob_linear(arr):
            #can't use outer n because when I am calling function below the length there is n-1
            m=len(arr)
            #again I need return because when I am calling n-1, it can become 0 or 1
            if m==0:
                return 0
            if m==1:
                return arr[0]
            dp=[0]*m
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])
            for i in range(2,m):
                dp[i]=max(dp[i-1],arr[i]+dp[i-2])
            return dp[m-1]
        
        return max(rob_linear(nums[:-1]),rob_linear(nums[1:]))
