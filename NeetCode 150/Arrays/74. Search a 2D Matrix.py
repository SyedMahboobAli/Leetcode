class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = ( n * m ) - 1

        while l <= r:
            mid = (l+r) // 2
            #converting mid to row and col. Always using column, Row // and col %
            row = mid // m
            col = mid % m
            
            if(target == matrix[row][col]):
                return True
            elif(target < matrix[row][col]):
                r = mid - 1
            else:
                l = mid + 1
        return False
