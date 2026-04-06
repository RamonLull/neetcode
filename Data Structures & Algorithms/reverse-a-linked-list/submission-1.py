# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # Save the rest of the list
            curr.next = prev       # Reverse the pointer
            
            # Move pointers forward for the next iteration
            prev = curr
            curr = next_node

        return prev  