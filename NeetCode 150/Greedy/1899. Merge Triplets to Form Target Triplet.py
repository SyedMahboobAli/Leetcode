class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tx,ty,tz= target
        found_x = found_y = found_z = False

        for x,y,z in triplets:
            # Skip invalid triplets
            if x>tx or y>ty or z>tz:
                continue
            
            if x == tx:
                found_x = True
            if y == ty:
                found_y = True
            if z == tz:
                found_z = True
            
        return found_x and found_y and found_z

