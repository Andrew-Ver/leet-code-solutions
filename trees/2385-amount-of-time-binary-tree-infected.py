'''
    https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
'''
from collections import defaultdict


class TreeNode():
    ...


def amountOfTime(root: TreeNode, start: int) -> int:    
    neighbours: dict[str[set[int]]] = defaultdict(set)
    all_nodes: set[int] = set()
    explore: list[tuple[TreeNode, int]] = []
    
    if root:
        explore.append((root, None))
    
    while explore:
        node, prev = explore.pop()
        v = node.val
        
        all_nodes.add(v)
        
        if node.left:
            neighbours[v].add(node.left.val)
            explore.append((node.left, v))
        if node.right:
            neighbours[v].add(node.right.val)
            explore.append((node.right, v))
        if (prev != None):
            neighbours[v].add(prev)
    
    time_required: int = -1
    explore: list[set[int]] = [{start}]
        
    while all_nodes:
        vals = explore.pop()
        new: set[int] = set()
            
        for v in vals:
            all_nodes.remove(v)
            new.update({n for n in neighbours[v] if n in all_nodes})
            
        explore.append(new)
        time_required += 1
        
    return time_required