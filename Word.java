import java.util.*;

public class World {
    public String[][] grid;
    public int size;

    public World(int size) {
        this.size = size;
        this.grid = new String[size][size];
        for (String[] row : grid) Arrays.fill(row, "");
        place("Wumpus");
        place("Gold");
        for (int i = 0; i < 3; i++) place("Pit");
    }

    private void place(String obj) {
        Random r = new Random();
        while (true) {
            int x = r.nextInt(size);
            int y = r.nextInt(size);
            if (grid[x][y].isEmpty() && !(x == 0 && y == 0)) {
                grid[x][y] = obj;
                break;
            }
        }
    }
}
