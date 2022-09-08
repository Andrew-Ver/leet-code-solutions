'''
    https://leetcode.com/problems/find-all-groups-of-farmland/
'''


def findFarmland(land: list[list[int]]) -> list[list[int]]:
    ANSWER: list[list[int]] = []
    seen: set = set()

    farm_land_squares: set[tuple[int, int]] = set()
    '''
        Initalize set of farmland coords
    '''
    for r in range(len(land)):
        for c in range(len(land[0])):
            if land[r][c] == 1:
                farm_land_squares.add((r, c))

    def explore(start_Y: int, start_X: int) -> list[list[int, int, int, int]]:
        START = [start_Y, start_X]
        END = [start_Y, start_X]
        stack: list[tuple[int, int]] = [(start_Y, start_X)]

        while stack:
            y, x = stack.pop()

            if (y >= END[0] and x >= END[1]):
                END = [y, x]

            neighbours = [
                (a, b) for a, b in [(y-1, x),
                                    (y+1, x),
                                    (y, x-1),
                                    (y, x+1)]
                if (0 <= a < len(land) and 0 <= b < len(land[0])) and (a, b) not in seen and (a, b) in farm_land_squares]

            stack.extend(neighbours)
            seen.update(((a, b) for a, b in neighbours))
        return START+END

    for r in range(len(land)):
        for c in range(len(land[0])):
            if (r, c) not in seen and (r, c) in farm_land_squares:
                ANSWER.append(explore(r, c))
    return ANSWER

