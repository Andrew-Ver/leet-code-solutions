'''
    https://leetcode.com/problems/search-suggestions-system/submissions/
'''


def suggestedProducts(products: list[str], searchWord: str) -> list[list[str]]:
    from collections import defaultdict

    prefixes = defaultdict(list)
    products.sort()
    
    for p in products:
        for i in range(1, len(p)+1):
            if len(prefixes[p[:i]]) < 3:
                prefixes[p[:i]].append(p)

    return [prefixes[searchWord[:i]] for i in range(1, len(searchWord)+1)]