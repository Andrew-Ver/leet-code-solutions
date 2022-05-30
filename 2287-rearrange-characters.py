'''
    https://leetcode.com/problems/rearrange-characters-to-make-target-string/
'''
from collections import Counter


def rearrangeCharacters(s: str, target: str) -> int:
    s_counter = Counter(s)

    max_copies = 0

    for letter, req in Counter(target).items():
        d = divmod(s_counter[letter], req)[0]
        if d == 0 or letter not in s_counter:
            return 0
        
        if max_copies == 0:
            max_copies = d
        else:
            max_copies = min(d, max_copies)

    return max_copies


print(rearrangeCharacters("wvu", "tu"))