class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        # Max heap using negative counts
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        queue = deque() #remaining_time,available_time

        time = 0
        while max_heap or queue:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # execute task
                if cnt < 0:
                    queue.append((cnt,time + n)) 
            # If task queue finished, push back to heap
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap,queue.popleft()[0])
        return time


