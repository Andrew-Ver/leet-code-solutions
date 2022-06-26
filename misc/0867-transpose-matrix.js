/**
 * https://leetcode.com/problems/transpose-matrix/
 */


 var transpose = function(matrix) {
    let new_matrix = [];
    const matrix_rows = matrix.length;
    const matrix_cols = matrix[0].length;

    for (let col=0; col < matrix_cols; col++){
        let new_row = [];
        for (let row=0; row < matrix_rows; row++){
            new_row.push(matrix[row][col]);
        }
        new_matrix.push(new_row);
    }
    return new_matrix;
};
