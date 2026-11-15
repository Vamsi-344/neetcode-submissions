# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linkedListValues = []
        while head != None:
            linkedListValues.append(head.val)
            head = head.next
        linkedListValues.pop(len(linkedListValues)-n)
        head = ListNode()
        curr = head
        for i in linkedListValues:
            curr.next = ListNode(i)
            curr = curr.next
        return head.next