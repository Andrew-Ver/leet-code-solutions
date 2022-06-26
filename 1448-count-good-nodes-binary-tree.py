'''
    https://leetcode.com/problems/count-good-nodes-in-binary-tree/
'''

from dataclasses import dataclass
from collections import deque

@dataclass
class TreeNode():
    val: int
    left: any
    right: any

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def goodNodes(root: TreeNode) -> int:
    queue: list[int, int] = deque([(root, root.val)])
    
    good_nodes_ans: int = 0
    
    while queue:
        NODE, LARGEST = queue.popleft()
        
        if (NODE.val >= LARGEST):
            good_nodes_ans += 1
            LARGEST = NODE.val
        # Enqueue node and the largest node val to this point
        # (don't need to store the whole path)
        if NODE.left:
            queue.append((NODE.left, LARGEST))
        if NODE.right:
            queue.append((NODE.right, LARGEST))
        
    return good_nodes_ans