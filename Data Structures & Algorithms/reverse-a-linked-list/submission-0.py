# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

       if not head:
        return None

       node = []
       curr = head

       while curr:
        node.append(curr)
        curr = curr.next

       for i in range(len(node) - 1, 0, -1):
        node[i].next = node[i-1]

       node[0].next = None

       return node[-1] 