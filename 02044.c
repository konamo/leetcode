// solution 1: brute force
int countMaxOrSubsets(int* nums, int numsSize)
{
    int max = -1;
    int or;
    int count;

    for (int bitmap = 0; bitmap < (1ull << numsSize); bitmap++) {
        or = 0;
        for (int ii = 0; ii < numsSize; ii++) {
            if ((1ull << ii) & bitmap) {
                or |= nums[ii];
            }
        }

        if (or > max) {
            max = or;
            count = 1;
        } else if (or == max) {
            count++;
        }
    }

    return count;
}



// solution 2: DP
// hard to understand!
int countMaxOrSubsets(int* nums, int numsSize)
{
    int max = 0;
    int dp[1ull << 17];

    memset(dp, 0, sizeof(dp));

    /*dp[i] means how many number of different non-empty subsets for number i.
     * dp presents the growing and exact result from empty subset to full A during the loop for a in A

      target is max(dp), or the OR operation of all elements in the nums.
      start point is dp[0] = 1.
      for each current result (k, v) in dp, increase dp[k|A[i]] by v, as k has v ways to make k|A[i] be there
      return dp[target]
      This solution is very straightforward and elegant. You can add print(dp) to get more idea.
      */
    dp[0] = 1;
    for (int ii = 0; ii < numsSize; ii++) {
        for (int jj = max; jj >= 0; jj--) {
            dp[jj | nums[ii]] += dp[jj];
        }
        max |= nums[ii];
    }

    return dp[max];
}

// solution 3: another DP
int countMaxOrSubsets(int* nums, int numsSize)
{
    int max = 0;
    int dp[1 << numsSize];
    int count = 0;

    for (int ii = 0; ii < numsSize; ii++) {
        max |= nums[ii];
    }

    // max = nums[0] | nums[1] | .. nums[n]
    // the max is our goal
    // for any substring whose OR == max, increase the counter by 1
    // dp[x] represents the OR of the bitmap on nums[]
    // dp[0b1110] = nums[1] OR nums[2] OR nums[3]
    //
    // DP algorithms:
    // dp[0b1110] = dp[0b1100] OR nums[1]
    // dp[0b1100] = dp[0b1000] OR nums[2]
    // ....
    dp[0] = 0;
    for (int bitmap = 1; bitmap < (1ull << numsSize); bitmap++) {
        int lowbit = bitmap & ~(bitmap - 1);
        int trailing_zero = 0;

        while (lowbit != (1ull << trailing_zero)) {
            trailing_zero++;
        }

        dp[bitmap] = dp[bitmap - lowbit] | nums[trailing_zero];

        if (dp[bitmap] == max) {
            count++;
        }
    }

    return count;
}


// solution 4: DFS
class Solution {
    
    int res = 0, target = 0;
    
    public int countMaxOrSubsets(int[] nums) {
        for (int num : nums)
            target |= num;
        
        dfs(nums, 0, 0);
        return res;
    }
    
    public void dfs(int[] nums, int idx, int mask) {
        if (mask == target) res++;
        
        for (int i = idx; i < nums.length; i++)
            dfs(nums, i + 1, mask | nums[i]);
    }
    
}

// solution 5: another DP
int subset(int* nums, int size, int goal, int mask)
{
    int ans = 0;

    if (size < 1) {
        return 0;
    }

    if (goal == (mask | nums[size - 1])) {
        ans = 1;
    }

    // + with and without current item
    return ans + subset(nums, size - 1, goal, mask) + subset(nums, size - 1, goal, mask | nums[size - 1]);
}

int countMaxOrSubsets(int* nums, int numsSize)
{
    int goal = 0;

    for (int ii = 0; ii < numsSize; ii++) {
        goal |= nums[ii];
    }

    return subset(nums, numsSize, goal, 0);
}
