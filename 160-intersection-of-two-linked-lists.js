/**
 * https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/
 * 
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
 var getIntersectionNode = function(headA, headB) {
    if (headA === headB) {
        return headA;
    }
    var seenNodes = new Set();
    
    while (headA || headB) {
        if (headA) {
            if (seenNodes.has(headA)) {
                return headA;
            }
            seenNodes.add(headA);
            headA = headA.next;
        }
        
        if (headB) {
            if (seenNodes.has(headB)) {
                return headB;
            }
            seenNodes.add(headB);
            headB = headB.next;
        }
    }
    return null;
};

