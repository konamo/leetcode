#include <stdio.h>
#include <string.h>


// solution 1: recursive
int uniquePaths (int m, int n)
{
    if (m == 1 || n == 1) {
        return 1;
    }

    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1);
}


// solution 2: bottom up
int uniquePaths (int m, int n)
{
    int path[m][n];

    for (int ii = 0; ii < m; ii++) {
        for (int jj = 0; jj < n; jj++) {
            if (ii == 0 || jj == 0) {
                path[ii][jj] = 1;
            } else {
                path[ii][jj] = path[ii - 1][jj] + path[ii][jj - 1];
            }
        }
    }

    return path[m - 1][n - 1];
}


// solution 2a: bottom up with optimization
int uniquePaths (int m, int n)
{
    int path[m + 1][n + 1];

    memset(path, 0, sizeof(path));
    // or path[1][0] = 1
    path[0][1] = 1;

    for (int ii = 1; ii <= m; ii++) {
        for (int jj = 1; jj <= n; jj++) {
            path[ii][jj] = path[ii - 1][jj] + path[ii][jj - 1];
        }
    }

    return path[m][n];
}

int main ()
{
    int p;

    p = uniquePaths(3, 7);
    printf("Paths: %d\n", p);

    p = uniquePaths(51, 9);
    printf("Paths: %d\n", p);

    return 0;
}
