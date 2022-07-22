'''
	https://leetcode.com/problems/reverse-linked-list/
'''


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        node: ListNode = None
            
        while head:
            node = ListNode(head.val, node)
            head = head.next
        
        return node
