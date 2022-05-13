

bool isPalindrome(char *s, int left, int right)
{
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}


bool validPalindrome(char * s)
{
    int left = 0;
    int right = strlen(s) - 1;


    while (left < right) {
        if (s[left] != s[right]) {
            return isPalindrome(s, left, right - 1) || isPalindrome(s, left + 1, right);
        }
        left++;
        right--;
    }
    return true;
}
