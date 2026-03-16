# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        stack=[]
        while current:
            while stack and current.val>stack[-1].val:
                stack.pop()
            stack.append(current)
            current=current.next
        
        dummy=ListNode(0)
        ptr=dummy

        for node in stack:
            ptr.next=node
            ptr=node
        ptr.next=None
        return dummy.next
