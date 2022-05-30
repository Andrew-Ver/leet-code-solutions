'''
    https://leetcode.com/problems/rearrange-characters-to-make-target-string/
'''


def maxProduct(words: list[str]) -> int:
    words_set = {w: set(w) for w in sorted(words, key=len, reverse=True)}
    max_product = 0

    for first_word in words_set:
        for second_word in words_set:
            if first_word != second_word and not (words_set[first_word].intersection(words_set[second_word])):
                max_product = max(max_product, len(first_word) * len(second_word))
                break

    return max_product

    
print(maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))