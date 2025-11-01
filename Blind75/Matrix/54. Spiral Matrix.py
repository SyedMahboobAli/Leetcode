class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            #below 2 loops condition not needed, coz it uses above condition from while
             # Traverse from left to right
            for j in range(left,right+1):
                res.append(matrix[top][j]) #here top exists, checked in while condition
            top+=1
            # Traverse from top to bottom
            for i in range(top,bottom+1):
                res.append(matrix[i][right]) #here right exists, checked in while condition
            right-=1

            #not sure bottom exists, top can become more than bottom, so condition needed
            if (top <=bottom):
                for j in range(right,left-1,-1):
                    res.append(matrix[bottom][j])
                bottom-=1
            #not sure if left exists, right can be less than left, so condition needed
            if (left <= right):
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
        
        return res
