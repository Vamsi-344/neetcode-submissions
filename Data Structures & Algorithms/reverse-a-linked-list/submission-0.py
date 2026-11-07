# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        valList = []
        while head != None:
            valList.append(head.val)
            head = head.next
        valList = valList[::-1]
        if valList == []:
            return head
        else:
            newListHead = ListNode()
            curr = newListHead
            for i in valList:
                node = ListNode(val=i, next=None)
                curr.next = node
                curr = curr.next
            newListHead = newListHead.next
            return newListHead