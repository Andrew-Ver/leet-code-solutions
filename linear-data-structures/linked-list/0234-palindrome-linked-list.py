'''
    https://leetcode.com/problems/palindrome-linked-list/
'''


class ListNode():
    ...


def isPalindrome(head: ListNode) -> bool:
    s: list[int] = []
        
    while head:
        s.append(head.val)
        head = head.next
    
    return s == s[::-1]