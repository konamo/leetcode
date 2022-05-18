

// solution 1: brute force
//
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int maxArea(int* height, int heightSize)
{
    int area = 0;

    for (int ii = 0; ii < heightSize - 1; ii++) {
        for (int jj = ii + 1; jj < heightSize; jj++) {
            area = MAX(area, (jj - ii) * MIN(height[ii], height[jj]));
        }
    }

    return area;
}



// solution 2
int maxArea (int* heights, int n)
{
    int water = 0;
    int left = 0;
    int right = n - 1;


    while (left < right) {
        int h = MIN(heights[left], heights[right]);
        int w = (right - left) * h;

        water = MAX(w, water);

        while (heights[left] <= h && left < right)
            left++;
        while (heights[right] <= h && left < right)
            right--;
    }

    return water;
}
