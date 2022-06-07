#define MIN(a, b) ((a) < (b) ? (a) : (b))

int minPathSum(int** grid, int gridSize, int* gridColSize)
{
    for (int ii = 0; ii < gridSize; ii++) {
        for (int jj = 0; jj < *gridColSize; jj++) {
            if (ii == 0 && jj == 0) {
                NULL;
            } else if (ii == 0) {
                grid[ii][jj] += grid[ii][jj - 1];
            } else if (jj == 0) {
                grid[ii][jj] += grid[ii - 1][jj];
            } else {
                grid[ii][jj] += MIN(grid[ii - 1][jj], grid[ii][jj - 1]);
            }
        }
    }

    return grid[gridSize -1][*gridColSize - 1];
}
