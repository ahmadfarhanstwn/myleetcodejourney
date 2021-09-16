# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        size = 0
        headkw = head
        while headkw:
            size += 1
            headkw = headkw.next
        stack = []
        index = 1
        if size % 2 == 0:
            while head:
                if index <= size/2:
                    stack.append(head.val)
                else:
                    if head.val != stack[-1]:
                        return False
                    else:
                        stack.pop(-1)
                index += 1
                head = head.next
        else:
            while head:
                if index <= size/2:
                    stack.append(head.val)
                elif index > (size/2)+1:
                    if head.val != stack[-1]:
                        return False
                    else:
                        stack.pop(-1)
                index += 1
                head = head.next
        return True