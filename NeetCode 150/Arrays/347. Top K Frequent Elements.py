#Solution 1: heap best beats 100%
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= Counter(nums)
        heap=[]
        for num,freq in d.items():
            heapq.heappush(heap,(freq,num)) # adding tuple the heap
            if (len(heap) > k): #always the heap is len k, and we are popping least freq num, so always we have max freq number in heap
                heapq.heappop(heap)
        return [tup[1] for tup in heap]


#Solution 2:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        # Step 1: Count frequency
        for i in nums:
            if i in d:# or d[i]=1+d.get(i,0)
                d[i]+=1
            else:
                d[i]=1
        # use d=Counter(nums)
        frequency=[[] for _ in range(len(nums)+1)]
#We're using bucket sort where the index of the outer list represents the frequency of elements.
#The maximum frequency any number can have is if all numbers are the same.
#So, in the worst case, one number appears len(nums) times.

        # Step 2: Create frequency table where index = frequency
        for num,freq in d.items():
            frequency[freq].append(num)
        
        # Step 3: Collect top k frequent elements
        res=[]
        for i in range(len(frequency)-1,0,-1):
            for num in frequency[i]:
                res.append(num)
                if(len(res)==k):
                    return res


        
