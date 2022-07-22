'''
	https://leetcode.com/problems/reverse-linked-list-ii/
'''

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        start_interval_node: ListNode = None
        end_interval_node: listNode = None
        curr: int = 1
        curr_node: ListNode = head
            
        # Reversed node sublist
        # update the "interval" for each node left <= n <= right
        hold_node: ListNode = None
        
        while curr_node:
            if left <= curr <= right:
                # The new hold node becomes current node val
                # and its next node is the prev hold node
                hold_node = ListNode(curr_node.val, hold_node)
                
            if curr == (left-1):
                start_interval_node = curr_node
            if curr == right:
                end_interval_node = curr_node.next
                
            curr_node = curr_node.next
            curr += 1
    
        # Merge interval from start_interval_node
        if start_interval_node:
            start_interval_node.next = hold_node
        
        #handle edge case of interval starting from the 1st node
        if left == 1:
            head = hold_node
        
        while hold_node.next:
            hold_node = hold_node.next
        hold_node.next = end_interval_node
        
        return head
