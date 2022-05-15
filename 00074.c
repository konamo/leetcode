#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>


// this solution works on mac, but doesn't work on leetcode
bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target)
{
    int *array = (int*)matrix;
    int left = 0;
    int right = matrixSize * *matrixColSize - 1;


    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (array[mid] == target) {
            return true;
        } else if (array[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return false;
}


int main()
{
    int matrix[3][4] = {
        {1, 3, 5, 7},
        {10, 11, 16, 20},
        {23, 30, 34, 60},
    };

    int size = 4;
    printf("%d \n", searchMatrix(matrix, 3, &size, 3));

    return 0;
}
