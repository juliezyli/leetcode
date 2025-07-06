from math import gcd 
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head 
        while curr and curr.next:
            a, b = curr.val, curr.next.val 
            greatest = gcd(a, b)
            new_node = ListNode(greatest)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        return head