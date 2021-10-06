# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr is not None:
            # storing the next node
            nextTemp = curr.next
            # making the current node point to previous node
            curr.next = prev
            # for next iteration -> update previous node to current node & current node to next node
            prev = curr
            curr = nextTemp
            
        return prev
