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




bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target)
{
    if (matrix == NULL) {
        return false;
    }

    // start from left bottom corner
    int col = 0;
    int row = matrixSize - 1;

    while (col < *matrixColSize && row >= 0) {
        if(target == matrix[row][col]) {
            return true;
        } else if(target < matrix[row][col]) {
            row--;
        } else if(target > matrix[row][col]) {
            col++;
        }
    }
    return false;
}
