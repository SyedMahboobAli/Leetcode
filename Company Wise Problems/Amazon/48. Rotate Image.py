class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Step1: transpose
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        #step 2: reverse rows:
        for row in matrix:
            row.reverse() #this does an inplace reverse
        
