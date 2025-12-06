class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 #it is not 0, be careful. 
        r = max(piles) 
        min_k = r
        while l<=r:
            k = (l + r) // 2 
            # For each pile, compute how many hours it takes at speed k
            total_time = 0
            for p in piles:
                total_time += math.ceil(p/k) #or other way for ceil is  (p + (k-1)) // k. This way we are not adding k and instead k-1 to pile and getting exact value we need using //
            if total_time <= h:
                min_k = k  # Update the best (minimum) valid speed found so far. It is always min as we are moving left. and if more, we are only updating l and not min_k
                r = k - 1
            else:
                l = k + 1
        return min_k
