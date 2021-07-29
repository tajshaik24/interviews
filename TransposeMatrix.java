//Given a matrix A, return the transpose of A.
//The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

class Solution {
    public int[][] transpose(int[][] A) {
        int rows = A.length;
        int columns = A[0].length;
        int[][] transpose = new int[columns][rows];
        for (int r = 0; r < rows; ++r)
            for (int c = 0; c < columns; ++c) {
                transpose[c][r] = A[r][c];
            }
        return transpose;
    }
}