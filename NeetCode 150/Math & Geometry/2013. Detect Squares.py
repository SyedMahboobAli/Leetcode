
class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)
        #points grouped by x cordinate
        self.points_by_x = defaultdict(set)
        

    def add(self, point: List[int]) -> None:
        x,y = point
        self.freq[(x,y)] += 1
        self.points_by_x[x].add(y)

    def count(self, point: List[int]) -> int:
        x,y = point
        res = 0 
        
        #Iterate over all points with same x
        for ny in self.points_by_x[x]:
            if ny == y:
                continue
            
            side = abs(y-ny)

            #check right square
            res += (self.freq[(x,ny)] * self.freq[(x+side, y)] * self.freq[(x+side,ny)])

            #check left square
            res += (self.freq[(x,ny)] * self.freq[(x-side, y)] * self.freq[(x-side,ny)])

        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
