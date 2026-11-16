# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeMap = {}
        count = 0
        curr = head
        while curr != None:
            nodeMap[count] = curr
            count += 1
            curr = curr.next
        newIndexMap = []
        for i in range(count//2 + 1):
            if i == 0:
                newIndexMap.append(i)
            else:
                if count-i == i:
                    newIndexMap.append(i)
                else:
                    newIndexMap.append(count-i)
                    newIndexMap.append(i)
        newHead = ListNode()
        curr = newHead
        for i in newIndexMap:
            node = nodeMap[i]
            node.next = None
            curr.next = node
            curr = curr.next
        while newHead != None:
            newHead = newHead.next