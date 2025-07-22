class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import Counter # creates an iterable of counts 
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        curr = root 
        def traverse(curr):
            if curr:
                lst.append(curr.val)
                traverse(curr.left)
                traverse(curr.right)
        
        traverse(curr)
        count = Counter(lst)
        maximum = 0 
        for i in lst:
            maximum = max(maximum, count[i])
        final = []
        for i in lst:
            if count[i] == maximum:
                final.append(i)
        return list(set(final))