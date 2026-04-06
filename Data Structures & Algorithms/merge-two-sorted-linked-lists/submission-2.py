# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = result = None
        if not list1:
            return list2
        elif not list2:
            return list1
        while list1 and list2:
            little = min(list1.val, list2.val)
            if not result:
                result = ListNode(little)
                head = result
            else:
                result.next = ListNode(little)
                result = result.next
            if list1.val == little:
                list1 = list1.next
            else:
                list2 = list2.next
        if list1:
            result.next = list1
        elif list2:
            result.next = list2
        return head