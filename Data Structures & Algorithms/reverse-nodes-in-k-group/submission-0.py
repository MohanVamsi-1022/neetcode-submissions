# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return 
        tail =  head
        for _ in range(k):
            if not tail:
                return head
            tail = tail.next
        def reverse(curr,end):
            prev = None
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        new_head =  reverse(head,tail)
        head.next = self.reverseKGroup(tail,k)
        return new_head


        