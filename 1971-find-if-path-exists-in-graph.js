/**
 * https://leetcode.com/problems/find-if-path-exists-in-graph/
 */

 var validPath = function(n, edges, source, destination) {
    const adj_list = {};

    for (let i=0; i<n; i++){
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
    if (!(source in adj_list) || !(destination in adj_list)){
        return false;
    }
    



    return adj_list;
};

console.log(validPath(3, [[3, 1], [1, 2], [2, 0]], 0, 2));
