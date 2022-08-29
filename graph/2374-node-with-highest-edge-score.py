'''
    https://leetcode.com/problems/node-with-highest-edge-score/
'''


def edgeScore(edges: list[int]) -> int:
    from collections import defaultdict
    
    edge_scores: dict[int, int] = defaultdict(int)
        
    for i, n in enumerate(edges):
        edge_scores[n] += i
    
    max_score = max(edge_scores.values()) or 0
    
    return min(n for n, s in edge_scores.items() if (s == max_score))