class Solution:
    def sortColors2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for ii in nums:
            if ii == 0:
                red += 1
            elif ii == 1:
                white += 1
            elif ii == 2:
                blue += 1
                
        for ii in range(red):
            nums[ii] = 0
            
        for ii in range(red, red + white):
            nums[ii] = 1
            
        for ii in range(red + white, red + white + blue):
            nums[ii] = 2
            
        return 
                    
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """  
        zero = 0
        second = len(nums) - 1
        ii = 0
        
        while ii <= second:
            while nums[ii] == 2 and ii < second:
                nums[ii], nums[second] = nums[second], nums[ii]
                second -= 1
            
            while nums[ii] == 0 and ii > zero:
                nums[ii], nums[zero] = nums[zero], nums[ii]
                zero += 1
                
            ii += 1
        return

    def sortColors3(self, nums):
        # Just like the Lomuto partition algorithm usually used in quick sort.
        # We keep a loop invariant that [0,i) [i, j) [j, k) are 0s, 1s and 2s sorted in place for [0,k).
        # Here ")" means exclusive. We don't need to swap because we know the values we want.
        i = j = 0
        for k in xrange(len(nums)):
            v = nums[k]
            nums[k] = 2
            if v < 2:
                nums[j] = 1
                j += 1
            if v == 0:
                nums[i] = 0
                i += 1

    // one pass in place solution
    void sortColors(int A[], int n) {
        int n0 = -1, n1 = -1, n2 = -1;
        for (int i = 0; i < n; ++i) {
            if (A[i] == 0) 
            {
                A[++n2] = 2; A[++n1] = 1; A[++n0] = 0;
            }
            else if (A[i] == 1) 
            {
                A[++n2] = 2; A[++n1] = 1;
            }
            else if (A[i] == 2) 
            {
                A[++n2] = 2;
            }
        }
    }

def main():
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    print(nums)
    return



if __name__ == '__main__':
    main()
