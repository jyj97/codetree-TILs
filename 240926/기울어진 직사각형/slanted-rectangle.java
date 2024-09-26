import java.util.*;

public class Main {
    static int n;
    static int[][] li;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        li = new int[n][n];
        for (int r = 0; r < n; r++){
            for (int c = 0; c < n; c++){
                li[r][c] = sc.nextInt();
            }
        }

        int answer = 0;
        for (int r = 2; r < n; r++){
            for(int c = 1; c < n - 1; c++){
                int tmp = li[r][c] + li[r - 1][c + 1] + li[r - 2][c] + li[r - 1][c - 1];

                int x1 = r - 1; int y1 = c + 1;
                int x2 = r - 2; int y2 = c;

                while(true){
                    x1 -= 1; y1 += 1;
                    x2 -= 1; y2 += 1;

                    if (x1 >= 0 && x1 < n && x2 >= 0 && x2 < n
                    && y1 >= 0 && y1 < n && y2 >= 0 && y2 < n){
                        tmp += (li[x1][y1] + li[x2][y2]);
                    }
                    else{
                        break;
                    }
                }

                if (tmp > answer){
                    answer = tmp;
                }

            }
        }

        System.out.println(answer);

    }
}