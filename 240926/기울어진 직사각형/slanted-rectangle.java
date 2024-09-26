import java.util.*;

public class Main {
    static int n, answer, r, c;
    static int[][] li;
    static Map<Integer, int[]> m = new HashMap<>();

    // 사각형 탐색 및 점수 더하기
    static void dfs(int x, int y, int score, int dir){
        // 격자 밖이면 끝내
        if (x < 0 || x >= n || y < 0 || y >= n){
            return;
        }

        // 사각형 탐색 끝내서 처음 스타트 지점으로 왔으면 점수 합산 및 최대값 갱신
        // 출발지를 체크해두기 위해 r,c를 전역변수로 설정함
        if (x == r && y == c && dir == 4){
            if (answer < score){
                answer = score;
            }
            return;
        }

        // 현 위치에서 점수 더하기.
        score += li[x][y];
        // 방향이 이제 현재 진행방향, 그리고 이거 바로 직후의 진행방향 두가지만 가능하다.
        // 근데 제일 마지막 되돌아오는 경우에는 방향 하나만 존재한다.
        int end = (dir == 4)? 4 : dir + 1;
        for (int d = dir; d <= end; d++){
            int nx = x + m.get(d)[0];
            int ny = y + m.get(d)[1];

            dfs(nx, ny, score, d);
        }
    }

    public static void main(String[] args) {
        // 사각형 방향성. 순서가 존재하므로 이대로.
        m.put(1, new int[]{-1, 1});
        m.put(2, new int[]{-1, -1});
        m.put(3, new int[]{1, -1});
        m.put(4, new int[]{1, 1});


        // 입력받기.
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        li = new int[n][n];
        for (r = 0; r < n; r++){
            for (c = 0; c < n; c++){
                li[r][c] = sc.nextInt();
            }
        }


        answer = 0;
        // 일단 제일 작은 사각형하려면 행의 인덱스는 최소 2이어야하고, 열은 좌우 한칸씩은 좁은 상태에서 해야한다.
        for (r = 2; r < n; r++){
            for(c = 1; c < n - 1; c++){
                int tmp = 0;
                // 출발지 기준으로 여러 사각형이 나오니깐, 이는 dfs를 해두어야하고. 그리고 각 사각형마다의 점수가
                // 별도로 있기 떄문에, 이 점을 고려해서 점수도 지역변수로 두어서 함수 매개변수로 넣어야 한다.
                dfs(r, c, tmp, 1);
            }
        }

        System.out.println(answer);
        sc.close();
    }
}