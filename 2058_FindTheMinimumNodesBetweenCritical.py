# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        indexNode = 2
        firstLocal = lastLocal = 0
        lastValue = head.val
        head = head.next
        output = [-1,-1]
        while head:
            if head.val < lastValue and head.next and head.val < head.next.val or head.val > lastValue and head.next and head.val > head.next.val:
                if firstLocal == 0: 
                    firstLocal = indexNode
                else:
                    output[0] = min(output[0], indexNode-lastLocal) if output[0] != -1 else indexNode-lastLocal
                    output[1] = indexNode-firstLocal
                lastLocal = indexNode
            indexNode += 1
            lastValue = head.val
            head = head.next
        return output