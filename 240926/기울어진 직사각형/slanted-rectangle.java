import java.util.*;

public class Main {
    static int n, answer, r, c;
    static int[][] li;
    static Map<Integer, int[]> m = new HashMap<>();

    static void dfs(int x, int y, int score, int dir){
        if (x < 0 || x >= n || y < 0 || y >= n){
            return;
        }

        if (x == r && y == c && dir == 4){
            if (answer < score){
                answer = score;
            }
            return;
        }

        score += li[x][y];
        for (int d = dir; d <= 4; d++){
            int nx = x + m.get(d)[0];
            int ny = y + m.get(d)[1];

            dfs(nx, ny, score, d);
        }

    }

    public static void main(String[] args) {
        m.put(1, new int[]{-1, 1});
        m.put(2, new int[]{-1, -1});
        m.put(3, new int[]{1, -1});
        m.put(4, new int[]{1, 1});


        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        li = new int[n][n];
        for (r = 0; r < n; r++){
            for (c = 0; c < n; c++){
                li[r][c] = sc.nextInt();
            }
        }

        answer = 0;
        for (r = 2; r < n; r++){
            for(c = 1; c < n - 1; c++){
                int tmp = 0;
                dfs(r, c, tmp, 1);
            }
        }

        System.out.println(answer);
        sc.close();
    }
}