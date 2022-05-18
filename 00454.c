// TLC
int fourSumCount (int* nums1, int nums1Size, int* nums2, int nums2Size, int* nums3, int nums3Size, int* nums4, int nums4Size)
{
    int count = 0;

    int *pair = (int *)malloc(sizeof(int) * nums1Size * nums2Size);

    int pair1index = 0;
    for (int aa = 0; aa < nums1Size; aa++) {
        for (int bb = 0; bb < nums2Size; bb++) {
            pair[pair1index++] = nums1[aa] + nums2[bb];
        }
    }

    int *pair2 = (int *)malloc(sizeof(int) * nums3Size * nums4Size);
    int pair2index = 0;
    for (int aa = 0; aa < nums3Size; aa++) {
        for (int bb = 0; bb < nums4Size; bb++) {
            pair2[pair2index++] = nums3[aa] + nums4[bb];
        }
    }

    for (int aa = 0; aa < pair1index; aa++) {
        for (int bb = 0; bb < pair2index; bb++) {
            if (pair1[aa] + pair2[bb] == 0) {
                count++;
            }
        }
    }


    free(pair);
    free(pair2);
    return count;
}
