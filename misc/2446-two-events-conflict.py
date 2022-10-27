'''
	https://leetcode.com/problems/determine-if-two-events-have-conflict/

	You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:
		event1 = [startTime1, endTime1] and
    		event2 = [startTime2, endTime2].

	Event times are valid 24 hours format in the form of HH:MM.
	A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).
	Return true if there is a conflict between two events. Otherwise, return false.
'''

def haveConflict(event1: list[str], event2: list[str]) -> bool:
        time_A: tuple[int] = tuple(sum(int(v)*60 if i==0 else int(v) for i, v in enumerate(t.split(':'))) for t in event1)
        
        time_B: tuple[int] = tuple(sum(int(v)*60 if i==0 else int(v) for i, v in enumerate(t.split(':'))) for t in event2)
            
        return (time_A[0] <= time_B[0] <= time_A[1]) or (time_B[0] <= time_A[0] <= time_B [1])
