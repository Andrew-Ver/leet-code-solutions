'''
	https://leetcode.com/problems/group-anagrams/

	Given an array of strings strs, group the anagrams together. You can return the answer in any order.
	An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
	typically using all the original letters exactly once.
'''

def groupAnagrams(strs: list[str]) -> list[list[str]]:
        from collections import Counter, defaultdict
        '''
            If the same collections of letters have been seen
            add the word to a group with the others
        '''
        ans_groups: defaultdict[list] = defaultdict(list)
        mapping: dict = {}
        n: int = 0
            
        for word in strs:
            counts = frozenset(Counter(word).items())
            if counts in mapping:
                ans_groups[mapping[counts]].append(word)
            else:
                mapping[counts] = n
                ans_groups[n].append(word)
                n += 1
            
        return ans_groups.values()
