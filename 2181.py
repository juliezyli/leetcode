def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        right = curr
        while right:
            sum = 0 
            while right.val != 0:
                sum += right.val
                right = right.next 
            curr.val = sum 
            right = right.next
            curr.next = right 
            curr = curr.next
        return head.next 