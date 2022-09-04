'''
    https://leetcode.com/problems/removing-stars-from-a-string/
'''


def removeStars(s: str) -> str:
    stack: list[str] = []
        
    for c in s:
        if c == '*':
            stack.pop()
        else:
            stack.append(c)
    
    return ''.join(stack)