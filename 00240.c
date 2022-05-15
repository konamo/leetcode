bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target)
{
    if (matrix == NULL) {
        return false;
    }

    // start from top right corner
    int col = *matrixColSize - 1;
    int row = 0;

    while (col >= 0 && row < matrixSize) {
        if(target == matrix[row][col]) {
            return true;
        } else if(target < matrix[row][col]) {
            col--;
        } else if(target > matrix[row][col]) {
            row++;
        }
    }
    return false;
}
