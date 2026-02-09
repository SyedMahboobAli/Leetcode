class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        pos = defaultdict(list)
        
        for i, v in enumerate(nums2):
            pos[v].append(i)
        
        res = []
        for v in nums1:
            res.append(pos[v].pop())
        
        return res
