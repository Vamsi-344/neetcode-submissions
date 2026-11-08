# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        numsList = []
        while list1 != None:
            numsList.append(list1.val)
            list1 = list1.next
        while list2 != None:
            numsList.append(list2.val)
            list2 = list2.next
        numsList = sorted(numsList)
        head = ListNode()
        curr = head
        for i in numsList:
            node = ListNode(val=i, next=None)
            curr.next = node
            curr = curr.next
        return head.next
        