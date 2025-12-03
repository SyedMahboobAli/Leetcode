class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #The speed of the car fleet is the minimum speed of any car in the fleet. If a faster car catches up to a slower car ahead of it, it becomes part of the same fleet and inherits the slower car’s speed.
'''
✔️ Sorting by position is ALWAYS correct
✔️ High speed at end does NOT break the algorithm
✔️ A fastest car behind will still be processed after the slower car in its front, so it would join that fleet if needed. and also We sort cars from closest to target → farthest from target so these cars would reach target first so the last car, even if it is fast cannot join the fleet. So sort by pos is correct. 

'''

        #Solution 1: stack, more memory stack O(n)
        cars = sorted(zip(position,speed), reverse=True)

        stack = [] # holds times of fleets

        for pos,spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
            # else it joins the fleet ahead (do nothing). Also note that if next time is greater other left times will also be greater since the cars is sorted in reverse order
        return len(stack)

        #solution 2: no stack, var:prev_time and fleet_count, memory optimized, but stack is best for runtime
        cars = sorted(zip(position,speed), reverse = True)
        
        prev_time= 0
        fleets = 0

        for pos,spd in cars:
            time = (target-pos) / spd
            if time > prev_time:
                fleets+=1
                prev_time = time
            #if time is less, it merges with the fleet
        return fleets
        
