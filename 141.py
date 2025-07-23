class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        one = head 
        two = head 

        while two is not None and two.next is not None: 
            one = one.next 
            two = two.next.next 
            if one == two:
                return True 
        return False