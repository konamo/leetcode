void swap(char *s, int left, int right)
{
    char t = s[left];
    s[left] = s[right];
    s[right] = t;
    return;
}



void reverseString(char* s, int sSize)
{
    int left = 0;
    int right = sSize;

    while (left < right) {
        swap(s, left, right);
        left++;
        right--;
    }

}
