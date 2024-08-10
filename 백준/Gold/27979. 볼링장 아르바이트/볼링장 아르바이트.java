

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int[] balls;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        balls = new int[n];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            balls[i] = Integer.parseInt(st.nextToken());
        }

        boolean flag = false; //옮긴 볼링공이 있는지
        int moveMaxBall = -1; //옮긴 공중에 최대값
        int maxBall = balls[0];

        int result = 0;

        for (int i = 0; i < n; i++) {
            maxBall = Math.max(maxBall, balls[i]);

            if (balls[i] < maxBall) {
                flag = true;
                moveMaxBall = Math.max(moveMaxBall, balls[i]);
                balls[i] = Integer.MAX_VALUE;
                result++;
            }
        }

        if (flag) {
            for (int i = 0; i < n; i++) {

                if (balls[i] < moveMaxBall) {
                    result++;
                }
            }
        }
        System.out.println(result);
    }
}

