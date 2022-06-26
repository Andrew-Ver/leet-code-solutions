'''
    https://leetcode.com/problems/keys-and-rooms/
'''


def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    '''
        Visit each room and collect its keys
        until cannot visit any more
    '''
    # Room zero is unlocked initially
    can_visit: list = [0]
    all_rooms: set = {r for r in range(len(rooms))}
    visited: set = set()

    while can_visit:
        room: int = can_visit.pop()
        visited.add(room)
        for key in rooms[room]:
            if key not in visited:
                can_visit.append(key)
    
    return visited.issuperset(all_rooms)


assert canVisitAllRooms(rooms = [[1],[2],[3],[]]) == True
assert canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]) == False