'''
    https://leetcode.com/problems/search-in-a-binary-search-tree/
'''


class TreeNode():
    ...


def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    def search(node: TreeNode, val=val) -> TreeNode:
        if (node.val == val):
            return node
        elif (val < node.val and node.left):
            return search(node.left)
        elif (val > node.val and node.right):
            return search(node.right)
        
    return search(root) or None
