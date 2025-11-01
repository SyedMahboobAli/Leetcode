class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #step 1: Transpose of a matrix
        n=len(matrix) # matrix is square nxn and it is only possible for square
        for i in range(n):
            for j in range(i+1,n): #j>1
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        #step 2: reverse rows, for anticlockwise reverse columns
        for row in matrix:
            row.reverse() # row[::-1] copies and reverses, row.reverse() does inplace reverse
        '''
        above 2 reverse are for rows, how to reverse column?
        (swap top row with bottom row)
        for i in range(n // 2):
            matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
        '''

        '''
        anticlockwise 90degree: transpose + reverse columns/swap rows
        180 degree: swap rows and reverse rows
        270 degree: anticlockwise 90 degree
        '''
        
        

