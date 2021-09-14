# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        index = 1
        while current != None:
            if index % 2 == 1 and current.next != None:
                temp = current.val
                current.val = current.next.val
            elif index % 2 == 0:
                current.val = temp
            index += 1
            current = current.next
        return head