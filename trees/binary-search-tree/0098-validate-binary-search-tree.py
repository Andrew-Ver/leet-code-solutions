'''
    https://leetcode.com/problems/validate-binary-search-tree/
'''


class TreeNode():
    ...


def isValidBST(root: TreeNode) -> bool:
    explore: list[tuple[TreeNode, int, int]] = []
        
    if root.left:
        explore.append((root.left, float('-inf'), root.val))
    if root.right:
        explore.append((root.right, root.val, float('inf')))
    
    while explore:
        node, L_range, R_range = explore.pop()
        if not (L_range < node.val < R_range):
            return False
        '''
            Update ranges each time
            For left subtrees the right bound is the smallest to this point
            For right subtrees the left bound is the largest to this point
        '''
        if node.left:
            explore.append((node.left, L_range, min(R_range, node.val)))
            
        if node.right:
            explore.append((node.right, max(L_range, node.val), R_range))
            
    return True