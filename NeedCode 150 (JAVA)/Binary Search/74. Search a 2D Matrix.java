class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int l = 0, n = matrix.length, m = matrix[0].length;
        int r = m * n -1;
        while(l<=r){
            int mid = (l+r)/2;
            //use column length to calculate row and col
            int row = mid/m, col = mid%m;
            if (target == matrix[row][col])
                return true;
            else if (target > matrix[row][col])
                l = mid + 1;
            else
                r = mid - 1;
        }
        return false;
    }
}
