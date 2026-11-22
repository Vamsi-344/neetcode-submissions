# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getNum(self, l: Optional[ListNode]) -> int:
        res = 0
        count = 0
        while l != None:
            res += l.val * (10**count)
            count += 1
            l = l.next
        return res 
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resSum = self.getNum(l1) + self.getNum(l2)
        sumStr = str(resSum)[::-1]
        head = ListNode()
        curr = head
        for i in sumStr:
            node = ListNode(i)
            curr.next = node
            curr = curr.next
        return head.next