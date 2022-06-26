'''
    https://leetcode.com/problems/all-paths-from-source-to-target/submissions/
'''


from collections import defaultdict


def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    adjacency: dict[list[int]] = defaultdict(list)
    
    # Initalize adjacency list
    for i, n in enumerate(graph):
        adjacency[i] = n

    total_paths: list[list[int]] = []

    explore: list[int] = [[0, [0]]]
    TARGET: int = len(graph)-1

    while explore:
        NODE, PATH = explore.pop()

        if NODE == TARGET:
            #print(f'Reached end! Curr path: {PATH}\n')
            total_paths.append(PATH)
        else:
            # Enqueue neighbours w/ new path
            neighbours = [(neighbour, PATH+[neighbour]) 
                            for neighbour in adjacency[NODE]]
            explore.extend(neighbours)

    return total_paths


