'''
    https://leetcode.com/problems/smallest-number-in-infinite-set/

    You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

    SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to 
    contain all positive integers.

    int popSmallest() Removes and returns the smallest integer contained 
    in the infinite set.

    void addBack(int num) Adds a positive integer num back into the infinite set, 
    if it is not already in the infinite set.

'''
import heapq


class SmallestInfiniteSet:    
    def __init__(self):
        '''
            Stored 'added backed' numbers in priority queue
            
            Use a set for o(1) lookup of currently 'added back' numbers
        '''    
        self.curr_smallest: int = 1
        self.q: list[int, int] = []
        self.added_back_numbers: set[int] = set()
        heapq.heapify(self.q)
        
    def popSmallest(self) -> int:
        if self.q:
            smallest_in_q = heapq.heappop(self.q)
            if smallest_in_q < self.curr_smallest:
                self.added_back_numbers.remove(smallest_in_q)
                return smallest_in_q
            heappush(self.q, smallest_in_q)
            n = self.curr_smallest
            self.curr_smallest += 1 
            return n
                     
        n: int = self.curr_smallest
        self.curr_smallest += 1
        return n

    def addBack(self, num: int) -> None:
        if num not in self.added_back_numbers and num < self.curr_smallest:
            heapq.heappush(self.q, num)
            self.added_back_numbers.add(num)
            
