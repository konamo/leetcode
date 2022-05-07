#define MAX(a, b) ((a) > (b) ? (a) : (b))

int matrixScore (int** grid, int gridSize, int* gridColSize)
{
    int row = gridSize;
    int col = *gridColSize;
    int res = (1 << (col - 1)) * row;

    for (int ii = 1; ii < col; ii++) {
        int cur = 0;
        for (int jj = 0; jj < row; jj++) {
            cur += grid[jj][ii] == grid[jj][0];
        }
        res += MAX(cur, row - cur) * (1 << (col - ii - 1));
    }


    return res;
}
