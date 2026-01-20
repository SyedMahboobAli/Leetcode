class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0 # total gas balance. => total diff
        tank = 0 #current gas in tank
        start = 0 #starting index

        for i in range(len(gas)):
            diff = gas[i] - cost[i] #considering only diff
            total += diff
            tank += diff
        
            if tank < 0:
                start = i+1
                tank =0
        return start if total >=0 else -1
