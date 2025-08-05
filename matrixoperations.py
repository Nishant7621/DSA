# User function Template for python3

class Solution:
    def endPoints(self, matrix, m, n):
        # Direction vectors: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Start moving to the right

        i, j = 0, 0  # Start position

        while 0 <= i < m and 0 <= j < n:
            if matrix[i][j] == 1:
                matrix[i][j] = 0
                dir_idx = (dir_idx + 1) % 4  # turn right

            # Move in the current direction
            i += directions[dir_idx][0]
            j += directions[dir_idx][1]

        # Last valid position before going out of bounds
        i -= directions[dir_idx][0]
        j -= directions[dir_idx][1]

        return (i, j)
