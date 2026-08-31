# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:   
        output = ListNode()

        curr1 = list1
        curr2 = list2
        new = output

        while curr1 and curr2:
            
            if curr1.val < curr2.val:
                new.next = curr1
                curr1 = curr1.next
            else:
                new.next = curr2
                curr2 = curr2.next

            new = new.next
        
        if not curr1 and curr2:
                new.next = curr2
        else:
            new.next = curr1
        
        return output.next