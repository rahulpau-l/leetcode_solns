class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
       
        before = None
        first = head
        second = head.next

        while second:
            # get the node after second and save it
            after = second.next
            #link it to the first one
            second.next = first
            first.next = before
            before = first
            #move the first pointer
            first = second
            #move the second ppointer
            second = after

        return first