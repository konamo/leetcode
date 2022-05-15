typedef struct {
    int *weight;
    int size;
} Solution;


Solution* solutionCreate(int* w, int wSize) {
    static Solution s;

    s.size = wSize;
    s.weight = malloc(sizeof(int) * wSize);
    memcpy(s.weight, w, sizeof(int) * wSize);

    for (int ii = 1; ii < wSize; ii++) {
        s.weight[ii] += s.weight[ii - 1];
    }
    srand(0);
    return &s;
}

int solutionPickIndex(Solution* obj) {
    int r = (rand() % (obj->weight[obj->size - 1])) + 1;

    printf("r %d\n", r);
    //binary search r
    int left = 0;
    int right = obj->size - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (obj->weight[mid] == r) {
            return mid;
        } else if (obj->weight[mid] > r) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

void solutionFree(Solution* obj) {
    free(obj->weight);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(w, wSize);
 * int param_1 = solutionPickIndex(obj);

 * solutionFree(obj);
*/
