# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        while curr!=None:
            count+=1
            curr=curr.next
        if count==n:
            return head.next
        c=count-n-1
        curr=head
        while curr!=None:
            if c==0:
                curr.next=curr.next.next
                break
            else:
                curr=curr.next
                c-=1
        return head