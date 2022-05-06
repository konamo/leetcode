int* decode(int* encoded, int encodedSize, int first, int* returnSize)
{
    int *decoded = (int*) malloc((encodedSize + 1) * sizeof(int));

    decoded[0] = first;
    for (int ii = 0; ii < encodedSize; ii++) {
        decoded[ii+1] = first ^ encoded[ii];
        first = decoded[ii+1];
    }

    *returnSize = encodedSize + 1;
    return decoded;
}
