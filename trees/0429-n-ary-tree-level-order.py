'''
    https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''


class Node():
    ...


def levelOrder(root: Node) -> list[list[int]]:
    from collections import deque, defaultdict
    levels: dict[list[int]] = defaultdict(list)

    explore: list[tuple[int, int]] = deque([])
    if root:
        levels[0].append(root.val)
        explore.append((root, 0))
        
    while explore:
        NODE, LVL = explore.popleft()
        
        for child in NODE.children:
            levels[LVL+1].append(child.val)
            explore.append((child, LVL+1))
            
    return levels.values()

