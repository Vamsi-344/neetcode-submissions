# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def linkedListToList(self, l: Optional[ListNode]) -> List:
        res = []
        while l != None:
            res.append(l.val)
            l = l.next
        return res

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        finalList = []
        for i in lists:
            finalList.extend(self.linkedListToList(i))
        finalList = sorted(finalList)
        res = ListNode()
        curr = res
        for i in finalList:
            node = ListNode(i)
            curr.next = node
            curr = curr.next
        return res.next