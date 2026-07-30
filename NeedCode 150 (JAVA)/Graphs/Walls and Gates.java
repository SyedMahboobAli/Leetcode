import java.util.*;

class Solution {

    public void wallsAndGates(int[][] rooms) {

        if (rooms == null || rooms.length == 0)
            return;

        int m = rooms.length;
        int n = rooms[0].length;

        Queue<int[]> queue = new LinkedList<>();

        // Add all gates to the queue
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                }
            }
        }

        int[][] dirs = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        while (!queue.isEmpty()) {

            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];

            for (int[] d : dirs) {

                int nr = r + d[0];
                int nc = c + d[1];

                // Check boundaries
                if (nr < 0 || nr >= m || nc < 0 || nc >= n)
                    continue;

                // Visit only empty rooms
                if (rooms[nr][nc] != Integer.MAX_VALUE)
                    continue;

                rooms[nr][nc] = rooms[r][c] + 1;
                queue.offer(new int[]{nr, nc});
            }
        }
    }
}
