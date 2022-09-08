'''
    https://leetcode.com/problems/binary-tree-inorder-traversal/
'''


class TreeNode:
    ...


def inorderTraversal(root: TreeNode) -> list[int]:
    ans: list[int] = []
        
    def rec_traverse(node: TreeNode) -> None:
        if not node:
            return
        else:
            rec_traverse(node.left)
            ans.append(node.val)
            rec_traverse(node.right)
    
    rec_traverse(root)        
        
    return ans