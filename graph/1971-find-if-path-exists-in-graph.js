/**
 * https://leetcode.com/problems/find-if-path-exists-in-graph/
 */


var validPath = function(n, edges, source, destination) {
    if (source == destination) {
        return true;
    }

    const adj_list = {};

    for (let i=0; i<edges.length; i++){
        let [A, B] = edges[i];
        
        if (A in adj_list){
            adj_list[A].push(B);
        }
        else {
            adj_list[A] = [B];
        }
        if (B in adj_list){
            adj_list[B].push(A);
        }
        else {
            adj_list[B] = [A];
        }
    }
    if (!(source in adj_list) || (!destination in adj_list)){
        return false;
    }
    
    var explore = [source];
    var seen = new Set();

    while (explore.length) {
        let node = explore.pop();
        seen.add(node);

        for (let n of adj_list[node]) {
            if (!seen.has(n)) {
                explore.push(n);
            }
        }
        
        if (node == destination) {
            return true;
        }
    }
    return false;
};

console.log(validPath(10, [[2,9],[7,8],[5,9],[7,2],[3,8],[2,8],[1,6],[3,0],[7,0],[8,5]], 1, 0));
