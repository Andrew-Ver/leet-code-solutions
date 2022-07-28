'''
	https://leetcode.com/problems/valid-anagram/
'''

def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s = Counter(s)
        
        for c, n in Counter(t).items():
            if n > s[c]:
                return False
        return True
