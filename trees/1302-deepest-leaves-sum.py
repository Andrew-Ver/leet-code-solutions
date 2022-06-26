class TreeNode():
    ...


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.deepest_lvl = float('-inf')
        self.deepest_sum = 0
        
        def traverse(root: TreeNode, lvl=0) -> None:
            if not root.left and not root.right:
                if lvl == self.deepest_lvl:
                    self.deepest_sum += root.val
                elif lvl > self.deepest_lvl:
                    self.deepest_lvl = lvl
                    self.deepest_sum = root.val
                return 
            else:
                if root.left:
                    traverse(root.left, lvl+1)
                if root.right:
                    traverse(root.right, lvl+1)
        traverse(root)
        return self.deepest_sum

        