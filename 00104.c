/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

#define MAX(a, b) (((a) > (b)) ? (a) : (b))

int maxDepthHelper(struct TreeNode* node, int depth)
{
    if (node == NULL) {
        return depth;
    } else {
        return MAX(maxDepthHelper(node->left, depth + 1), maxDepthHelper(node->right, depth + 1));
    }
}

int maxDepth(struct TreeNode* root)
{
    return maxDepthHelper(root, 0);
}
