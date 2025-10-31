class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]: #for [] and [[]] coz in [[]] when we travese through cols we get indexnotfound
            return

        n,m=len(matrix),len(matrix[0])
        # Check if the first row or first column should be zeroed
        first_row_has_zero = any(matrix[0][j]==0 for j in range(m))
        first_column_has_zero = any(matrix[i][0]==0 for i in range(n))

        # Use the first row and first column as marker arrays
        for i in range(1,n): #start traversal from 1
            for j in range(1,m): #start traversl from 1
                if(matrix[i][j]==0):
                    matrix[i][0]=0
                    matrix[0][j]=0

        # Zero out cells based on row and column markers
        for i in range(1,n):
            for j in range(1,m):
                if(matrix[i][0]==0 or matrix[0][j]==0):
                    matrix[i][j]=0
        
        # Finally, handle the first row and first column
        if first_row_has_zero:
            for j in range(m):
                matrix[0][j]=0

        if first_column_has_zero:
            for i in range(n):
                matrix[i][0]=0 

        
