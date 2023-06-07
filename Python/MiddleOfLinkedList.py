# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # declaring fast and slow pointer
        fast = slow = head
        # increment fast ptr 2x times of slow pointer
        # when fast ptr reaches the end -> slow ptr will be at the mid-node of the linked-list
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
